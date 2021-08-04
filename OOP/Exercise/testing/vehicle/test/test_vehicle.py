from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(25.5, 125.5)

    def test_vehicle_init(self):
        self.assertEqual(25.5, self.car.fuel)
        self.assertEqual(25.5, self.car.capacity)
        self.assertEqual(125.5, self.car.horse_power)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_vehicle_fuel_decreases_after_driving(self):
        self.assertEqual(25.5, self.car.fuel)
        self.car.drive(10)
        self.assertEqual(13.0, self.car.fuel)

    def test_vehicle_drive_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(25)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle_fuel_increases_after_refueling(self):
        self.car.fuel = 10
        self.car.refuel(10)
        self.assertEqual(20, self.car.fuel)

    def test_vehicle_refuel_too_much_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_str_method(self):
        expected_result = "The vehicle has 125.5 horse power with 25.5 fuel left and 1.25 fuel consumption"
        actual_result = str(self.car)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
