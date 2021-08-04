from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("test", 10, 100, 20)
        self.enemy_hero = Hero("test2", 5, 100, 10)

    def test_hero_init(self):
        self.assertEqual("test", self.hero.username)
        self.assertEqual("test2", self.enemy_hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(5, self.enemy_hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.enemy_hero.health)
        self.assertEqual(20, self.hero.damage)
        self.assertEqual(10, self.enemy_hero.damage)

    def test_battle_with_same_name(self):
        self.enemy_hero.username = "test"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_takes_damage_after_fighting(self):
        self.assertEqual(100, self.hero.health)
        self.hero.battle(self.enemy_hero)
        self.assertEqual(55, self.hero.health)

    def test_battle_end_draw(self):
        self.hero.damage = 10
        self.enemy_hero.damage = 20
        expected_result = "Draw"
        actual_result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_result, actual_result)

    def test_hero_wins_battle(self):
        self.hero.damage = 10
        expected_result = "You win"
        actual_result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_hero_loses_battle(self):
        self.hero.damage = 5
        expected_result = "You lose"
        actual_result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(6, self.enemy_hero.level)
        self.assertEqual(55, self.enemy_hero.health)
        self.assertEqual(15, self.enemy_hero.damage)

    def test_hero_str_method(self):
        expected_result = "Hero test: 10 lvl\n" \
                          "Health: 100\n" \
                          "Damage: 20\n"
        actual_result = str(self.hero)
        self.assertEqual(expected_result, actual_result)

    def test_hero_fights_with_negative_health_raises(self):
        self.hero.health = -5
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero_fight_enemy_with_negative_health_raises(self):
        self.enemy_hero.health = -5
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight test2. He needs to rest", str(ex.exception))


if __name__ == "__main__":
    main()
