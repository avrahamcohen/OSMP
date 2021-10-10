from project import app 
from flask_wtf.csrf import CSRFError
from flask import render_template, request, render_template_string, redirect, session, make_response

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return redirect('/')

@app.route("/error.do", methods=['GET'])
def error():
    return redirect('/')

@app.errorhandler(400)
def page_not_found(e):
    return redirect('/')

@app.errorhandler(401)
def page_not_found(e):
    return redirect('/')

@app.errorhandler(403)
def page_not_found(e):
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

@app.errorhandler(408)
def page_not_found(e):
    return redirect('/')

@app.errorhandler(500)
def page_not_found(e):
    return redirect('/')

@app.errorhandler(502)
def page_not_found(e):
    return redirect('/')

@app.errorhandler(503)
def page_not_found(e):
    return redirect('/')

@app.errorhandler(504)
def page_not_found(e):
    return redirect('/')
