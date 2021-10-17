import re
from project import app
from bs4 import BeautifulSoup
from werkzeug.utils import unescape
from flask import escape, render_template

def getXmlTag(_file, _tag):
    match = re.search("^[A-Za-z]+.xml$", _file)
    if (match):
        infile = open("project/storage/" + _file,"r")
        contents = infile.read()
        soup = BeautifulSoup(contents,'xml')
        tags = soup.find_all(_tag)
        return tags

def removePackageXmlTag(_file, _data):
    valid = True
    match = re.search("^[A-Za-z]+.xml$", _file)
    valid = valid and match

    if (match):
        infile = open("project/storage/" + _file,"r")
        contents = infile.read()
        soup = BeautifulSoup(contents,'xml')
        infile.close()

        tag = "<package><name>" + escape(_data[0]) + "</name><licenses>" + escape(_data[1]) + "</licenses></package>"
        soup = str(soup).replace(unescape(tag),"")
        
        if (valid):
            outfile = open("project/storage/" + _file, "w")
            outfile.write(str(soup))
            outfile.close()

    return valid

def addPackageXmlTag(_file, _tag, _data):
    infile = open("project/storage/" + _file,"r")
    contents = infile.read()
    soup = BeautifulSoup(contents,'xml')
    tag = soup.new_tag("package")
    valid = True
    
    for i in range(0, len(_tag)):
        match = re.search("^[A-Za-z]+.xml$", _file)
        match = match and re.search("^[A-Za-z]+$", _tag[i])
        match = match and re.search("^[a-zA-Z\-\_0-9\.\ ]+$", _data[i])
        valid = valid and match
        if (match):
            
            newTag = soup.new_tag(_tag[i])
            newTag.string = _data[i]
            tag.append(newTag)

    soup.packages.insert(1, tag)
    infile.close()
   
    if (valid):
        outfile = open("project/storage/" + _file, "w")
        outfile.write(str(soup))
        outfile.close()

    return valid

def addLicensesXmlTag(_file, _tag, _data):
    infile = open("project/storage/" + _file,"r")
    contents = infile.read()
    soup = BeautifulSoup(contents,'xml')
    tag = soup.new_tag("license")
    valid = True
    
    for i in range(0, len(_tag)):
        match = re.search("^[A-Za-z]+.xml$", _file)
        match = match and re.search("^[A-Za-z]+$", _tag[i])
        match = match and re.search("^[a-zA-Z\-\_0-9\.\ ]+$", _data[i])
        valid = valid and match
        if (match):
            
            newTag = soup.new_tag(_tag[i])
            newTag.string = _data[i]
            tag.append(newTag)

    soup.licenses.insert(1, tag)
    infile.close()
   
    if (valid):
        outfile = open("project/storage/" + _file, "w")
        outfile.write(str(soup))
        outfile.close()

    return valid
