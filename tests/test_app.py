import unittest, time
from src.app import app


class TestHealthAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_status(self):
        start_time = time.time()
        response = self.app.get("/health")
        end_time = time.time()
        duration = end_time - start_time
        print("Time response:", duration)
        self.assertLess(duration, 2, "Bad latency!")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "UP")


if __name__ == "__main__":
    unittest.main()
