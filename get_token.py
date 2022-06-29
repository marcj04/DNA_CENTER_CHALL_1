import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_USER, DNAC_PASSWORD, DNAC_IP, DNAC_PORT

def get_token():
    url = "https://" + DNAC_IP + "/dna/system/api/v1/auth/token"
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify=False)
    token = resp.json()
    return token['Token']

if __name__ == "__main__":
    get_token()
