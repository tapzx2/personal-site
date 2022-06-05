# build index

# append(header)
# for item in layout
#    append(h3(item))
#     for sub-item in item
#        if directory
#            append(makeLink(sub-item'.html'))
#         if file
#            append(makeLink(sub-item))
# append(links)
# append(tail)


import os
import re

index = os.path.expanduser("~/personal-site/www/index.html")
layout = os.path.expanduser("~/personal-site/layout/")

# clear and make freshhhhhhhh
if os.path.isfile(index):
    os.remove(index)
    file = open(f"{index}", "w")
    file.close()


# write output to file
def append(string):
    file1 = open(index, "a")
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


head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="resources/css/tuzz-github.css">
    <link rel="stylesheet" href="resources/css/style.css">
    <title>Nicholas Tapia's Personal Page</title>
</head>
<body>
"""

body = ""
body += '<div class="title"><h1>Nicholas Tapia\'s Personal Page</h1> <p>Hello! I\'m a human working in cyber security at JPMC. I used to be a dancer. Sometimes I front end.</p></div>'
headers = sorted(os.listdir(layout))
for h3 in headers:
    if h3[0] != ".":
        body += '<div class="column">'
        body += f"<h3>{cleanUp(h3)}</h3>\n"
        for link in sorted(os.listdir(layout+h3)):
            if link[0] != ".":
                if os.path.isdir(layout+h3+"/"+link):
                    body += f'<p><a href="{stripSort(link)}.html">{cleanUp(link)}</a></p>' + '\n'
                else:
                    body += f'<p><a href="{stripSort(link)}">{striphtml(cleanUp(link))}</a></p>' + '\n'
        body += "</div>"
body += '</div><div class="column"><img id="profileImg" src="resources/photos/nicholas-profile-smallv3.jpg"></div></body>'

tail = """</body>
</html>
"""

append(head)
append(body)
append(tail)
