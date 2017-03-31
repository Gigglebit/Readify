import json
from flask import jsonify
from flask import Flask, make_response,Response
from flask import request
app = Flask(__name__)



def makeMyResponse(data = "Hello World", code = 200):
	response = make_response(data, code, {"pragma": "no-cache",
						  "server": "Microsoft-IIS/8.0",
						  "x-aspnet-version": "4.0.30319",
						  "x-powered-by": "ASP.NET",
						  "vary": "Accept-Encoding",
						  "content-type": "application/json; charset=utf-8",
						  "cache-control": "no-cache",
						  "expires": "-1"})		
	return response

@app.route("/")
def hello():

    return makeMyResponse()

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

@app.route("/api/Fibonacci")  
def fibonacci():
	n = request.args.get('n')
	if n.isdigit() and int(n) >= 0:
		fib_num = fib(int(n))
		return makeMyResponse(str(fib_num),200)
	else:
		return makeMyResponse(json.dumps({"message": "The request is invalid."}),400)
	

@app.route("/api/ReverseWords")
def reverseWords():
	sentence = request.args.get('sentence')
	words = sentence.split(" ")
	n_words = len(words)
	reversed_words = ""
	for i in xrange(n_words):
		reversed_words+=words[i][::-1]
		if i!= n_words:
			reversed_words+=" "
	return makeMyResponse(reversed_words,200)

@app.route("/api/Token")
def getToken():
	return makeMyResponse("\"d41c19f7-b2a3-41be-8190-6531d2200b3f\"",200)

@app.route("/api/TriangleType")
def triangleType():
	a = request.args.get('a')
	b = request.args.get('b')
	c = request.args.get('c')
	triType = "Error"
	if a.isdigit() and b.isdigit() and c.isdigit():
		if int(a)+int(b)>int(c) and int(b)+int(c)>int(a) and int(c)+int(a)>int(b):
			if a==b==c:
				triType="Equilateral"
			elif a!=b!=c:
				triType="Scalene"
			else:
				triType="Isosceles"
	else:
		return makeMyResponse(json.dumps({"message": "The request is invalid."}),400)
	result = "\"%s\"" % triType
	return makeMyResponse(result,200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000, debug = True)