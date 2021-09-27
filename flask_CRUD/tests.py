import random
import unittest
import main


class FlaskBootstrapTestCase(unittest.TestCase):
    # should fail unless configured postgres is running
    def setUp(self):
        app = main.create_app()
        app.debug = True
        self.app = app.test_client()


if __name__ == '__main__':
    unittest.main()