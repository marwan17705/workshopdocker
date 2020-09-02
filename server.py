#!/usr/bin/python3
#run ด้วย ./server.py
from flask import Flask,jsonify

app = Flask(__name__)
@app.route('/api/v1/info',methods=['GET'])
def info():
   return jsonify({'status':'success','name':'Marwan Waechi'})

@app.route('/api/v1/getdata',methods=['GET'])
def getdata():
   return jsonify({'status':'success'})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",threaded= True,port=5001)