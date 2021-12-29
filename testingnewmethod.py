from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
data = requests.get('https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479').text
soup = BeautifulSoup(data, 'lxml')
soupdata = soup.findAll('h3', class_='story-text__heading-medium')
things = []
for elements in soupdata:
    info = elements.get_text()
    things.append(info)  #work done names

things.remove("Religion in schools")



moves = []
impact = []
upshot = []
story_text = soup.find_all("div", {"class":"story-text"})
story_text = story_text[2:]
for story in story_text:
    print(story.get_text())
    if "The move" not in story.get_text() or "The impact" not in story.get_text() or "The upshot" not in story.get_text():
        print("error here^^^^")
    else:
        storyparagraphs = story.find_all('p', {"class":"story-text__paragraph"})
        for element in storyparagraphs:
            if 'The move' in str(element):
                moves.append(element.get_text())
            if 'The impact' in str(element):
                impact.append(element.get_text())
            if 'The upshot' in str(element):
                upshot.append(element.get_text())

for i in range(len(things)):
    full_details = []
    full_details.append(things[i])
    full_details.append(moves[i])
    full_details.append("None")
    full_details.append("None")
    with open('details.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow(full_details)
        f.close()


