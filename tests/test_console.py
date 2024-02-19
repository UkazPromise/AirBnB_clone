import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User first_name='John' last_name='Doe'")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Assuming UUID length is 36 characters

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User first_name='John' last_name='Doe'")
            output = f.getvalue().strip()
            user_id = output

            with patch('sys.stdout', new=StringIO()) as f_show:
                HBNBCommand().onecmd(f"show User {user_id}")
                show_output = f_show.getvalue().strip()
                self.assertIn(user_id, show_output)

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User first_name='John' last_name='Doe'")
            output = f.getvalue().strip()
            user_id = output

            with patch('sys.stdout', new=StringIO()) as f_count:
                HBNBCommand().onecmd(f"count User")
                count_before_destroy = int(f_count.getvalue().strip())

            with patch('sys.stdout', new=StringIO()) as f_destroy:
                HBNBCommand().onecmd(f"destroy User {user_id}")
                destroy_output = f_destroy.getvalue().strip()
                self.assertEqual(destroy_output, "")

            with patch('sys.stdout', new=StringIO()) as f_count:
                HBNBCommand().onecmd(f"count User")
                count_after_destroy = int(f_count.getvalue().strip())
                self.assertEqual(count_after_destroy, count_before_destroy - 1)

    

if __name__ == '__main__':
    unittest.main()

