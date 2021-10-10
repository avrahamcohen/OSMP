from project import app
from flask import escape, request, render_template
from project.controllers.XMLParser import *

@app.route("/", methods=['GET'])
def dashboard():
    names = []
    notes = []
    blocks = ""

    for name in getXmlTag("approved.xml", "name"):
        names.append(name.get_text())

    for note in getXmlTag("approved.xml", "notes"):
        notes.append(note.get_text())

    for i in range(0,len(names)):
        blocks = blocks + "<tr>"
        blocks = blocks + "<td>" + names[i] + "</td>"
        blocks = blocks + "<td>" + notes[i] + "</td>"
        blocks = blocks + "</tr>"

    return render_template("dashboard/index.html", user = 'Guest', blocks = blocks)

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
            blocks = blocks + "<td>" + notes[i] + "</td>"
            blocks = blocks + "</tr>"

    return render_template("dashboard/index.html", user = 'Guest', blocks = blocks)
