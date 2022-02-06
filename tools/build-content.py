from bs4 import BeautifulSoup
import os
import re

www = os.path.expanduser("~/personal-site/www/")
layout = os.path.expanduser("~/personal-site/layout/")

prehead = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="resources/css/tuzz-github.css">
    <link rel="stylesheet" href="resources/css/style.css">
    <title>
"""

posthead = """</title>
</head>
<body>"""

tail = """</body>
</html>
"""

# clear and make freshhhhhhhh


def startFresh(file):
    if os.path.isfile(file):
        os.remove(file)
        file1 = open(f"{file}", "w")
        file1.close()


# write output to file
def append(string, file):
    file1 = open(file, "a")
    file1.write(string)
    file1.close()


# strip sort
def stripSort(string):
    return re.sub('^[0-9]*-', '', string)


# clean string
def cleanUp(string):
    return stripSort(string).replace("-", " ")


# strip html
def striphtml(string):
    return string.replace(".html", "")


def getTitle(input):
    """
    returns the first h1 contents of an html page
    """
    with open(input, 'r') as file:
        file = file.read()
    soup = BeautifulSoup(file, features="html.parser")
    if soup.h1 is not None:
        return soup.h1.string
    else:
        return "ERROR IN getTITLE FUNCTION"


def buildBlurbBody(dir):
    """
    returns a string of the files in dir, reverse numerical sort
    """
    body = ""
    blurbs = sorted(os.listdir(dir), reverse=True)
    for blurb in blurbs:
        path = dir + "/" + blurb
        if os.path.isfile(path) and blurb[0] != ".":
            with open(dir + "/" + blurb, 'r') as blurbName:
                body += blurbName.read()
    return body


def buildHtml(input, saveLoc, name):
    """
    Writes an html file with parameters: html body, output location, and output file name. 
    """
    #print("input: " + input)
    #print("saveLoc: " + saveLoc)
    #print("name: " + name)
    if os.path.isfile(input):
        page = saveLoc + stripSort(name)
        with open(input, 'r') as body:
            body = body.read()
        title = getTitle(input)
    else:
        page = saveLoc + stripSort(name) + ".html"
        body = input
        title = cleanUp(name)

    startFresh(page)
    append(prehead, page)
    append(title, page)
    append(posthead, page)
    append(body, page)
    append(tail, page)


# main
headers = sorted(os.listdir(layout))
for h3 in headers:
    if os.path.isdir(layout+h3):
        for name in sorted(os.listdir(layout+h3)):
            path = layout+h3+"/"+name
            if name[-5:] == ".html":
                #print("item is html: " + item)
                buildHtml(path, www, name)
            elif os.path.isdir(path):
                #print("item is directory: " + name)
                buildHtml(buildBlurbBody(path), www, name)
            else:
                print("item is neither .html file or directory: " + name)
