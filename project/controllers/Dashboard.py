from project import app
from flask import session, escape, request, render_template, url_for
from project.controllers.XMLParser import *

@app.route("/", methods=['GET'])
def dashboard():
    names = []
    notes = []
    blocks = ""
    
    try:
        session['username']
    except:
        session['username'] = 'Guest'

    for name in getXmlTag("approved.xml", "name"):
        names.append(name.get_text())

    for note in getXmlTag("approved.xml", "notes"):
        notes.append(note.get_text())

    for i in range(0,len(names)):
        blocks = blocks + "<tr>"
        blocks = blocks + "<td>" + names[i] + "</td>"
        blocks = blocks + "<td><a href=" + url_for("legal_search_internal", license = notes[i]) + " style=\"color: black;\">Read more</a></td>"
        blocks = blocks + "</tr>"
    
    return render_template("dashboard/index.html", user = session['username'], blocks = blocks, login = "/requests/new")

@app.route("/dashboard/search.do", methods=['POST'])
def dashboard_search_do():
    filter_form = escape(request.form.get('filter-form'))
    
    names = []
    notes = []
    blocks = ""

    for name in getXmlTag("approved.xml", "name"):
        names.append(name.get_text())

    for note in getXmlTag("approved.xml", "notes"):
        notes.append(note.get_text())

    for i in range(0,len(names)):
        if (filter_form in names[i]):
            blocks = blocks + "<tr>"
            blocks = blocks + "<td>" + names[i] + "</td>"
            blocks = blocks + "<td><a href=" + url_for("legal_search_internal", license = notes[i]) + " style=\"color: black;\">Read more</a></td>"
            blocks = blocks + "</tr>"

    return render_template("dashboard/index.html", user = session['username'], blocks = blocks)
