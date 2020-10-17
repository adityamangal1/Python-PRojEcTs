'''
Made by - Aditya mangal
Purpose - Task submission
Date  - 18 october 2020
'''
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time

chatbot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')


def Enrollment():
    print('Fill all the following details to submit the form.\n')
    user_name = input('Enter your name: ')
    user_location = input(
        'Enter your location which was suitable for the exam: \n')
    user_field_of_work = input('Enter your field of work: ')
    submission_date = input('Enter submission date: ')
    print('Searching nearest location.......')
    time.sleep(3)
    print('According to your submiited date', submission_date, 'and location',
          user_location, '\nLocations assigned to you are: Noida')
    print('Locations assigned to you are: Delhi ')
    print('Good luck!!')


print('\t\t\t A Chatot')
print('Type enrollment forms to enroll otherwise continue to talk with ChatBot')
print('You can exit by type exit\n')
while True:
    query = input(">> ")
    if 'exit' in query:
        exit()
    elif 'Enrollment Forms' and 'enrollment forms' in query:
        Enrollment()
    else:
        print(chatbot.get_response(query))
