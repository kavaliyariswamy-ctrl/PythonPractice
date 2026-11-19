import unittest
from inventry import Product


class TestProduct(unittest.TestCase):

    def test_product_details(self):
        product = Product(101, "Laptop", 50000, 5)

        self.assertEqual(product.product_id, 101)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 50000)
        self.assertEqual(product.quantity, 5)


if __name__ == "__main__":
    unittest.main()

