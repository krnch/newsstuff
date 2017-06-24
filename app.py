from flask import Flask, render_template
app= Flask (__name__)
apikey='3169bba2dc224d789955587d3544e310'
from itertools import repeat
import requests
@app.route("/")
def main():
    r=requests.get("https://newsapi.org/v1/articles?source=techcrunch&apiKey="+apikey)

    resp=r.json()
    l=len(resp['articles'])
    d = [[] for i in repeat(None, l)]
    p=0
    for i in resp['articles']:
	d[p].append (i['title'])
	d[p].append (i['url'])
       	d[p].append (i['urlToImage'])
       	p=p+1

    return render_template('index.html',
                           title='Home',
                           tags=d)

if __name__ == "__main__":
    app.run()
