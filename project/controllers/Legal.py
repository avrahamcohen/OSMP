from project import app
from flask import render_template

from project import app
from flask import escape, request, render_template
from project.controllers.XMLParser import *

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

    return render_template("legal/list/index.html", user = 'Guest', blocks = blocks)

@app.route("/legal/licenses/search.do", methods=['POST'])
def legal_search_do():
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

    return render_template("legal/list/index.html", user = 'Guest', blocks = '')

@app.route("/legal/licenses/add", methods=['GET'])
def new():
    return render_template("legal/add/index.html", user = 'Guest', blocks = '')
