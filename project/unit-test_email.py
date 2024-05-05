import unittest
import myform

class MyFormTest(unittest.TestCase): # Класс юнит тестов
    # Массив с корректными адресами
    correct_tests_list = ["g1fka@gmail.com",
                          "g1fka213TV@gmail.com",
                          "g1fka@mail.com.ru.org",
                          "g1f@mail.com",
                          "g1f.net@mail.org",
                          "g1fkAAAAAAAAAAAAAAAA@mail.com"]

    # Массив с некорректными адресами
    uncorrect_tests_list = ["@gmail.com",
                            "12@gmail.com",
                            "mail.org",
                            "gf@.com",
                            "@.com",
                            "",
                            " ",
                            "mail",
                            "g1fka42@gmail.incorparated",
                            "g1fka42@m.inc",
                            "g1fka42!!!@m.inc",
                            "g1fka 42@mail.inc",
                            "@",
                            ".org"]

    def test_check_uncor(self): # Проверка некорректных адресов
        for mail in self.uncorrect_tests_list:
            self.assertFalse(myform.check(mail))

    def test_check_cor(self): # Проверка корректных адресов
        for mail in self.correct_tests_list:
            self.assertTrue(myform.check(mail))