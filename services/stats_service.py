import os
import requests

SPRING_BOOT_URL = os.getenv(
    "SPRING_BOOT_URL",
    "https://onlineexamsystem2026.onrender.com/api/results/registration"
)


def get_data(reg_no):

    try:

        url = f"{SPRING_BOOT_URL}/{reg_no}"

        print(f"Fetching: {url}")

        response = requests.get(
            url,
            timeout=10
        )

        print("Status:", response.status_code)

        if response.status_code != 200:
            print("Response:", response.text)
            return []

        data = response.json()

        print("Data:", data)

        return data

    except Exception as e:

        print("Analytics Error:", str(e))

        return []


def get_pass_fail(reg_no):

    data = get_data(reg_no)

    if not data:

        return {
            "pass": 0,
            "fail": 0,
            "total": 0
        }

    pass_count = len(
        [
            item for item in data
            if item.get("marks", 0) >= 40
        ]
    )

    fail_count = len(data) - pass_count

    return {
        "pass": pass_count,
        "fail": fail_count,
        "total": len(data)
    }


def get_marks(reg_no):

    data = get_data(reg_no)

    if not data:
        return []

    return [
        {
            "subject": item.get("subject"),
            "marks": item.get("marks", 0)
        }
        for item in data
    ]


def get_dashboard(reg_no):

    data = get_data(reg_no)

    if not data:

        return {
            "registrationNo": reg_no,
            "totalMarks": 0,
            "averageMarks": 0,
            "percentage": 0,
            "highestMarks": 0,
            "lowestMarks": 0,
            "pass": 0,
            "fail": 0,
            "grade": "N/A",
            "chartData": []
        }

    marks = [
        item.get("marks", 0)
        for item in data
    ]

    total_marks = sum(marks)

    average_marks = round(
        total_marks / len(marks),
        2
    )

    percentage = round(
        total_marks / (len(marks) * 100) * 100,
        2
    )

    highest_marks = max(marks)

    lowest_marks = min(marks)

    pass_count = len(
        [
            mark for mark in marks
            if mark >= 40
        ]
    )

    fail_count = len(marks) - pass_count

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return {

        "registrationNo": reg_no,

        "totalMarks": total_marks,

        "averageMarks": average_marks,

        "percentage": percentage,

        "highestMarks": highest_marks,

        "lowestMarks": lowest_marks,

        "pass": pass_count,

        "fail": fail_count,

        "grade": grade,

        "chartData": [
            {
                "subject": item.get("subject"),
                "marks": item.get("marks", 0)
            }
            for item in data
        ]
    }