import http.server
import socketserver
import http.client
import json
from flask import Flask, request, abort, redirect,render_template,url_for
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
                Limite: <input type="text" name="limit" value="">
            </form>
            <form action = "/listCompanies" method="get">
              <input type="submit" value="Empresas">
                Limite: <input type="text" name="limit" value="">
            </form>
            <form action = "/listWarnings" method="get">
              <input type="submit" value="Advertencias">
                Limite: <input type="text" name="limit" value="">
            </form>
            <form action = "/searchDrug" method="get">
              <input type="submit" value="Buscar fármaco">
                Limite: <input type="text" name="limit" value="">
                Campo: <input type="text" name="active_ingredient" value="Aspirin">
            </form>
            <form action = "/searchCompany" method="get">
              <input type="submit" value="Buscar empresas">
                Limite: <input type="text" name="limit" value="">
                Campo: <input type="text" name="company" value="Bayer">
            </form>
            <form action = "/secret" method="get">
              <input type="submit" value="secret">
            </form>
            <form action = "/redirect" method="get">
              <input type="submit" value="redirect">
            </form>
            </body>
            </html>"""
        return archivo
@app.route("/listDrugs")
def listDrugs():
    if request.args.get('limit'):
        limit = request.args.get('limit')
    else:
        limit = 10
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=" + limit, None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    contenido = """
                        <!doctype html>
                        <html>
                            <body style='background-color: blue' >
                             <h1> Medicamentos </h2>
                             <p>Generic_name:</p>
                            </body>
                        </html>
                        """
    limite = repos["meta"]["results"]["limit"]
    print(limite)
    for i in range(0, limite):
        try:
            name = repos["results"][i]["openfda"]["generic_name"]
        except:
            name = "desconocido"
        contenido += "<li>{}.\n".format(name)
    return contenido

@app.route("/listWarnings")
def listWarnings():
    if request.args.get('limit'):
        limit = request.args.get('limit')
    else:
        limit = 10
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=" + limit, None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    contenido = """
                    <!doctype html>
                    <html>
                        <body style='background-color: orange' >
                         <h1> Medicamentos </h1>
                         <p>Advertencias:</p>
                         <ul>{names}</ul>
                         
                        </body>
                    </html>
                    """
    contenido_list = ''
    for i in range(0, repos["meta"]["results"]["limit"]):
        try:
            nombre = repos["results"][i]["openfda"]["generic_name"]
        except:
            nombre = "medicamento desconocido"
        try:
            advertencia = repos["results"][i]["warnings"]
        except:
            advertencia = "advertencia desconocida"
        contenido_list += "<li>{}. {}</li>".format(nombre, advertencia)
    contenido = contenido.format(names=contenido_list)
    return contenido

@app.route("/searchDrug")
def searchDrug():
    if request.args.get('limit'):
        limit = request.args.get('limit')
    else:
        limit = 10
    value=request.args.get("active_ingredient")
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?search=active_ingredient:"+ value +"&limit=" + str(limit), None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    contenido = """
                            <!doctype html>
                            <html>
                                <body style='background-color: red' >
                                 <h1> Medicamentos </h2>
                                 <p>Generic_name:</p>
                                 <ul>{names}</ul>
                                </body>
                            </html>
                            """
    contenido_list = ''
    for i in range(0, repos["meta"]["results"]["limit"]):
        id = repos["results"][i]["id"]
        try:
            name = repos["results"][i]["purpose"]
        except:
            name = "desconocido"
        contenido_list += "<li>{}</li>".format(id, name)
    contenido = contenido.format(names=contenido_list)
    return contenido

@app.route("/searchCompany")
def searchCompany():
    if request.args.get('limit'):
        limit = request.args.get('limit')
    else:
        limit = 10
    value = request.args.get("company")
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?search=openfda.manufacturer_name:" + value + "&limit=" + str(limit) , None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    contenido = """
                            <!doctype html>
                            <html>
                                <body style='background-color: yellow' >
                                 <h1> Medicamentos </h2>
                                 <p>Company:</p>
                                 <ul>{company}</ul>
                                </body>
                            </html>
                            """
    contenido_list = ''
    for i in range(0, repos["meta"]["results"]["limit"]):
        try:
            name = repos["results"][i]["openfda"]["generic_name"]
        except:
            name = "desconocido"
        if isinstance(name, list):
            for i_name in name:
                contenido_list += "<li>{}</li>".format(i_name)
        else:
            contenido_list += "<li>{}</li>".format(name)
    contenido = contenido.format(company=contenido_list)
    return contenido

@app.route("/listCompanies")
def listCompanies():
    if request.args.get('limit'):
        limit = request.args.get('limit')
    else:
        limit = 10
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=" + limit, None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    contenido = """
                    <!doctype html>
                    <html>
                        <body style='background-color: green' >
                         <h1> Nombre de la empresa </h2>
                         <p>manufacturer_name</p>
                         <ul>{manufacturer_name}<ul>
                        </body>
                    </html>
                    """
    contenido_list = ''
    for i in range(0, repos["meta"]["results"]["limit"]):
        try:
            name = repos["results"][i]["openfda"]["manufacturer_name"]
        except:
            name = "desconocido"
        if isinstance(name, list):
            for i_name in name:
                contenido_list += "<li>{}</li>".format(i_name)
        else:
            contenido_list += "<li>{}</li>".format(name)
    contenido = contenido.format(manufacturer_name=contenido_list)
    return contenido

@app.route("/secret")
def secret():
    abort(401)
@app.route("/redirect")
def redirect():
    return "", 302, {'location': 'http://localhost:8000'}
@app.errorhandler(404)
def error():
    contenido="""<!doctype html>
                <html>
                    <body>
                     <p>Has cometido un error</p>
                     <p><a href="https://localhost:8000">Vuelve al inicio</a></p>
                    </body>
                </html>"""
    return render_template(contenido), 404
socketserver.TCPServer.allow_reuse_address = True
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


