import requests

SPRING_BOOT_URL = "http://localhost:8080/api/results"

def get_data(reg_no):
    try:
        response = requests.get(
            f"{SPRING_BOOT_URL}/{reg_no}",
            timeout=5
        )

        # 🔥 IMPORTANT: check status
        if response.status_code != 200:
            print("ERROR STATUS:", response.status_code)
            return []

        data = response.json()

        # 🔥 DEBUG
        print("SPRING RESPONSE:", data)

        return data

    except Exception as e:
        print("REQUEST ERROR:", e)
        return []


def get_pass_fail(reg_no):
    data = get_data(reg_no)

    if not data:
        return {"pass": 0, "fail": 0, "total": 0}

    pass_count = len([r for r in data if r.get("marks", 0) >= 40])
    fail_count = len(data) - pass_count

    return {
        "pass": pass_count,
        "fail": fail_count,
        "total": len(data)
    }


def get_marks(reg_no):
    data = get_data(reg_no)

    return [
        {
            "name": r.get("subject", "Exam"),
            "marks": r.get("marks", 0)
        }
        for r in data
    ]