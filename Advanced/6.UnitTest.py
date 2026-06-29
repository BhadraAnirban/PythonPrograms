import unittest

from SampleClass import MyClass1, MyClass2

class TestMyClass1(unittest.TestCase): 

    def testAdd(self): 
        my_class_obj = MyClass1()
        self.assertEqual(my_class_obj.add(2,2), 4)
        self.assertEqual(my_class_obj.add(3.0, 6.0), 9.0)
        self.assertEqual(my_class_obj.add(-3, -3), -6)
        self.assertNotEqual(my_class_obj.add(-3, -3), -9)

class TestMyClass2(unittest.TestCase): 

    def testMulti(self): 
        my_class_obj = MyClass2()
        self.assertEqual(my_class_obj.multi(2,2), 4)
        self.assertEqual(my_class_obj.multi(3.0, 6.0), 18.0)
        self.assertEqual(my_class_obj.multi(-3, -4), 12)
        self.assertNotEqual(my_class_obj.multi(-3, -3), -9)
        
unittest.main()