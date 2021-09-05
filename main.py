from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import re

appFF = Flask(__name__)


def getInfo(username):
    try:
        url = "https://api.github.com/users/" + username
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        s = str(soup.text)
        s = re.sub('[''""{}]', "", s)
        li = list(s.split(","))
        print(li)
        li_res = [li[0], li[1], li[-3], li[-4], li[-6]]
        res = []
        for i in range(0, len(li_res)):
            s1 = (li_res[i].split(":"))
            res.append(s1)
        return res

    except:
        return getInfo('github')


@appFF.route('/')
def home():
    res= getInfo("github")
    return render_template('form.html', res=res, A="Attributes", V="Value")


@appFF.route('/predict', methods=['POST', 'GET'])
def predict():
    username = str(request.form.get("name"))
    print(username)
    res= getInfo(username)
    return render_template('form.html', A="Attributes", V="Value", res=res)


if __name__ == "__main__":
    appFF.run(debug=True)
