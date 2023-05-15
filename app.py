from flask import Flask
import os, time

import cProfile, pstats, io
from pstats import SortKey

app = Flask(__name__)
num = 1

def firstMethod():
    secondMethod() #Calling secondMethod
    return "I am done here"

def secondMethod():
    thirdMethod(2.5) #Calling thirdMethod 
    for loop in range(1): #CPU time spent
        for index in range(121474838):
            num * index
    thirdMethod(5) #Calling thirdMethod again

def thirdMethod(n):
    time.sleep(n) #Sleep

@app.route("/")
def home():  

    pr = cProfile.Profile()
    pr.enable()
    result = firstMethod()

    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())

    return "%s!" %result

if __name__ == '__main__':
    app.run()
