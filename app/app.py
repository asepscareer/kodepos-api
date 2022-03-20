from flask import Flask, request
from src.res import success, badRequest
from src.base import get_daerah, setup_provinsi, setup_nasional, getdata_nasional, getdata_provinsi, get_paginated_list

app = Flask(__name__)

@app.route('/api/v1/daftar-daerah', methods=['GET'])
def getdaerah():
    response = get_daerah()
    return success(response)

@app.route('/api/v1/reset-data-provinsi', methods=['GET'])
def setupprovinsi():
    response = setup_provinsi()
    return success(response)

@app.route('/api/v1/get-data-provinsi/<provinsi_name>', methods=['GET'])
def getdataprovinsi(provinsi_name):
    try:
        provinsi = provinsi_name
        response = getdata_provinsi(params=provinsi)
        return success(response)
    except:
        response = 'Sesuaikan dengan yang ada pada endpoint Get Daftar Provinsi'
        return badRequest(message= response, values= None)

@app.route('/api/v1/reset-data-nasional', methods=['GET'])
def setupnasional():
    response = setup_nasional()
    return success(response)

@app.route('/api/v1/get-data-nasional', methods=['GET'])
def getdatanasional():
    response = getdata_nasional()
    return success(response)

@app.route('/api/v1/get-nasional', methods=['GET'])
def getnasional2():
    data = getdata_nasional()
    response = get_paginated_list(
        data, '/api/v1/get-nasional',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 20)
        )
    return success(response)
    