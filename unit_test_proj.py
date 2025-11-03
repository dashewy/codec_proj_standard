import unittest
import surfshop

class chicken_joe(unittest.TestCase):

  def setUp(self):
    self.cart = surfshop.ShoppingCart()  
  
  def test_add_surfboards(self):
    add_board = self.cart.add_surfboards(1)
    self.assertEqual(add_board, 'Successfully added 1 surfboard to cart!')

    for i in range(2,4):
      add_board = self.cart.add_surfboards(i)
      with self.subTest(i):
        self.assertEqual(add_board, f'Successfully added {i} surfboards to cart!')
  def test_add_surfboards_2(self):
    add_board = self.cart.add_surfboards(2)
    self.assertEqual(add_board, 'Successfully added 2 surfboards to cart!')


  @unittest.skip("end of season sale")
  def test_TooManyBoardsError(self):
    with self.assertRaises(surfshop.TooManyBoardsError):
      self.cart.add_surfboards(5)

  def test_locals_only(self):
    discount = self.cart.apply_locals_discount()
    local = self.cart.locals_discount
    self.assertTrue(local)

  

unittest.main()