import unittest
from unittest.mock import patch
from io import StringIO
from snakes_cafe import SnakesCafe

class TestSnakesCafe(unittest.TestCase):

    def setUp(self):
        self.cafe = SnakesCafe()

    def test_print_welcome_message(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.cafe.print_welcome_message()
            self.assertIn("Welcome to the Snakes Cafe", mock_output.getvalue())

    def test_print_menu(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.cafe.print_menu()
            self.assertIn("Appetizers", mock_output.getvalue())
            self.assertIn("Entrees", mock_output.getvalue())

    def test_add_to_order_valid_item(self):
        self.cafe.add_to_order("Wings")
        self.assertIn("Wings", self.cafe.order)

    def test_add_to_order_invalid_item(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.cafe.add_to_order("Invalid Item")
            self.assertIn("not on the menu", mock_output.getvalue())

    @patch('builtins.input', side_effect=['Wings', 'quit'])
    def test_start_ordering(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            self.cafe.start_ordering()
            self.assertIn("1 order(s) of Wings has been added", mock_output.getvalue())

if __name__ == '__main__':
    unittest.main()
