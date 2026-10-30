
import csv
import os

from config import (
    DATA_FILE,
    HIGH_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD
)


def calculate_risk(attendance, marks, assignment_completion):
    # Calculate overall academic risk score
    risk_score = (
        0.35 * (100 - attendance)
        + 0.45 * (100 - marks)
        + 0.20 * (100 - assignment_completion)
    )

    if risk_score >= HIGH_RISK_THRESHOLD:
        risk_level = "High"

    elif risk_score >= MEDIUM_RISK_THRESHOLD:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    return round(risk_score, 2), risk_level


def analyze_students():
    students = []

    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(
            f"Student data file not found: {DATA_FILE}"
        )

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            attendance = float(row["attendance"])
            marks = float(row["marks"])
            assignment_completion = float(
                row["assignment_completion"]
            )

            risk_score, risk_level = calculate_risk(
                attendance,
                marks,
                assignment_completion
            )

            students.append({
                "student_id": row["student_id"],
                "name": row["name"],
                "attendance": attendance,
                "marks": marks,
                "assignment_completion": assignment_completion,
                "risk_score": risk_score,
                "risk_level": risk_level
            })

    return students
