from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room


class TestRoom(TestCase):
    def setUp(self):
        self.room = Room("test_family", 100, 2)

    def test_init(self):
        self.assertEqual("test_family", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_with_valid_value(self):
        self.room.expenses = 20
        self.assertEqual(20, self.room.expenses)

    def test_expenses_with_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = - 10
        expected_res = "Expenses cannot be negative"
        self.assertEqual(expected_res, str(ex.exception))

    def test_calculate_expenses(self):
        self.assertEqual(0, self.room.expenses)
        child = Child(5, 4, 1)
        self.room.calculate_expenses([child])
        self.assertEqual(300, self.room.expenses)


if __name__ == '__main__':
    main()
