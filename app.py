from flask import Flask
from flask import request
from flask import Response
import json

import countvowels

app = Flask(__name__)

@app.route('/')
def countvar():
    x = str(request.args.get('x', default=""))
    answer = int(countvowels.countvowel(x))

    r = {
        "x": x,
        "answer": answer    
    }

    reply = json.dumps(r)

    response = Response(response=reply, status=200, mimetype="application/json")

    response.headers['Content-type']='application/json'
    response.headers['Access-Control-Allow-Origin']='*'

    return response
	 
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
