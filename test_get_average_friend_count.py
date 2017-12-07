import unittest

import network_functions

class TestGetAverageFriendCount(unittest.TestCase):

    def test_get_average_empty(self):
        param = {}
        actual = network_functions.get_average_friend_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_get_average_one_person_one_friend(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_average_friend_count_with_empty_graph(self):
        person_to_friends = {}
        
        count = get_average_friend_count(person_to_friends)
        
        self.assertEqual(count, 0.0)

    def test_get_average_friend_count_with_person_not_in_key (self):
        person_to_friends = {

            'a': ['a','b','c'],
            'b':['c'],
            'c':['a']

            
        }
    
        count = get_average_friend_count(person_to_friends)
        self.assertAlmostEqual(count, 3.0)
        
    def test_get_average_friend_count(self):
        person_to_friends = {
            'a': ['a','b','c'],
            'b':['c'],
            'c': ['a','b']

        }

        count = get_average_friend_count(person_to_friends)
        self.assertEqual(count, 2.0)
            
    def test_get_average_friend_count_return_float_value(self):

        person_to_friends ={
            'a':['a','b','c'],
            'b':['c'],
            'c':['a']
        
            

        }
        
        count = get_average_friend_count(person_to_friends)
        self.assertAlmostEqual(count, 1.667, delta=0.001)

if __name__ == '__main__':
    unittest.main()
