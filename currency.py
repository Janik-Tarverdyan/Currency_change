from flask import Flask, render_template,request
import requests
import os
path = os.getcwd()

response = requests.get("https://openexchangerates.org/api/latest.json?app_id=7808c1bc3f0343ff8daa562c3378378c&base=USD")
data = response.json()
Rates = data['rates']
key = ['SEK','EUR','PLN','USD']



app = Flask(__name__, template_folder=path + "/template")

@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'name':key[0]}, {'name':key[1]}, {'name':key[2]}, {'name':key[3]}],
    )


@app.route("/", methods=['GET', 'POST'])
def test():
    change_amount = float(request.form.get('change_amount'))
    select_from = request.form.get('select_from')
    select_to = request.form.get('select_to')
    select = [select_from,select_to]
    k = Rates[select[0]] / Rates[select[1]]
    result = change_amount * k

    return render_template(
        'index.html',
        amount=change_amount,
        opt1=select[0],
        opt2=select[1],
        data=[{'name':key[0]}, {'name':key[1]}, {'name':key[2]}, {'name':key[3]}],
        ch_res=result
    )

if  __name__ == "__main__":
    app.run()

