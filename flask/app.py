# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:23:15 2021

@author: PRIYANKA REDDY
"""


# Importing of Libraries
from flask import Flask, render_template, request, redirect, url_for
import requests

# Flask App
app = Flask(__name__)
@app.route('/')

# Defining stats function 
def stats():
    url = "https://pp0t4wu0cg.execute-api.us-east-1.amazonaws.com/attendance_count"
    # Change the above url with your API Url
    response = requests.get(url)
    # Converting the json format
    r = response.json()
    print(r)
    # Rendering the html template
    return render_template('stats.html',a=sum(r),b=str(r[0]),c=str(r[1]),d=str(r[2]))

if __name__ == "__main__":
    app.run(debug=True)