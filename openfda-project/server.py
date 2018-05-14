import http.server
import socketserver
import http.client
import json
from flask import Flask
app = Flask(__name__)
@app.route("/")
def Sin_parametros():
    archivo ="""<!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>OpenFDA-project</title>
            </head>
            <body>
    
            <form action = "/listDrugs" method="get">
              <input type="submit" value="Listar fármacos">
                Limite: <input type="text" name="limit" value="1">
            </form>
    
            <form action = "/manufacturer_name" method="get">
              <input type="submit" value="Listar empresas">
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
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=10", None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()

    repos = json.loads(repos_raw)
    n = 0
    List1 = []
    while n != 10:
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
def listDrugs():
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=10", None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()

    repos = json.loads(repos_raw)
    n = 0
    List1 = []
    while n != 10:
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
def listDrugs():
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=10", None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()

    repos = json.loads(repos_raw)
    n = 0
    List1 = []
    while n != 10:
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
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=10", None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()

    repos = json.loads(repos_raw)
    n = 0
    List2 = []
    while n != 10:
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
    app.run(host='0.0.0.0', port=5399)
