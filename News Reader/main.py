import requests
import json
from termcolor import cprint


def speak(str):
    from win32com.client import Dispatch
    tell = Dispatch("SAPI.spvoice")
    tell.speak(str)


if __name__ == "__main__":
    cprint("#" * 50, "magenta")
    cprint((f"Latest news reader ").center(50), "yellow")
    cprint("#" * 50, "magenta")
    speak("good morning")
    url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-08-07&sortBy=publishedAt&apiKey=e684369eea9446d19026cf7281f207c9"
    news = requests.get(url).text
    latest_news = json.loads(news)
    news_reader = latest_news["articles"]
    speak("today's latest news are")
    for articles in news_reader:

        print("\t\t**Today Latest News**\t\t")
        speak(articles['title'])
        print("News:- ", articles['title'])
        speak("Moving on to the next news..Listen Carefully")

speak("thank you for listening")
print("\t\tThank you for listening..")
