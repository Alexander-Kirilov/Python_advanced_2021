from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.pfactory = PaintFactory("Test", 10)

    def test_init_method(self):
        self.assertEqual("Test", self.pfactory.name)
        self.assertEqual(10, self.pfactory.capacity)
        self.assertEqual({}, self.pfactory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pfactory.valid_ingredients)
        self.assertEqual({}, self.pfactory.ingredients)

    def test_can_add(self):
        self.assertTrue(self.pfactory.can_add(5))
        self.assertFalse(self.pfactory.can_add(11))

    def test_add_ingredient_with_invalid_capacity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pfactory.add_ingredient("blue", 12)
        expected_res = "Not enough space in factory"
        actual_res = str(ex.exception)
        self.assertEqual(expected_res, actual_res)

    def test_add_ingredient_invalid_type_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.pfactory.add_ingredient("test", 5)
        expected_res = "Ingredient of type test not allowed in PaintFactory"
        actual_res = str(ex.exception)
        self.assertEqual(expected_res, actual_res)

    def test_add_ingredient_with_valid_input(self):
        self.assertEqual({}, self.pfactory.ingredients)
        self.pfactory.add_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.pfactory.ingredients)

    def test_remove_ingredient_with_valid_values(self):
        self.pfactory.add_ingredient("blue", 2)
        self.pfactory.remove_ingredient("blue", 1)
        self.assertEqual({"blue": 1}, self.pfactory.ingredients)

    def test_remove_ingredient_with_invalid_type_raises(self):
        self.pfactory.add_ingredient("blue", 5)
        with self.assertRaises(ValueError) as ex:
            self.pfactory.remove_ingredient("blue", 6)
        expected_res = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected_res, str(ex.exception))

    def test_remove_ingredient_with_invalid_key_raises(self):
        with self.assertRaises(KeyError) as ex:
            self.pfactory.remove_ingredient("test", 1)
        expected_res = "'No such ingredient in the factory'"
        self.assertEqual(expected_res, str(ex.exception))

    def test_repr_method(self):
        self.pfactory.ingredients = {"blue": 1, "white": 2}
        expected_res = "Factory name: Test with capacity 10.\n" \
                        "blue: 1\n"\
                        "white: 2\n"
        self.assertEqual(expected_res, repr(self.pfactory))


if __name__ == '__main__':
    main()
