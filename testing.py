from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# from textblob import TextBlob as tb
    
# def web(a):
#     driver = webdriver.Chrome()
#     driver.get(a)
#     sleep(1)
#     a = driver.find_element_by_tag_name('h1').text
#     print(a)
#     return a
    

# a = input("input link berita")
# web(a)
# sentimen = tb(a).sentiment.polarity
# if sentimen < 0:
#     mood = "Komenan jahat nih ( negatif )"
# elif sentimen == 0:
#     mood = "Komenan standar lah ( normal )"
# else :
#     mood = "Buset seneng bet ni komenan diliat liat ( positif ) "

# print(mood)


from flask import Flask, render_template, request
import requests
from urllib.parse import urlparse
from textblob import TextBlob as tb

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST': 
        link = request.form['link']
        driver = webdriver.Chrome()
        driver.get(link)
        sleep(1)
        a = driver.find_element_by_tag_name('h1').text
        sentimen = tb(a).sentiment.polarity
        if sentimen < 0:
            mood = "negatif"
        elif sentimen == 0:
            mood = "normal"
        else :
            mood = "positif"
        # print(f"\n\n\ncomments:\n{comments}")
        # print(f"\n\n\ncomments no satu :\n{komen[0]}")
        # print(f"\n\n\nhasil blob:\n{sentimen}")
        # print(f"count comment: {len(comments)}")
        # print("finished.")
        return render_template('index.html', link = link, mood = mood, a = a)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
