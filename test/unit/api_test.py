def test_api_divide_with_zero_divisor(self):
    response = self.client.get("/calc/divide/1/0")
    self.assertEqual(response.status_code, 400)
    self.assertIn("Division by zero", response.data.decode())

def test_api_sqrt_with_negative_number(self):
    response = self.client.get("/calc/sqrt/-1")
    self.assertEqual(response.status_code, 400)
    self.assertIn("Cannot calculate square root of a negative number", response.data.decode())

def test_api_log10_with_non_positive_number(self):
    response = self.client.get("/calc/log10/0")
    self.assertEqual(response.status_code, 400)
    self.assertIn("Logarithm base 10 is undefined for non-positive values", response.data.decode())