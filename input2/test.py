import unittest
import year


class VYearTest(unittest.TestCase):

    def test_ask_for_year(self):

        r1 = year.ask_for_year('a123')
        r2 = year.ask_for_year('112')
        r3 = year.ask_for_year('12345')
        r4 = year.ask_for_year('22')
        r5 = year.ask_for_year('1995')
        r6 = year.ask_for_year('')
        r7 = year.ask_for_year(None)
        
        self.assertEqual(r1, 'a123')
        self.assertEqual(r2, None)
        self.assertEqual(r3, None)
        self.assertEqual(r4, "22")
        self.assertEqual(r5, "1995")
        self.assertEqual(r6, None)
        self.assertEqual(r7, None)
        
    def test_verify_only_number(self):

        s1 = year.verify_only_number('azer')
        s2 = year.verify_only_number('12a')
        s3 = year.verify_only_number('2134')
        s4 = year.verify_only_number('')
        s5 = year.verify_only_number(None)

        self.assertEqual(s1, False)
        self.assertEqual(s2, False)
        self.assertEqual(s3, True)
        self.assertEqual(s4, False)
        self.assertEqual(s5, False)

    # def test_days_passed(my_year):


if __name__ == '__main__':
    unittest.main()
