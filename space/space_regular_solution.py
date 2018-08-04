import requests
import pandas as pd

r = requests.get(url='http://api.open-notify.org/astros.json')
people = r.json()['people']

df = pd.DataFrame(data=people)

print(df)