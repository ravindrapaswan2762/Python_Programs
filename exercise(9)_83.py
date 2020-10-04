# my apikey = 70530c21e4194c5f81f6a9faa5dc4ad7
# importing requests package
##############################################################################################

"""
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=70530c21e4194c5f81f6a9faa5dc4ad7"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])
        speak(article['title'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")
"""


############################### UPDATED ###########################################################

"""
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    speak("our first news is")
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=70530c21e4194c5f81f6a9faa5dc4ad7"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']

    for i in range(0, 7):
        print(i+1)
        print(arts[i]['title'])
        speak(arts[i]['title'])
 
        if i >= 6:
            break
        elif i == 5:
            speak("the last news is")
        else:
            speak("Moving on to the next news..Listen Carefully")

    speak("thanks for listening...")"""
###################################################################################
import requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Hello sir, i am jaarvis, how can i help you")
    speak("can i, sing a song, ok...")



