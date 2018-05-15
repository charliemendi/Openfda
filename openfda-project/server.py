import http.server
import socketserver
import http.client
import json
from flask import Flask, request, abort, redirect ,url_for
app = Flask(__name__)


@app.route("/redirect")
def redirect():
    return redirect(url_for("Sin_parametros"))
@app.route("/secret")
def secret():
    abort(401)
@app.route("/")
def Sin_parametros():
        archivo = """<!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>OpenFDA-project</title>
            </head>
            <body>
            <form action = "/listDrugs" method="get">
              <input type="submit" value="Fármacos">
                Limite: <input type="text" name="limit" value="1">
            </form>
            <form action = "/listCompanies" method="get">
              <input type="submit" value="Empresas">
                Limite: <input type="text" name="limit" value="1">
            </form>
            <form action = "/listWarnings" method="get">
              <input type="submit" value="Advertencias">
                Limite: <input type="text" name="limit" value="1">
            </form>
            <form action = "/searchDrug" method="get">
              <input type="submit" value="Buscar fármaco">
                Limite: <input type="text" name="limit" value="1">
                Campo: <input type="text" name="Principio activo" value="">
            </form>
            <form action = "/searchCompany" method="get">
              <input type="submit" value="Buscar empresas">
                Limite: <input type="text" name="limit" value="1">
                Campo: <input type="text" name="Nombre empresaa" value="">
            </form>
            </body>
            </html>"""
        return archivo
@app.route("/listDrugs")
def listDrugs():
    limit = request.args.get("limit")
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=" + limit, None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    n = 0
    List1 = []
    while n <= repos["meta"]["results"]["limit"]:
        try:
            List1.append(repos["results"][n]["openfda"]["generic_name"])
        except:
            List1.append("desconocido")
        n += 1
    contenido = """< !doctypehtml >
                                <html>
                                    <body style = 'background-color: blue' >
                                        <h1> Medicamentos </h2>
                                        <p> Generic_name: %s </p>
                                    </body >
                                </html >""" % (List1)
    return contenido
@app.route("/listWarnings")
def listWarnings():
    limit = request.args.get("limit")
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=" + limit, None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    n = 0
    List1 = []
    while n <= repos["meta"]["results"]["limit"]:
        try:
            List1.append(repos["results"][n]["warnings"])
        except:
            List1.append("desconocido")
        n += 1
    contenido = """< !doctypehtml >
                                <html>
                                    <body style = 'background-color: red' >
                                        <h1> Medicamentos </h2>
                                        <p> Advertencias: %s </p>
                                    </body >
                                </html >""" % (List1)
    return contenido
@app.route("/searchDrug")
def searchDrug():
    limit = request.args.get("limit")
    value=request.args.get("Principio activo")
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?search=active_ingredient:"  + value + "&limit=" + limit , None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    n = 0
    List1 = []
    while n <= repos["meta"]["results"]["limit"]:
        try:
            List1.append(repos["results"][n]["openfda"]["generic_name"])
        except:
            List1.append("desconocido")
        n += 1
    contenido = """< !doctypehtml >
                                <html>
                                    <body style = 'background-color: blue' >
                                        <h1> Medicamentos </h2>
                                        <p> Generic_name: %s </p>
                                    </body >
                                </html >""" % (List1)
    return contenido
@app.route("/searchCompany")
def searchCompany():
    limit = request.args.get("limit")
    value = request.args.get("Nombre empresaa")
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?search=openfda.manufacturer_name:" + value + "&limit=" + limit , None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    n = 0
    List1 = []
    while n <= repos["meta"]["results"]["limit"]:
        try:
            List1.append(repos["results"][n]["openfda"]["manufacturer_name"])
        except:
            List1.append("desconocido")
        n += 1
    contenido = """< !doctypehtml >
                                <html>
                                    <body style = 'background-color: green' >
                                        <h1> Medicamentos </h2>
                                        <p> Generic_name: %s </p>
                                    </body >
                                </html >""" % (List1)
    return contenido
@app.route("/listCompanies")
def listCompanies():
    limit = request.args.get("limit")
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=" + limit, None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    n = 0
    List2 = []
    while n <= repos["meta"]["results"]["limit"]:
        try:
            List2.append(repos["results"][n]["openfda"]["manufacturer_name"])
        except:
            List2.append("desconocido")
        n += 1
    contenido2 = """< !doctypehtml >
                                    <html>
                                        <body style = 'background-color: green' >
                                            <h1> Nombre de la empresa </h2>
                                            <p> manufacturer_name: %s </p>
                                        </body >
                                    </html >""" % (List2)
    return contenido2
socketserver.TCPServer.allow_reuse_address = True
if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8000)
