import unittest
from repositries import members_repository

class Test_members(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_in_login_failed_wrongpasssword(self):
        with self.assertRaises(Exception) as ex:
            members_repository.check_in_login("1", "1", "2")
        self.assertEqual("Wrong Password", str(ex.exception))
    
    def test_check_in_login_failed_wrongusername(self):
        with self.assertRaises(Exception) as ex:
            members_repository.check_in_login("1", "2", "1")
        self.assertEqual("Wrong username or not exist", str(ex.exception))
        
    def test_check_in_login_failed_wrongname(self):
        with self.assertRaises(Exception) as ex:
            members_repository.check_in_login("2", "1", "1")
        self.assertEqual("Name not registered", str(ex.exception))

    def test_signup_failed_username_inuse(self):
        with self.assertRaises(Exception) as ex:
            members_repository.sign_up("1", "1", "1")
        self.assertEqual("This username is used", str(ex.exception))

    def test_signup_failed_username_no_name(self):
        with self.assertRaises(Exception) as ex:
            members_repository.sign_up(None, "1", "1")
        self.assertEqual("info can't be None", str(ex.exception))

    def test_signup_failed_username_no_username(self):
        with self.assertRaises(Exception) as ex:
            members_repository.sign_up("1", None, "1")
        self.assertEqual("info can't be None", str(ex.exception))

    def test_signup_failed_username_no_password(self):
        with self.assertRaises(Exception) as ex:
            members_repository.sign_up("1", "1", None)
        self.assertEqual("info can't be None", str(ex.exception))


        
        