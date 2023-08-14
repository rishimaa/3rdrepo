from lxml import html
import requests as HTTP
from bs4 import BeautifulSoup as SOUP
import re
import smtplib
import ssl
import base64
from datetime import datetime, timezone

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start>=0 and n>1:
        start = haystack.find(needle, start+len(needle))
        n-=1
    return start

def get_todays_horoscope(sunsign):
    d={}
    urlhere = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data,"lxml")
    title = soup.find('div', id="test").text
    f1 = find_nth(title,'(',2)
    f2 = title.find(')')
    x = title[f1+1:f2]
    return x

sun = input('Enter the sunsign:')
email = input("Enter the recievers email address")
sun = sun.capitalize()
fadd = "rangadurai.d@gmail.com"
tadd = email
text = get_todays_horoscope(sun)
username = 'rangadurai.d'
passwordEnc = 'XXXXXXXXXXXXXXXXXXXX'
base64_bytes = passwordEnc.encode('ascii')
message_bytes=base64.b64decode(base64_bytes)
password = message_bytes.decode('ascii')
date_utc = datetime.now(timezone.utc)
date_local = str(date_utc.astimezone()).split(' ')[0]
subject = 'Your Horoscope today ('+date_local+'):'+sun
msg = 'Subject: {}\n\n'.format(subject,text)
context = ssl.create_default_context()
server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo
server.starttls(context=context)
server.login(username,password)
server.sendmail(fadd,tadd,msg)
print("message sent")






    
