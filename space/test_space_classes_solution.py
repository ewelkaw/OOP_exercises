import unittest
from open_notify_classes import SpaceConnector, SpaceParser, SpacePresenter, Space

class SpaceTestCase(unittest.TestCase):
    def test_space_connector(self):
        class RequestMock:
            def get(self, url):
                return 'test'

        connector = SpaceConnector(RequestMock())
        self.assertEqual(connector.call(), 'test')

    def test_spac_parser(self):
        class ParserDataMock:
            def __init__(self, data):
                self.data = data

            def json(self):
                return self.data

        parser = SpaceParser(ParserDataMock({'people': 'test'}))
        self.assertEqual(parser.call(), 'test')

    def test_space_presenter(self):
        def data_frame_mock(data):
            return data
            
        presenter = SpacePresenter('test', data_frame_mock)
        self.assertEqual(presenter.present(), 'test')

    def test_space(self):
        class ConnectorMock:
            def call(self):
                return 'test'


        class ParserMock:
            def __init__(self, data):
                self.data = data

            def call(self):
                return self.data


        class PresenterMock:
            def __init__(self, data):
                self.data = data

            def present(self):
                return self.data


        space = Space(ConnectorMock, ParserMock, PresenterMock)
        self.assertEqual(space.get_people(), 'test')

if __name__ == '__main__':
    unittest.main()
