from unittest import TestCase, main
from primenumbers import get_page

# class TestPageMethods(TestCase):

#     def setUp(self):
#         print("setUp code")
#         print("self\n")
#         print(self)
#         # self.page = get_page()
    
#     # def test_get_page(self):
#     #     print("test_get_page")
#     #     self.assertEqual(1, 1, "One equal one")

class TestSanityTest(TestCase):
    def setUp(self):
        print("setup self\n")
        print(self)
    def test_basic(self):
        self.assertEqual(1, 2, "one does not equal 2")

if __name__ == '__main__':
    main()
