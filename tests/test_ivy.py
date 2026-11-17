import unittest
from src.ivy import find_cleanest_window

class TestIvy(unittest.TestCase):
    def test_no_reduction(self):
        test_forecast = {
            "prediction_1": {
                "time": "Now",
                "carbon_intensity": 420
            },
            "prediction_2": {
                "time": "+1 hour",
                "carbon_intensity": 420
            }
        }

        result = find_cleanest_window(test_forecast)
        self.assertEqual(result[0], "Now")
        self.assertEqual(result[1], 420)
        self.assertEqual(result[2], 0.00)

    def test_cleaner_future_windows(self):
        test_forecast = {
            "prediction_1": {
                "time": "Now",
                "carbon_intensity": 400
            },
            "prediction_2": {
                "time": "+1 hour",
                "carbon_intensity": 300
            },
            "prediction_3": {
                "time": "+2 hours",
                "carbon_intensity": 200
            }
        }

        result = find_cleanest_window(test_forecast)
        self.assertEqual(result[0], "+2 hours")
        self.assertEqual(result[1], 200)
        self.assertEqual(result[2], 50.0)

    def test_zero_carbon_intensity(self):
        test_forecast = {
            "prediction_1": {
                "time": "Now",
                "carbon_intensity": 0
            },
            "prediction_2": {
                "time": "+1 hour",
                "carbon_intensity": 100
            }
        }

        result = find_cleanest_window(test_forecast)
        self.assertEqual(result[0], "Now")
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 0.0)