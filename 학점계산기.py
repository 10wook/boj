def grade_to_score(grade: str) -> float:
    base_map = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    if grade[0] == "F":  # F는 0.0
        return 0.0
    base = base_map[grade[0]]
    if grade[1] == "+":
        return base + 0.5
    elif grade[1] == "0":
        return base + 0.3
    elif grade[1] == "-":
        return base + 0.0
    else:
        return base

def calculate_gpa(entries):
    total_score, total_credit = 0.0, 0.0
    for credit, grade in entries:
        score = grade_to_score(grade)
        total_score += credit * score
        total_credit += credit
    return total_score / total_credit if total_credit > 0 else 0.0

if __name__ == "__main__":
    entries = []
    print("학점과 등급을 입력하세요 (예: 3.0 A0). 종료하려면 '끝' 입력.")
    while True:
        line = input("> ").strip()
        if line == "끝":
            break
        try:
            credit, grade = line.split()
            entries.append((float(credit), grade))
        except:
            print("입력 형식이 잘못되었습니다. 예: 3.0 A0")
    gpa = calculate_gpa(entries)
    print(f"평균 학점 (GPA): {gpa:.2f}")
