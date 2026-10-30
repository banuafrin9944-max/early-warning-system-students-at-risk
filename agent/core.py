
from tools.data_query import analyze_students


class AgentExecutor:
    def __init__(self):
        self.name = "EduAlert AI"

    def run(self, query):
        """
        Analyze student performance and identify
        students who may be at academic risk.
        """

        try:
            students = analyze_students()

            if not students:
                return "No student records found."

            high_risk = []
            medium_risk = []
            low_risk = []

            for student in students:
                risk = student["risk_level"]

                if risk == "High":
                    high_risk.append(student)

                elif risk == "Medium":
                    medium_risk.append(student)

                else:
                    low_risk.append(student)

            result = {
                "total_students": len(students),
                "high_risk": high_risk,
                "medium_risk": medium_risk,
                "low_risk": low_risk
            }

            return result

        except Exception as error:
            return {
                "error": str(error)
            }

