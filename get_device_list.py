import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD
from get_token import get_token
#from tabulate import tabulate

def get_device_list():
    url = "https://" + DNAC_IP + "/dna/intent/api/v1/network-device"
    token = get_token()
    print(url,token)
    hdr = {'X-Auth-Token': token, "Content-Type": "application/json"}
    print(hdr)
    resp = requests.get(url, headers=hdr, verify=False)
    device_list = resp.json()
    print_device_list(device_list)

def print_device_list(device_json):
    device_list = []
    for i in device_json['response']:
        temp_list = []
        temp_list += i[
        device_list += temp_list
        temp_list = []
    print(device_list)

if __name__ == "__main__":
    get_device_list()

