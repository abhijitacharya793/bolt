package main

import (
	"fmt"
	"os"

	"github.com/go-git/go-git/v5"
	"github.com/projectdiscovery/nuclei/v3/core"
)

func main() {
	// Clone the GitHub repository
	_, err := git.PlainClone("path/to/local/repo", false, &git.CloneOptions{
		URL:      "https://github.com/your-username/your-repo.git",
		Depth:    1, // Clone only the latest commit
		Progress: os.Stdout,
	})
	if err != nil {
		fmt.Println("Failed to clone repository:", err)
		return
	}

	// Get the path to the templates directory (adjust as needed)
	templatesDir := "path/to/local/repo/templates"

	// Create a Nuclei engine
	engine := core.NewNucleiEngine()

	// Load templates from the cloned directory
	err = engine.LoadTemplates([]string{templatesDir})
	if err != nil {
		fmt.Println("Error loading templates:", err)
		return
	}

	// ... rest of your Nuclei code ...
}
