import unittest
from dictionary import CustomDict
from cost import CostDict
from order import WordForm

class TestCustomDict(unittest.TestCase):
    def test_newentry(self):
        d = CustomDict()
        d.newentry('Apple', 'A fruit')
        self.assertEqual(d.looks('Apple'), 'A fruit')

    def test_look_entry_not_found(self):
        d = CustomDict()
        d.newentry('Apple', 'A fruit')
        self.assertEqual(d.looks('Banana'), "can't find entry for 'Banana'")

class TestCostDict(unittest.TestCase):
    def test_get_total(self):
        cost_dict = CostDict()
        total = cost_dict.get_total(['socks', 'shoes'], 0.09)
        self.assertEqual(total, 72.09) 

class TestWordForm(unittest.TestCase):
    def test_form_word(self):
        word_former = WordForm(['yoda', 'best', 'has'])
        formed_word = word_former.form_word()
        self.assertEqual(formed_word, 'yes')  

if __name__ == '__main__':
    unittest.main()
