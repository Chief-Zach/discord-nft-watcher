import requests
import json
from binance.spot import Spot
from decouple import config

API=config('API')
client = Spot()

url = "https://beta.api.solanalysis.com/rest/get-project-stats"

def get_price():
    payload = json.dumps({
      "conditions": {
        "project_ids": [
          "degenboyzdao1"
        ]
      }
    })
    headers = {  'Authorization': API,  'Content-Type': 'application/json'}
    original = requests.request("POST", url, headers=headers, data=payload)

    payload = json.dumps({
      "conditions": {
        "project_ids": [
          "9a8JV3n2N3vMfGKcV1gj89Pf34ZaKrZqkMs8VpEbhjKJ"
        ]
      }
    })
    headers = {  'Authorization': API,  'Content-Type': 'application/json'}
    radiated1 = requests.request("POST", url, headers=headers, data=payload)

    payload = json.dumps({
      "conditions": {
        "project_ids": [
          "kgPFYXgAzNje2z9NBTCyRx3uXkqXq2JMwxkW5cQtWDC"
        ]
      }
    })
    headers = {  'Authorization': API,  'Content-Type': 'application/json'}
    radiated2 = requests.request("POST", url, headers=headers, data=payload)

    payload = json.dumps({
      "conditions": {
        "project_ids": [
          "GfdmASNhXMdEBHcbABAzzWhsBfGtUuYABFezfV28xvvN"
        ]
      }
    })
    headers = {  'Authorization': API,  'Content-Type': 'application/json'}
    pharos = requests.request("POST", url, headers=headers, data=payload)


    return original.json()["project_stats"][0]["floor_price"], radiated1.json()["project_stats"][0]["floor_price"], radiated2.json()["project_stats"][0]["floor_price"], pharos.json()["project_stats"][0]["floor_price"]

def get_sol():
    print(round(float(client.ticker_price("SOLUSDT")["price"]), 2))
    return round(float(client.ticker_price("SOLUSDT")["price"]), 2)