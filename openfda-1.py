import http.client
import json

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()

repos = json.loads(repos_raw)

repo = repos[0]
print("La id del producto es",["results"][0]["id"],"/n El proposito del producto es",["results"][0]["purpose"],"/n El nombre del fabricante es",["results"][0]["purpose"])



