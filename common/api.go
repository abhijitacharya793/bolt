package common

type Healthz struct {
	Server   string `json:"server"`
	Database string `json:"database"`
}

type Parameters struct {
	Target          string `json:"target"`
	RootDomain      string `json:"rootDomain"`
	Domain          string `json:"domain"`
	Protocol        string `json:"protocol"`
	ProtocolVersion string `json:"protocolVersion"`
	Port            string `json:"port"`
	Method          string `json:"method"`
	Path            string `json:"path"`
	Body            string `json:"body"`
}
