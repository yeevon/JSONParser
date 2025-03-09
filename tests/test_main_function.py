import io
import unittest
import json_parser as jp
from unittest.mock import patch

class MyTestCase(unittest.TestCase):

    # Json file only contains: ""
    def test_empty_json_file(self):
        with patch('sys.argv', ["script_name", "../test_data/step1/invalid.json"]), patch(
            'sys.stdout', new_callable=io.StringIO) as fake_out:

            jp.main()
            output = fake_out.getvalue().strip()
            self.assertEqual(int(output), 1)

    # Json file contains: {}
    def test_valid_json_with_no_values(self):
        with patch('sys.argv', ["script_name", "../test_data/step1/valid.json"]), patch(
            'sys.stdout', new_callable=io.StringIO) as fake_out:

            jp.main()
            output = fake_out.getvalue().strip()

            expected_output = "0\n{}"
            self.assertEqual(output, expected_output)

    # Json file contains: {"key": "value",}
    def test_invalid_json_extra_comma(self):
        with patch('sys.argv', ["script_name", "../test_data/step2/invalid.json"]), patch(
            'sys.stdout', new_callable=io.StringIO) as fake_out:

            jp.main()
            output = fake_out.getvalue().strip()
            self.assertEqual(int(output), 1)

    # Json file contains:
    # {
    #   "key": "value",
    #   key2: "value"
    # }
    def test_invalid_json_invalid_key(self):
        with patch('sys.argv', ["script_name", "../test_data/step2/invalid2.json"]), patch(
            'sys.stdout', new_callable=io.StringIO) as fake_out:

            jp.main()
            output = fake_out.getvalue().strip()
            self.assertEqual(int(output), 1)

    # Json file contains: {"key": "value"}
    def test_valid_json_one_key_value_pair(self):
        with patch('sys.argv', ["script_name", "../test_data/step2/valid.json"]), patch(
                'sys.stdout', new_callable=io.StringIO) as fake_out:
            jp.main()
            output = fake_out.getvalue().strip()

            expected_output = "0\n{'key': 'value'}"
            self.assertEqual(output, expected_output)

    # Json file contains:
    # {
    #   "key": "value",
    #   "key2": "value"
    # }
    def test_valid_json_two_key_value_pair(self):
        with patch('sys.argv', ["script_name", "../test_data/step2/valid2.json"]), patch(
                'sys.stdout', new_callable=io.StringIO) as fake_out:
            jp.main()
            output = fake_out.getvalue().strip()

            expected_output = "0\n{'key': 'value', 'key2': 'value'}"
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
