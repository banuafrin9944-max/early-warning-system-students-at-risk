def calculate_risk(attendance, marks, assignments):

    risk = (
        0.35 * (100 - attendance) +
        0.45 * (100 - marks) +
        0.20 * (100 - assignments)
    )

    if risk >= 60:
        level = "High"
    elif risk >= 35:
        level = "Medium"
    else:
        level = "Low"

    return round(risk, 2), level
