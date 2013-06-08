from bottle import route,run,template
from requests import get
@route('/')
@route('/hello/<name>')
def greet(name='STRANGER'):
	return template('Hello {{name}}, how r U ?', name=name)

@route('/gog')
def gog():
	r = get('http://google.co.in/')
	out = template('make_table', rows=list(r.headers))
	return out

run(host="localhost", port=8080, debug=True)

