import json

# Dummy mapping for demonstration
technique_map = {
    "PowerShell": "T1059.001",
    "Mimikatz": "T1003.001",
    "Base64": "T1140"
}

def map_alerts(logs):
    mapped = []
    for log in logs:
        for keyword, technique in technique_map.items():
            if keyword.lower() in json.dumps(log).lower():
                log['mitre_technique'] = technique
                mapped.append(log)
    return mapped

if __name__ == "__main__":
    logs = [{"message": "Suspicious PowerShell execution detected"}]
    enriched = map_alerts(logs)
    print(json.dumps(enriched, indent=2))
