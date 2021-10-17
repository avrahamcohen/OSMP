from project import app
from project.controllers.XMLParser import *
from flask import session, url_for, redirect, request, render_template, escape

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
        
        if (access_control() == False):
            blocks = blocks + "<td>"
            blocks = blocks + "Pending"
            blocks = blocks + "</td>"
        if (access_control() == True):
            blocks = blocks + "<td>"
            blocks = blocks + "<div class=\"w3-container\">"
            blocks = blocks + "<div class=\"w3-section\">"
            blocks = blocks + "<a href=" + url_for("request_approved", entry = str(names[i] + "|" + licenses[i])) + " style=\"color: black;\">Approve</a>"
            blocks = blocks + " | "
            blocks = blocks + "<a href=" + url_for("request_rejected", entry = str(names[i] + "|" + licenses[i])) + " style=\"color: black;\">Reject</a>"
            blocks = blocks + "</div>"
            blocks = blocks + "</div>"
            blocks = blocks + "</td>"
            blocks = blocks + "</tr>"

    return render_template("requests/pending/index.html", user = session['username'], blocks = blocks)

@app.route('/request/approve/<string:entry>',methods=['GET'])
def request_approved(entry):
    if (access_control() == False):
        return redirect("/", code=302)

    entry = escape(entry)
    entry = entry.split("|")
    
    tags = ["name", "notes"]
    data = [entry[0], entry[1]]

    addPackageXmlTag("approved.xml", tags, data)
    removePackageXmlTag("pending.xml", data)
   
    return redirect("/requests/pending", code=302)

@app.route('/request/reject/<string:entry>',methods=['GET'])
def request_rejected(entry):
    if (access_control() == False):
        return redirect("/", code=302)

    entry = escape(entry)
    entry = entry.split("|")
    
    data = [entry[0], entry[1]]

    removePackageXmlTag("pending.xml", data)
   
    return redirect("/requests/pending", code=302)

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
        
            if (access_control() == False):
                blocks = blocks + "<td>"
                blocks = blocks + "Pending"
                blocks = blocks + "</td>"
            if (access_control() == True):
                blocks = blocks + "<td>"
                blocks = blocks + "<div class=\"w3-container\">"
                blocks = blocks + "<div class=\"w3-section\">"
                blocks = blocks + "<a href=" + url_for("request_approved", entry = str(names[i] + "|" + licenses[i])) + " style=\"color: black;\">Approve</a>"
                blocks = blocks + " | "
                blocks = blocks + "<a href=" + url_for("request_rejected", entry = str(names[i] + "|" + licenses[i])) + " style=\"color: black;\">Reject</a>"
                blocks = blocks + "</div>"
                blocks = blocks + "</div>"
                blocks = blocks + "</td>"
                blocks = blocks + "</tr>"
    
    return render_template("requests/pending/index.html", user = session['username'], blocks = blocks)

@app.route("/requests/new", methods=['GET'])
def create():
    return render_template("requests/new/index.html", user = 'Guest', blocks = '')

@app.route("/requests/new.do", methods=['POST'])
def create_do():
    jar = escape(request.form.get('package'))
    licenses = escape(request.form.get('licenses'))

    tags = ["name", "licenses"]
    data = [jar, licenses]

    valid = addPackageXmlTag("pending.xml", tags, data)
   
    if (valid == None):
        return render_template("requests/new/index.html", user = session['username'], blocks = '', error = "Invalid input")
    
    return redirect("/requests/pending", code=302)
