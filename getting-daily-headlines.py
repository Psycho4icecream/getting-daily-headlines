import requests
from bs4 import BeautifulSoup
import pyttsx3
import xmltodict

def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    return engine

def say(engine, txt):
    engine.say(txt)
    engine.runAndWait()


tts = init_engine()

def bbcDailyHeadlines():
    print('BBC')
    url='https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    unwanted = ['BBC World News TV', 'BBC World Service Radio',
            'News daily newsletter', 'Mobile app', 'Get in touch']

    for x in list(dict.fromkeys(headlines)):
        if x.text.strip() not in unwanted:
            print(x.text.strip())
            say(tts, x.text.strip())

    print()

def dwDailyHeadlines():
    print('DW')
    url='https://www.dw.com/en/top-stories/s-9097'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h2')

    for x in headlines:
        print(x.text.strip())
        say(tts, x.text.strip())

    print()

def aljazeeraDailyHeadlines():
    print('Al Jazeera')
    url='https://www.aljazeera.com/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    unwanted = ['Related Stories']

    for x in list(dict.fromkeys(headlines)):
        if x.text.strip() not in unwanted:
            print(x.text.strip())
            say(tts, x.text.strip())

    print()

def nytimesDailyHeadlines():
    print('NYTimes')
    url='https://www.nytimes.com/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    unwanted = ['Advertisement', 'The Editorial Board', 'Listen to Times Articles, Narrated for You', 'Read the Cooking Newsletter', 'Read the On Soccer Newsletter', 'Take the Weakly Health Quiz']

    for x in list(dict.fromkeys(headlines)):
        if x.text.strip() not in unwanted:
            print(x.text.strip())
            say(tts, x.text.strip())

    print()

bbcDailyHeadlines()

dwDailyHeadlines()

aljazeeraDailyHeadlines()

nytimesDailyHeadlines()