from unittest import TestCase, main


from project.pet_shop import PetShop


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.ps = PetShop("Test_shop")

    def test_init(self):
        self.assertEqual("Test_shop", self.ps.name)
        self.assertEqual({}, self.ps.food)
        self.assertEqual([], self.ps.pets)

    def test_add_food_valid(self):
        self.assertEqual({}, self.ps.food)
        expected_res = "Successfully added 2.00 grams of test_food."
        self.assertEqual(expected_res, self.ps.add_food("test_food", 2))
        self.assertEqual({"test_food": 2}, self.ps.food)

    def test_add_food_invalid_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.ps.add_food("test_food", -2)
        expected_res = "Quantity cannot be equal to or less than 0"
        self.assertEqual(expected_res, str(ex.exception))

    def test_add_pet_valid(self):
        self.assertEqual([], self.ps.pets)
        self.assertEqual("Successfully added test_pet.", self.ps.add_pet("test_pet"))
        self.assertEqual(["test_pet"], self.ps.pets)

    def test_add_pet_with_same_name_raises(self):
        self.ps.add_pet("Sharo")
        with self.assertRaises(Exception) as ex:
            self.ps.add_pet("Sharo")
        expected_res = "Cannot add a pet with the same name"
        self.assertEqual(expected_res, str(ex.exception))
        self.assertEqual(["Sharo"], self.ps.pets)

    def test_feed_pet_valid(self):
        self.ps.add_pet("Sharo")
        self.ps.add_food("meat", 200)
        self.assertEqual(["Sharo"], self.ps.pets)
        self.assertEqual({"meat": 200}, self.ps.food)
        self.assertEqual("Sharo was successfully fed", self.ps.feed_pet("meat", "Sharo"))
        self.assertEqual({"meat": 100}, self.ps.food)

    def test_feed_pet_with_invalid_pet_name(self):
        self.ps.add_pet("Sharo")
        self.ps.add_food("meat", 200)
        self.assertEqual(["Sharo"], self.ps.pets)
        self.assertEqual({"meat": 200}, self.ps.food)
        with self.assertRaises(Exception) as ex:
            self.ps.feed_pet("meat", "Sarah")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_invalid_food_name(self):
        self.ps.add_pet("Sharo")
        self.ps.add_food("meat", 200)
        self.assertEqual(["Sharo"], self.ps.pets)
        self.assertEqual({"meat": 200}, self.ps.food)
        self.assertEqual("You do not have sweet", self.ps.feed_pet("sweet", "Sharo"))

    def test_feed_pet_add_food(self):
        self.ps.pets = ["Jerry"]
        self.ps.food = {"meat": 50}
        expected_result = "Adding food..."
        actual_result = self.ps.feed_pet("meat", "Jerry")
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(1050.0, self.ps.food["meat"])

    def test_repr(self):
        self.ps.pets = ["Sharo", "Sarah"]
        expected_res = "Shop Test_shop:\nPets: Sharo, Sarah"
        self.assertEqual(expected_res, repr(self.ps))


if __name__ == '__main__':
    main()
