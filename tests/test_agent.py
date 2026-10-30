
import unittest

from agent.core import AgentExecutor


class TestEduAlertAgent(unittest.TestCase):

    def setUp(self):
        self.agent = AgentExecutor()

    def test_agent_initialization(self):
        self.assertEqual(self.agent.name, "EduAlert AI")

    def test_student_analysis(self):
        result = self.agent.run(
            "Analyze student academic performance"
        )

        self.assertIsInstance(result, dict)
        self.assertIn("total_students", result)
        self.assertIn("high_risk", result)
        self.assertIn("medium_risk", result)
        self.assertIn("low_risk", result)

    def test_total_students(self):
        result = self.agent.run("Analyze students")

        if "error" not in result:
            self.assertGreaterEqual(result["total_students"], 0)


if __name__ == "__main__":
    unittest.main()
