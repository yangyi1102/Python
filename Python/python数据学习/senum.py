Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import Beautiful
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from bs4 import Beautiful
ImportError: cannot import name 'Beautiful'
>>> from bs4 import BeautifulSoup
>>> from urllib.request import urlopen
>>> html=urlopen("https://www.baidu.com/?tn=80035161_1_dg&ocid=msncn1-6')
	     
SyntaxError: EOL while scanning string literal
>>> html=urlopen("https://www.baidu.com/?tn=80035161_1_dg&ocid=msncn1-6")
>>> soup=BeautifulSoup(html,'html.parser')
>>> print(soup.prettify())
<html>
 <head>
  <script>
   location.replace(location.href.replace("https://","http://"));
  </script>
 </head>
 <body>
  <noscript>
   <meta content="0;url=http://www.baidu.com/" http-equiv="refresh"/>
  </noscript>
 </body>
</html>
>>> html=urlopen("https://jx.tmall.com/?ali_trackid=2:mm_121122127_23396474_77812994:1507964309_250_939250840")
>>> soup=soup=BeautifulSoup(html,'html.parser')
>>> print(soup.prettify())
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(soup.prettify())
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 8350-8350: Non-BMP character not supported in Tk
>>> import nltk
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    import nltk
ModuleNotFoundError: No module named 'nltk'
>>> import nltk
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
>>> import requests
>>> params={'firstname': 'Ryan', 'lastname': 'Mitchell'}
>>> r=requests.post("http://pythonscraping.com/files/processing.php", data=params)
>>> print(r.text)
Hello there, Ryan Mitchell!
>>> import requests
>>> params={'username':'Ryan','password':'password'}
>>> r=requests.postost("http://pythonscraping.com/pages/cookies/welcome.php", params)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    r=requests.postost("http://pythonscraping.com/pages/cookies/welcome.php", params)
AttributeError: module 'requests' has no attribute 'postost'
>>> r=requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
>>> print("Cookie is set to:")
Cookie is set to:
>>> print(r.cookies.get_dict())
{'loggedin': '1', 'username': 'Ryan'}
>>> print("----------")
----------
>>> 
>>> print("Going to profile psge...")
Going to profile psge...
>>> r=requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=r.cookies)
>>> print(r.text)
Hey Ryan! Looks like you're still logged into the site!
>>> import requests
>>> session=requests.Session()
>>> params={'username':'username','password':'password'}
>>> s=session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
>>> print("Cookie is set to:")
Cookie is set to:
>>> print(s.cookies.get_dict())
{'loggedin': '1', 'username': 'username'}
>>> print("---------")
---------
>>> s=session.get("http://pythonscraping.com/pages/cookies/profile.php")
>>> print(s.text)
Hey username! Looks like you're still logged into the site!
>>> 
