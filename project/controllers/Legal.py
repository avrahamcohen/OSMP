from project import app
from project.controllers.XMLParser import *
from project.controllers.Login import access_control
from flask import session, escape, request, render_template, redirect, url_for

@app.route("/legal/licenses", methods=['GET'])
def list():
    names = []
    descriptions = []
    clearances = []
    embeds = []
    links = []
    publics = []
    distributions = []
    directs = []
    notes = []
    urls = []
    blocks = ""

    for name in getXmlTag("licenses.xml", "name"):
        names.append(name.get_text())
        
    for description in getXmlTag("licenses.xml", "description"):
        descriptions.append(description.get_text())
        
    for clearance in getXmlTag("licenses.xml", "clearance"):
        clearances.append(clearance.get_text())
        
    for embed in getXmlTag("licenses.xml", "embed"):
        embeds.append(embed.get_text())
        
    for link in getXmlTag("licenses.xml", "link"):
        links.append(link.get_text())
        
    for public in getXmlTag("licenses.xml", "public"):
        publics.append(public.get_text())
        
    for distribution in getXmlTag("licenses.xml", "distribution"):
        distributions.append(distribution.get_text())
        
    for direct in getXmlTag("licenses.xml", "direct"):
        directs.append(direct.get_text())
        
    for note in getXmlTag("licenses.xml", "notes"):
        notes.append(note.get_text())
        
    for url in getXmlTag("licenses.xml", "url"):
        urls.append(url.get_text())
        
    for i in range(0,len(names)):
        blocks = blocks + "<tr>"
        blocks = blocks + "<td><button type=\"button\" class=\"collapsible\" style=\"border: none;outline: none;background: transparent;\">" + names[i] + "</button>"
        blocks = blocks + "<div class=\"content\">"
        blocks = blocks + "<hr>"
        blocks = blocks + "<p>Description: " + descriptions[i] + "</p>"
        blocks = blocks + "<p>Clearance required: " + clearances[i] + "</p>"
        blocks = blocks + "<p>Can embed in our code: " + embeds[i] + "</p>"
        blocks = blocks + "<p>Can link as library: " + links[i] + "</p>"
        blocks = blocks + "<p>Can run as separate process using public API: " + publics[i] + "</p>"
        blocks = blocks + "<p>Offer to distribute 3rd party required: " + distributions[i] + "</p>"
        blocks = blocks + "<p>Directly provide 3rd party source: " + directs[i] + "</p>"
        blocks = blocks + "<p>Legal notes: " + notes[i] + "</p>"
        blocks = blocks + "<p>URL: " + urls[i] + "</p>"
        blocks = blocks + "</div>"
        blocks = blocks + "</td>"
        blocks = blocks + "</tr>"

    return render_template("legal/list/index.html", user = session['username'], blocks = blocks)

@app.route('/legal/licenses/<string:license>',methods=['GET'])
def legal_search_internal(license):
    return redirect(url_for(".legal_search_do", license = license))

@app.route("/legal/licenses/search.do", methods=['POST', 'GET'])
def legal_search_do():
    names = []
    descriptions = []
    clearances = []
    embeds = []
    links = []
    publics = []
    distributions = []
    directs = []
    notes = []
    urls = []
    blocks = ""
   
    try:
        filter_form = escape(request.form.get('filter-form'))
        redirect_form = escape(request.args['license'])
    except:
        pass

    for name in getXmlTag("licenses.xml", "name"):
        names.append(name.get_text())
        
    for description in getXmlTag("licenses.xml", "description"):
        descriptions.append(description.get_text())
        
    for clearance in getXmlTag("licenses.xml", "clearance"):
        clearances.append(clearance.get_text())
        
    for embed in getXmlTag("licenses.xml", "embed"):
        embeds.append(embed.get_text())
        
    for link in getXmlTag("licenses.xml", "link"):
        links.append(link.get_text())
        
    for public in getXmlTag("licenses.xml", "public"):
        publics.append(public.get_text())
        
    for distribution in getXmlTag("licenses.xml", "distribution"):
        distributions.append(distribution.get_text())
        
    for direct in getXmlTag("licenses.xml", "direct"):
        directs.append(direct.get_text())
        
    for note in getXmlTag("licenses.xml", "notes"):
        notes.append(note.get_text())
        
    for url in getXmlTag("licenses.xml", "url"):
        urls.append(url.get_text())
        
    for i in range(0,len(names)):
        if ((filter_form in names[i]) or (redirect_form in names[i])):
            blocks = blocks + "<tr>"
            blocks = blocks + "<td><button type=\"button\" class=\"collapsible\" style=\"border: none;outline: none;background: transparent;\">" + names[i] + "</button>"
            blocks = blocks + "<div class=\"content\">"
            blocks = blocks + "<hr>"
            blocks = blocks + "<p>Description: " + descriptions[i] + "</p>"
            blocks = blocks + "<p>Clearance required: " + clearances[i] + "</p>"
            blocks = blocks + "<p>Can embed in our code: " + embeds[i] + "</p>"
            blocks = blocks + "<p>Can link as library: " + links[i] + "</p>"
            blocks = blocks + "<p>Can run as separate process using public API: " + publics[i] + "</p>"
            blocks = blocks + "<p>Offer to distribute 3rd party required: " + distributions[i] + "</p>"
            blocks = blocks + "<p>Directly provide 3rd party source: " + directs[i] + "</p>"
            blocks = blocks + "<p>Legal notes: " + notes[i] + "</p>"
            blocks = blocks + "<p>URL: " + urls[i] + "</p>"
            blocks = blocks + "</div>"
            blocks = blocks + "</td>"
            blocks = blocks + "</tr>"

    return render_template("legal/list/index.html", user = session['username'], blocks = blocks)

@app.route("/legal/licenses/add", methods=['GET'])
def new():
    if (access_control() == False):
        return redirect("/", code=302)
    
    return render_template("legal/add/index.html", user = session['username'], blocks = '')

@app.route("/legal/licenses/add.do", methods=['POST'])
def new_do():
    if (access_control() == False):
        return redirect("/", code=302)

    license = escape(request.form.get('license'))
    description = escape(request.form.get('description'))
    clearance = escape(request.form.get('clearance'))
    embed = escape(request.form.get('embed'))
    link = escape(request.form.get('link'))
    public = escape(request.form.get('public'))
    distribute = escape(request.form.get('distribute'))
    direct = escape(request.form.get('direct'))
    notes = escape(request.form.get('notes'))
    url = escape(request.form.get('url'))
    
    tags = ["name", "description", "clearance", "embed", "link", "public", "distribution", "direct", "notes", "url"]
    data = [license, description, clearance, embed, link, public, distribute, direct, notes, url]
    
    valid = addLicensesXmlTag("licenses.xml", tags, data)

    if (valid == None):
        return render_template("legal/add/index.html", user = session['username'], blocks = '', error = "Invalid input")
    
    return redirect("/legal/licenses", code=302)
