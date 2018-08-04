import requests
import pandas as pd


class SpaceConnector:
    URL = 'http://api.open-notify.org/astros.json'

    def __init__(self, adapter=requests):
        self.adapter=adapter

    def call(self):
        return self.adapter.get(url=self.URL)


class SpaceParser:
    def __init__(self, data):
        self.data = data

    def call(self):
        return self.data.json()['people']


class SpacePresenter:
    def __init__(self, data, data_frame=pd.DataFrame):
        self.data_frame=data_frame
        self.data = data

    def present(self):
        return str(self.data_frame(data=self.data))

    def __str__(self):
        return self.present()


class Space:
    def __init__(self, connector=SpaceConnector, parser=SpaceParser, presenter=SpacePresenter):
        self.connector = connector
        self.parser = parser
        self.presenter = presenter

    def get_people(self):
        data = self.connector().call()
        people = self.parser(data).call() 
        return self.presenter(people).present()

if __name__=='__main__':
    print(Space().get_people())
