import unittest
from exercise_one import skaiciu_suma, didziausias_skaicius, sakinys_atvirksciai, ar_yra, patikrinti_sakini, lyginiai_skaiciai


class TestExerciseOne(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(skaiciu_suma(45, 5, 6), 56)
        self.assertEqual(skaiciu_suma(), 0)
        self.assertEqual(skaiciu_suma(-1, -2, -5, -10), -18)

    def test_highest_number(self):
        self.assertEqual(didziausias_skaicius(-1, -10, -100, -45), -1)
        self.assertEqual(didziausias_skaicius(1, 45, 111, 1000), 1000)
        self.assertIsInstance(didziausias_skaicius(5), int)
        self.assertIsNotNone(didziausias_skaicius("5"),
                             "value must be not None")

    def test_backward_sentence(self):
        backwards = "pridėjo? tiek plytų čia kas atėjo, pavasaris Jau"
        sentence = "Jau pavasaris atėjo, kas čia plytų tiek pridėjo?"
        self.assertEqual(sakinys_atvirksciai(sentence), backwards)
        self.assertTrue(sakinys_atvirksciai(sentence), backwards)
        self.assertIsInstance(didziausias_skaicius(sentence), str)

    def test_if_number_is_in_list(self):
        test_list = [1, 5, -10, 11]
        self.assertTrue(ar_yra(5, test_list))
        self.assertFalse(ar_yra(42, test_list))

    def test_check_sentece(self):
        sentence_check = "Žodžių kiekis: 9, Skaičių kiekis: 2, Didžiųjų raidžių: 5, Mažųjų raidžių: 34"
        sentence = "12: Jau pavasaris atėjo, kas čia plytų TIEK pridėjo?"
        self.assertEqual(patikrinti_sakini(sentence), sentence_check)
        self.assertIsInstance(patikrinti_sakini(sentence), str)
        self.assertTrue(patikrinti_sakini(sentence), sentence_check)

    def test_if_numbers_is_even(self):
        test_list_one = [2, 4, 6, 8, 10]
        test_list_two = [4, 6, 8, 10, 12, 14]
        test_list_three = [8, 12, 4, 14, 6, 10]
        self.assertTrue(lyginiai_skaiciai(2, 62))
        self.assertEqual(lyginiai_skaiciai(1, 10), test_list_one)
        self.assertEqual(lyginiai_skaiciai(3, 15), test_list_two)
        #must be in same order, assertListEqual
        self.assertListEqual(lyginiai_skaiciai(3, 15), test_list_two)
        #number order doesn't matters, assertCountEqual
        self.assertCountEqual(lyginiai_skaiciai(3, 15), test_list_three)

        
        

        
