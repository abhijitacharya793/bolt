package handler

import (
	"database/sql"
	"log"
	"net/http"

	"github.com/go-chi/chi"
	"github.com/go-chi/cors"

	"github.com/abhijitacharya793/yggdrasil/internal/database"

	_ "github.com/lib/pq"
)

type apiConfig struct {
	DB *database.Queries
}

func Handle(port string, dbUrl string) {
	// Init database connection
	portString := port
	dbURL := dbUrl

	conn, err := sql.Open("postgres", dbURL)
	if err != nil {
		log.Fatal("Can't connect to database")
	}

	apiCfg := apiConfig{
		DB: database.New(conn),
	}

	// new router
	router := chi.NewRouter()
	router.Use(cors.Handler(cors.Options{
		AllowedOrigins:   []string{"https://*", "http://*"},
		AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowedHeaders:   []string{"*"},
		ExposedHeaders:   []string{"Link"},
		AllowCredentials: false,
		MaxAge:           300,
	}))

	// sub router
	v1Router := chi.NewRouter()

	// add endpoints
	v1Router.Get("/healthz", handlerReadiness)
	v1Router.Get("/err", handlerErr)

	v1Router.Post("/tag", apiCfg.handlerCreateTag)
	v1Router.Get("/tag", apiCfg.handlerGetTagByID)
	v1Router.Get("/tags", apiCfg.handlerListTag)
	v1Router.Delete("/tag", apiCfg.handlerDeleteTag)

	v1Router.Post("/fuzzing", apiCfg.handlerCreateFuzzing)
	v1Router.Get("/fuzzing", apiCfg.handlerGetFuzzingByID)
	v1Router.Get("/fuzzings", apiCfg.handlerListFuzzing)
	v1Router.Delete("/fuzzing", apiCfg.handlerDeleteFuzzing)

	v1Router.Post("/risk", apiCfg.handlerCreateRisk)
	v1Router.Get("/risk", apiCfg.handlerGetRiskByID)
	v1Router.Get("/risks", apiCfg.handlerListRisk)
	v1Router.Delete("/risk", apiCfg.handlerDeleteRisk)

	v1Router.Post("/vulnerability", apiCfg.handlerCreateVulnerability)
	v1Router.Get("/vulnerability", apiCfg.handlerGetVulnerabilityByID)
	v1Router.Get("/vulnerability/tags", apiCfg.handlerGetVulnerabilityTagByID)
	v1Router.Get("/vulnerability/fuzzings", apiCfg.handlerGetVulnerabilityFuzzingByID)
	v1Router.Get("/vulnerabilitys", apiCfg.handlerListVulnerability)
	v1Router.Delete("/vulnerability", apiCfg.handlerDeleteVulnerability)

	v1Router.Post("/template", apiCfg.handlerCreateTemplate)
	v1Router.Get("/template", apiCfg.handlerGetTemplateByID)
	v1Router.Get("/templates", apiCfg.handlerListTemplate)
	v1Router.Delete("/template", apiCfg.handlerDeleteTemplate)

	// router mount
	router.Mount("/yggdrasil/v1", v1Router)

	// create server and start
	srv := &http.Server{
		Handler: router,
		Addr:    ":" + portString,
	}

	log.Printf("Server starting on port %v", portString)
	err1 := srv.ListenAndServe()

	if err1 != nil {
		log.Fatal(err1)
	}
}
