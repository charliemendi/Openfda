import http.server
import socketserver
import http.client
import json
from flask import Flask, request
app = Flask(__name__)


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

            <form action = "/manufacturer_name" method="get">
              <input type="submit" value="Empresas">
            </form>

            <form action = "/SearchDrug" method="get">
              <input type="submit" value="Buscar fármaco">
                Campo: <input type="text" name="Principio activo" value="">
            </form>

            <form action = "/SearchCompany" method="get">
              <input type="submit" value="Buscar empresas">
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
    print(limit)
    List1 = []
    while n != limit:
        try:
            List1.append(repos["results"][n]["openfda"]["generic_name"])
        except:
            print("desconocido")
        n += 1
    contenido = """< !doctypehtml >
                                <html>
                                    <body style = 'background-color: blue' >
                                        <h1> Medicamentos </h2>
                                        <p> Generic_name: %s </p>
                                    </body >
                                </html >""" % (List1)
    return contenido


@app.route("/SearchDrug")
def SearchDrug():
    limit = request.args.get("name")
    value=request.args.get("value")
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=" + limit + "&search=active_ingredient" + value, None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()

    repos = json.loads(repos_raw)
    n = 0
    List1 = []
    while n != limit:
        try:
            if value == repos["results"][n]["activate_ingredient"]:
                List1.append(repos["results"][n]["openfda"]["generic_name"])
            else:
                continue
        except:
            print("desconocido")
        n += 1
    contenido = """< !doctypehtml >
                                <html>
                                    <body style = 'background-color: blue' >
                                        <h1> Medicamentos </h2>
                                        <p> Generic_name: %s </p>
                                    </body >
                                </html >""" % (List1)
    return contenido


@app.route("/SearchCompany")
def SearchCompany():
    limit = request.args.get("name")
    value = request.args.get("value")
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=" + limit + "&search=openfda.manufacturer_name" + value, None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()

    repos = json.loads(repos_raw)
    n = 0
    List1 = []
    while n != limit:
        try:
            if value == repos["results"][n]["openfda"]["manufacturer_name"]:
                List1.append(repos["results"][n]["openfda"]["manufacturer_name"])
            else:
                continue
        except:
            print("desconocido")
        n += 1
    contenido = """< !doctypehtml >
                                <html>
                                    <body style = 'background-color: blue' >
                                        <h1> Medicamentos </h2>
                                        <p> Generic_name: %s </p>
                                    </body >
                                </html >""" % (List1)
    return contenido


@app.route("/manufacturer_name")
def manufacturer_name():
    limit = request.args.get("name")
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
    while n != limit:
        try:
            List2.append(repos["results"][n]["openfda"]["manufacturer_name"])
        except:
            print("Desconocido")
        n += 1
    contenido2 = """< !doctypehtml >
                                    <html>
                                        <body style = 'background-color: blue' >
                                            <h1> Nombre de la empresa </h2>
                                            <p> manufacturer_name: %s </p>
                                        </body >
                                    </html >""" % (List2)
    return contenido2


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5889)
