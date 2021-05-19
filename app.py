from flask import Flask, render_template, url_for, request
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    results = {}
    if request.method == "POST":
        # get url that the person has entered
            url = request.form['url']
            r = requests.get(url, verify=False)
            soup = BeautifulSoup(r.content)
            title = soup.title.string
            meta = soup.find_all('meta')

            for tag in meta:
                tag1,tag2 = [],[]
                if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['Description', 'Keywords']:
                    tag1.append(tag.attrs['name'].lower())
                    tag2.append(tag.attrs['content'])
                    return (tag1,tag2)
    
            return title
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

