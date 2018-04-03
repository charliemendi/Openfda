from flask import Flask

from flask import jsonify

from flask import request

app = Flask(__name__)

empDB=[

 {

 'ip':'212.128.255.155',

 'name':'Carlos',

 'title':'Ordenador'

 },

 ]

@app.route('/empdb/employee',methods=['GET'])

def getAllEmp():

    return jsonify({'emps':empDB})

@app.route('/empdb/employee/<empId>',methods=['GET'])

def getEmp(empId):

    usr = [ emp for emp in empDB if (emp['ip'] == empId) ]

    return jsonify({'emp':usr})

@app.route('/empdb/employee/<empId>',methods=['PUT'])

def updateEmp(empId):

    em = [ emp for emp in empDB if (emp['ip'] == empId) ]

    if 'name' in request.json :

        em[0]['name'] = request.json['name']

    if 'title' in request.json:

        em[0]['title'] = request.json['title']

    return jsonify({'emp':em[0]})

@app.route('/empdb/employee',methods=['POST'])

def createEmp():

    dat = {

    'ip':request.json['ip'],

    'name':request.json['name'],

    'title':request.json['title']

    }

    empDB.append(dat)

    return jsonify(dat)

@app.route('/empdb/employee/<empId>',methods=['DELETE'])

def deleteEmp(empId):

    em = [ emp for emp in empDB if (emp['ip'] == empId) ]

    if len(em) == 0:

       abort(404)

    empDB.remove(em[0])

    return jsonify({'response':'Success'})

if __name__ == '__main__':

 app.run(host="0.0.0.0",port=8080)


import urllib.request

with open("pagina_web", 'w') as g:

Web = urllib.request.urlopen("https://api.fda.gov/drug/label.json")

for linea in Web.readlines():
    g.write()
import json
with open('pagina_web') as json_file:
    data = json.load(json_file)
    for p in data['results']:
        for d in data["0"]:
            print('Propósito del producto: ' + p['purpose'])
            for c in data["openfda"]:
                print('id: ' + p['spl_id'])
                print('Nombre del fabricante: ' + p['manufacturer_name'])
