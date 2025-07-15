import requests
import json

def lookup_ip(ip):
    headers = {'X-OTX-API-KEY': 'YOUR_API_KEY'}
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general"
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {}

if __name__ == "__main__":
    sample_ip = "8.8.8.8"
    print(f"Looking up threat intel for {sample_ip}")
    result = lookup_ip(sample_ip)
    print(json.dumps(result, indent=2))
