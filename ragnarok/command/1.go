package main

import (
	"fmt"

	nuclei "github.com/projectdiscovery/nuclei/v3/lib"
)

func main() {
	// Create a new Nuclei engine
	engine, _ := nuclei.NewNucleiEngine(nuclei.WithTemplatesOrWorkflows(
		nuclei.TemplateSources{
			Templates: []string{"template.yaml"},
		}),
	)

	// Define targets
	engine.LoadTargets([]string{"testphp.vulnweb.com/listproducts.php?cat=1"}, false)

	// Execute the scan
	results := engine.ExecuteWithCallback(nil)

	// Process results
	fmt.Printf("Found vulnerability: %s\n", results)
}
