import unittest
from repositries import classes_repository

class Test_classes(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_return_current_weekday(self):
        expected_outcome = "wed"
        actual_outcome = classes_repository.return_current_weekday()
        self.assertEqual(expected_outcome, actual_outcome)

    def test_check_class_today(self):
        expected_outcome = ["Yoga"]
        list = classes_repository.check_class_today()
        actual_outcome = []
        for classes in list:
            actual_outcome.append(classes.name)
        self.assertEqual(expected_outcome, actual_outcome)
