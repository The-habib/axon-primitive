// AXON 1.0 Go Standalone Core Verifier Engine (engines/axon_go.go)
package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"sort"
)

type AXONHeader struct {
	Version      string `json:"version"`
	ContentHash  string `json:"contentHash"`
	ContractHash string `json:"contractHash"`
	SemanticHash string `json:"semanticHash"`
}

type AXONPayload struct {
	Header     AXONHeader             `json:"header"`
	Data       map[string]interface{} `json:"data"`
	Schema     map[string]string      `json:"schema"`
	Invariants []string               `json:"invariants"`
}

func Canonicalize(v interface{}) string {
	switch val := v.(type) {
	case nil:
		return "null"
	case bool:
		if val {
			return "true"
		}
		return "false"
	case float64:
		return fmt.Sprintf("%v", val)
	case string:
		b, _ := json.Marshal(val)
		return string(b)
	case map[string]interface{}:
		keys := make([]string, 0, len(val))
		for k := range val {
			keys = append(keys, k)
		}
		sort.Strings(keys)
		res := "{"
		for i, k := range keys {
			kb, _ := json.Marshal(k)
			res += string(kb) + ":" + Canonicalize(val[k])
			if i < len(keys)-1 {
				res += ","
			}
		}
		return res + "}"
	}
	return fmt.Sprintf("%v", v)
}

func ComputeSHA256(str string) string {
	h := sha256.New()
	h.Write([]byte(str))
	return hex.EncodeToString(h.Sum(nil))
}

func VerifyAXON(payload AXONPayload) (string, error) {
	cData := Canonicalize(payload.Data)
	expContentHash := ComputeSHA256(cData)
	if expContentHash != payload.Header.ContentHash {
		return "FALSE", fmt.Errorf("content hash mismatch")
	}
	return "TRUE", nil
}

func main() {
	fmt.Println("✔ AXON 1.0 Go Core Engine compiled successfully")
}
