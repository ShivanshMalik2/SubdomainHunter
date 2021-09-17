import requests
import sys

domain = sys.argv[1]
valid = []
with open("subdomains.txt", "r") as lyst:
    for line in lyst:
        for word in line.split():
            url = f"https://{word}.{domain}"
            code = requests.get(url)

            if code.status_code < 400:
                 valid.append(url)
            else:
                pass
        else:
             print("[-] Discovered subdomain: ", url)

valid.append(url)
