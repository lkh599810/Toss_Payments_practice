from flask import Blueprint, request, make_response, jsonify, send_file, session, render_template, redirect,Flask
import http.client
from app import *


bp=Blueprint('view',__name__)

@bp.route('/', methods=['GET'])
def tosspayments():


    return render_template('tosspayments.html')



@bp.route('/tosspayments_success',methods=['GET'])
def tosspayments_success():

    paymentKey=request.args.get('paymentKey')
    orderId=request.args.get('orderId')
    amount=request.args.get('amount')

    conn = http.client.HTTPSConnection("api.tosspayments.com")
    formatting_string="{\"paymentKey\":\"{}\",\"amount\":{},\"orderId\":\"{}\"}"
    payload = """{{\"paymentKey\":\"{}\",\"amount\":{},\"orderId\":\"{}\"}}""".format(paymentKey,amount,orderId)


    headers = {
        'Authorization': "Basic dGVzdF9za196WExrS0V5cE5BcldtbzUwblgzbG1lYXhZRzVSOg==",
        'Content-Type': "application/json"
    }

    conn.request("POST", "/v1/payments/confirm", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    import json

    return render_template('tosspayments_success.html', data=json.loads(data.decode("utf-8")))


@bp.route('/tosspayments_fail',methods=['GET'])
def tosspayments_fail():
    return render_template('tosspayments_fail.html')



