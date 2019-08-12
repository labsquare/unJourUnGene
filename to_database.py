import peewee
import markdown
from bs4 import BeautifulSoup
#from config import *

# api = twitter.Api(consumer_key=CONSUMER_KEY,
#                   consumer_secret=CONSUMER_SECRET,
#                   access_token_key=ACCESS_TOKEN_KEY,
#                   access_token_secret=ACCESS_TOKEN_SECRET)




with open("database.md","r") as file:
    md = markdown.Markdown()
    soup = BeautifulSoup(md.convert(file.read()), features="html.parser")

    for h1 in soup.findAll("h1"):
        gene = h1.getText()
            
        contents = []
        for child in h1.find_next_siblings():
            if child.name == "p":
                contents.append(child.contents)
            else:
                break

        print(contents)
        print("=====")

