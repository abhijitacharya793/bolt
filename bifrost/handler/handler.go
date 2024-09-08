package handler

import (
	"database/sql"
	"log"
	"net/http"

	"github.com/go-chi/chi"
	"github.com/go-chi/cors"

	"github.com/abhijitacharya793/bifrost/internal/database"

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
	v1Router.Post("/api", apiCfg.handlerCreateAPI)
	v1Router.Get("/api", apiCfg.handlerGetAPIByID)
	v1Router.Get("/apis", apiCfg.handlerListAPI)
	v1Router.Delete("/api", apiCfg.handlerDeleteAPI)
	v1Router.Get("/api/request", apiCfg.handlerAPIRequest)

	v1Router.Post("/query", apiCfg.handlerCreateQuery)
	v1Router.Get("/query", apiCfg.handlerGetQueryByID)
	v1Router.Get("/queries", apiCfg.handlerListQuery)

	v1Router.Post("/header", apiCfg.handlerCreateHeader)
	v1Router.Get("/header", apiCfg.handlerGetHeaderByID)
	v1Router.Get("/headers", apiCfg.handlerListHeader)

	// router mount
	router.Mount("/bifrost/v1", v1Router)

	// create server and start
	srv := &http.Server{
		Handler: router,
		Addr:    ":" + portString,
	}

	log.Printf("Server starting on port %v", portString)
	log.Printf("config: %v", dbURL)
	err1 := srv.ListenAndServe()

	if err1 != nil {
		log.Fatal(err1)
	}
}
