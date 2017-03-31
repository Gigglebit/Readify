import re
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
	a, b = 0, 1
	if n == 0:
		return a
	if n == 1:
		return b
	if n > 0:
		for i in xrange(n):
			a, b = b, a+b

	else: 
		for i in xrange(n,0):
			a, b = b-a, a

	return a
	# if n == 0:
	# 	return 0
	# elif n == 1:
	# 	return 1
	# else:
	# 	if n > 0:
	# 		return fib(n-1)+fib(n-2)
	# 	if n < 0:
	# 		return fib(n+2)-fib(n+1)

@app.route("/api/fibonacci")  
def fibonacci():
	n = request.args.get('n')
	#print n.isdigit(),n[0]=="-",n[1::].isdigit()
	if (n.isdigit() or (n[0]=="-" and n[1::].isdigit()) and abs(int(n))<=92):

		fib_num = fib(int(n))
		print fib_num
		if fib_num == "error":
			return makeMyResponse(json.dumps({"message": "The request is invalid."}),400)
		return makeMyResponse(str(fib_num),200)
	else:
		return makeMyResponse(json.dumps({"message": "The request is invalid."}),400)
	

@app.route("/api/reversewords")
def reverseWords():
	sentence = request.args.get('sentence')
	reversed_words =""
	words = sentence.split(" ")
	words = re.sub("[^\w]", " ",  sentence).split()
	n_words = len(words)
	for i in xrange(n_words):
		reversed_words+=words[i][::-1]
		if i!= n_words:
			reversed_words+=" "
	result = "\"%s\"" % reversed_words	
	return makeMyResponse(result,200)

@app.route("/api/token")
def getToken():
	return makeMyResponse("\"d41c19f7-b2a3-41be-8190-6531d2200b3f\"",200)

@app.route("/api/triangletype")
def triangleType():
	a = request.args.get('a')
	b = request.args.get('b')
	c = request.args.get('c')
	triType = "Error"
	if int(a)<=0 or int(b)<=0 or int(c)<=0:
		result = "\"%s\"" % triType
		return makeMyResponse(result,200)
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
    app.run(host='0.0.0.0', port = 80, debug = True)