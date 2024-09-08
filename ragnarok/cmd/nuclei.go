/*
Copyright © 2024 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"fmt"
	"sync"

	nuclei "github.com/projectdiscovery/nuclei/v3/lib"
	"github.com/projectdiscovery/nuclei/v3/pkg/output"
	"github.com/spf13/cobra"
)

// nucleiCmd represents the nuclei command
var nucleiCmd = &cobra.Command{
	Use:   "nuclei",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("nuclei called")
	},
}

func init() {
	rootCmd.AddCommand(nucleiCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// nucleiCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// nucleiCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
	fmt.Println("nuclei called")

	wg := &sync.WaitGroup{}
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
