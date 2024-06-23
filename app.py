#!/usr/bin/env python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def helloworld():
    if request.method == 'GET':
        name = request.args.get('name', 'World1')
        data = {"data": f"Hello {name}"}
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
