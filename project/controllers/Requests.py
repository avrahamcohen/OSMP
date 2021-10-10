from project import app
from project.controllers.XMLParser import *
from flask import redirect, request, render_template, escape

@app.route("/requests/pending", methods=['GET'])
def pending():
    names = []
    licenses = []
    blocks = ""

    for name in getXmlTag("pending.xml", "name"):
        names.append(name.get_text())

    for license in getXmlTag("pending.xml", "licenses"):
        licenses.append(license.get_text())

    for i in range(0,len(names)):
        blocks = blocks + "<tr>"
        blocks = blocks + "<td>" + names[i] + " | " + licenses[i] +  "</td>"
        blocks = blocks + "<td>"
        blocks = blocks + "<div class=\"w3-container\">"
        blocks = blocks + "<div class=\"w3-section\">"
        blocks = blocks + "<button class=\"w3-button w3-green\">Accept</button>"
        blocks = blocks + "<button class=\"w3-button w3-red\">Decline</button>"
        blocks = blocks + "</div>"
        blocks = blocks + "</div>"
        blocks = blocks + "</td>"
        blocks = blocks + "</tr>"

    return render_template("requests/pending/index.html", user = 'Guest', blocks = blocks)

@app.route("/requests/pending.do", methods=['GET'])
def pending_do():
    return redirect("/requests/pending", code=302)

@app.route("/requests/search.do", methods=['POST'])
def requests_search_do():
    names = []
    licenses = []
    blocks = ""
    filter_form = escape(request.form.get('filter-form'))

    for name in getXmlTag("pending.xml", "name"):
        names.append(name.get_text())

    for license in getXmlTag("pending.xml", "licenses"):
        licenses.append(license.get_text())

    for i in range(0,len(names)):
        if ((filter_form in names[i]) or (filter_form in licenses[i])):
            blocks = blocks + "<tr>"
            blocks = blocks + "<td>" + names[i] + " | " + licenses[i] +  "</td>"
            blocks = blocks + "<td>"
            blocks = blocks + "<div class=\"w3-container\">"
            blocks = blocks + "<div class=\"w3-section\">"
            blocks = blocks + "<button class=\"w3-button w3-green\">Accept</button>"
            blocks = blocks + "<button class=\"w3-button w3-red\">Decline</button>"
            blocks = blocks + "</div>"
            blocks = blocks + "</div>"
            blocks = blocks + "</td>"
            blocks = blocks + "</tr>"
    
    return render_template("requests/pending/index.html", user = 'Guest', blocks = blocks)

@app.route("/requests/new", methods=['GET'])
def create():
    return render_template("requests/new/index.html", user = 'Guest', blocks = '')

@app.route("/requests/new.do", methods=['POST'])
def create_do():
    jar = escape(request.form.get('package'))
    licenses = escape(request.form.get('licenses'))
    addXmlTag("pending.xml", ["name", "licenses"], [jar, licenses])
    return redirect("/requests/pending", code=302)
