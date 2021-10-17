import hashlib
from project import app
from flask import escape, render_template, request, render_template_string, redirect, session, make_response

def access_control():
    try:
        if ((session['authorization']) == 'authorized'):
            return True
    except:
        return False
    return False

@app.route("/login", methods=['GET'])
def login_login():  
    return render_template("login/index.html", user = ' Guest', error = '')

@app.route("/login/verify.do", methods=['POST', 'GET'])
def login_verify():
    #TODO make it more secure.
    session.clear()
    session['username'] = ' Guest'

    _username = escape(request.form.get('username'))
    _password = escape(request.form.get('password'))
    
    session['username'] = _username
    session['password'] = _password
    
    if ((_username == 'admin') and (_password == 'admin')):
        session['username'] = 'Admin'
        session['authorization'] = 'authorized'
        return redirect("/", code=302)
    else:
        return render_template("login/index.html", user = session['username'], error = 'Incorrect username or password.')

@app.route("/logout.do", methods=['GET'])
def login_logout():
    session.clear()
    session['username'] = ' Guest'
    return redirect("/", code=302)
