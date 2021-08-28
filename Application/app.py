from flask import Flask, request
import requests
import os

app = Flask(__name__)
api_key = os.environ['API_KEY']
username = os.environ['MY_NAME']
country = os.environ['COUNTRY']

@app.route('/')
def holidays_in_russia():
    from datetime import datetime, timedelta

    url = f"https://calendarific.com/api/v2/holidays?&api_key={api_key}&country={country}&year=2021"
    response = requests.get(url).json()

    all_holidays = response['response']['holidays']
    for i in all_holidays:
        elem_name = i.get('name')
        elem_date = i.get('date').get('iso')
        delta1 = datetime.today()
        delta2 = datetime.fromisoformat(elem_date)
        if delta1 < delta2.replace(tzinfo=None):
            return f"Hello, {username}! \nThe nearest Russian holiday is '{elem_name}'. Celebrated on {elem_date}."


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
