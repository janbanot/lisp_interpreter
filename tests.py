import unittest
from interpreter import lisp_eval, parse


class EvalTests(unittest.TestCase):

    def test_addition(self):
        test_procedure = "(+ 10 9)"
        self.assertEqual(19, lisp_eval(parse(test_procedure)))

    def test_subtraction(self):
        test_procedure = "(- 10 9)"
        self.assertEqual(1, lisp_eval(parse(test_procedure)))

    def test_multiplication(self):
        test_procedure = "(* 10 9)"
        self.assertEqual(90, lisp_eval(parse(test_procedure)))

    def test_division(self):
        test_procedure = "(/ 90 9)"
        self.assertEqual(10, lisp_eval(parse(test_procedure)))

    def test_equality(self):
        test_procedure = "(eq 90 9)"
        self.assertFalse(lisp_eval(parse(test_procedure)))

    def test_lists(self):
        test_procedure = "(define box (cons 3 4))"
        lisp_eval(parse(test_procedure))
        test_procedure_cons = "box"
        test_procedure_car = "(car box)"
        test_procedure_cdr = "(cdr box)"
        self.assertEqual([3, 4], lisp_eval(test_procedure_cons))
        self.assertEqual(3, lisp_eval(parse(test_procedure_car)))
        self.assertEqual(4, lisp_eval(parse(test_procedure_cdr)))

    def test_conditions_1(self):
        test_procedure = "(if (< 2 4) 1 2)"
        self.assertEqual(1, lisp_eval(parse(test_procedure)))

    def test_conditions_2(self):
        test_procedure = "(if (> 2 4) 1 2)"
        self.assertEqual(2, lisp_eval(parse(test_procedure)))

if __name__ == '__main__':
    unittest.main()