package main

import (
	"database/sql"
	"fmt"
	"github.com/google/uuid"
	"github.com/gookit/config/v2"
	"github.com/gookit/config/v2/yaml"
	_ "github.com/lib/pq"
	nuclei "github.com/projectdiscovery/nuclei/v3/lib"
	"github.com/projectdiscovery/nuclei/v3/pkg/output"
	"log"
	"sync"
)

type API struct {
	id               uuid.UUID
	created_at       string
	updated_at       string
	target           string
	root_domain      string
	domain           string
	protocol         string
	protocol_version string
	port             string
	method           string
	path             string
	body             string
}

func main() {
	// ################################## CONFIG ##################################
	config.WithOptions(config.ParseEnv)
	config.AddDriver(yaml.Driver)

	err := config.LoadFiles("config/dev.yml")
	if err != nil {
		panic(err)
	}

	// ################################# POSTGRES #################################
	dbURL := config.String("db_url")

	conn, err := sql.Open("postgres", dbURL)
	if err != nil {
		log.Fatal("Can't connect to database", err)
	}
	defer conn.Close()

	rows, _ := conn.Query("SELECT * from api")
	for rows.Next() {
		var data API
		err := rows.Scan(&data.id, &data.created_at, &data.updated_at, &data.target, &data.root_domain, &data.domain,
			&data.protocol, &data.protocol_version, &data.port, &data.method, &data.path, &data.body)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(data)
	}

	// ################################## NUCLEI ##################################
	wg := new(sync.WaitGroup)
	wg.Add(1)
	targets := map[string]string{
		"scanme.sh": "http",
	}
	go func(targets map[string]string) {
		for target, protocol := range targets {
			ne, _ := nuclei.NewNucleiEngine(nuclei.WithTemplateFilters(
				nuclei.TemplateFilters{
					ProtocolTypes: protocol,
					Severity:      "critical",
					ExcludeTags:   []string{"bruteforce", "dos", "fuzzing"},
				}),
			)

			ne.LoadTargets([]string{target}, false)

			_ = ne.ExecuteWithCallback(func(event *output.ResultEvent) {
				if target != event.URL {
					fmt.Printf("%s != %s\n", target, event.URL)
				}
			})

			ne.Close()
		}
		wg.Done()
	}(targets)

	wg.Wait()
}
