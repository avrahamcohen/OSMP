import re
from project import app
from bs4 import BeautifulSoup

def getXmlTag(_file, _tag):
    match = re.search("^[A-Za-z]+.xml$", _file)
    if (match):
        infile = open("project/storage/" + _file,"r")
        contents = infile.read()
        soup = BeautifulSoup(contents,'xml')
        tags = soup.find_all(_tag)
        return tags

def addXmlTag(_file, _tag, _data):
    infile = open("project/storage/" + _file,"r")
    contents = infile.read()
    soup = BeautifulSoup(contents,'xml')
    tag = soup.new_tag("package")
    
    for i in range(0, len(_tag)):
        match = re.search("^[A-Za-z]+.xml$", _file)
        match = match and re.search("^[A-Za-z]+$", _tag[i])
        match = match and re.search("^[a-zA-Z\-\_0-9\.]+$", _data[i])
        if (match):
            
            newTag = soup.new_tag(_tag[i])
            newTag.string = _data[i]
            tag.append(newTag)

    soup.packages.insert(1, tag)
    infile.close()
    
    outfile = open("project/storage/" + _file, "w")
    outfile.write(str(soup))
    outfile.close()
