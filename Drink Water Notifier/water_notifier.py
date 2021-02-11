

'''
Author: Aditya Mangal 
Date:  18 september,2020
Purpose: python practise problem

'''
from plyer import notification
import time



if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please drink water",
            message="it's good for your health to drink water regularly so plaease drink it on regular basis",
            app_icon=r"C:\Users\Aditya Mangal\Desktop\visual studio\python\ico.ico",
            timeout=5

        )
        time.sleep(4)
