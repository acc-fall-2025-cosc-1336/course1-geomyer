import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def setUp(self):
        self.widgets = {}

    def test_add_inventory(self):
        add_inventory(self.widgets, 'Widget1', 10)
        self.assertIn('Widget1', self.widgets)
        self.assertEqual(self.widgets['Widget1'], 10)
#Test case test_remove_inventory_widget
#Write a test case add two widgets(widget1 and widget2 with quantities of your choice).
#Remove widget1. Test that the length of dictionary is 1 and that widget2 still exists. 

def test_remove_inventory_widget(self):
        add_inventory(self.widgets, 'Widget1', 10)
        add_inventory(self.widgets, 'Widget2', 20)
        remove_inventory_widget(self.widgets, 'Widget1', 10)
        self.assertNotIn('Widget1', self.widgets)
        self.assertIn('Widget2', self.widgets)
        self.assertEqual(len(self.widgets), 1)
        