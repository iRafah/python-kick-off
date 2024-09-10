import unittest
import script


class TestMain(unittest.TestCase):

    # set up any config that is required before each test runs.
    def setUp(self):
        print('let\'s test our functions')

    def test_sum_number(self):
        '''Comment that appears when the test runs'''
        test_param = 10
        result = script.sum_number(test_param)
        self.assertEqual(result, 15)

    def test_sum_number_value_error(self):
        test_param = 'string'
        result = script.sum_number(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff(self):
        test_param = None
        result = script.sum_number(test_param)
        self.assertEqual(result, 'Please enter a number')

    # run after each test - rarely used.
    def tearDown(self):
        print('Cleaning up')


# Run the tests on in the main file.
if __name__ == '__main__':
    unittest.main()
