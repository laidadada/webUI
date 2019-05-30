import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):
        exp_value = 1
        act_value = 1
        if_exp_equql_act = exp_value == act_value
        self.assertTrue(if_exp_equql_act,
                        "exp_value=%s,act_value=%s" % (exp_value,act_value))
        print (if_exp_equql_act)

if __name__ == '__main__':
    unittest.main()
