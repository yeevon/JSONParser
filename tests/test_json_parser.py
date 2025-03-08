import io
import unittest
import json_parser as jp
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    def test_invalid_json(self):
        with patch('sys.argv', ["script_name", "../test_data/step1/invalid.json"]), patch(
            'sys.stdout', new_callable=io.StringIO) as fake_out:

            jp.main()
            output = fake_out.getvalue().strip()
            self.assertEqual(int(output), 1)

    def test_valid_json(self):
        with patch('sys.argv', ["script_name", "../test_data/step1/valid.json"]), patch(
            'sys.stdout', new_callable=io.StringIO) as fake_out:

            jp.main()
            output = fake_out.getvalue().strip()
            self.assertEqual(int(output), 0)


if __name__ == '__main__':
    unittest.main()
