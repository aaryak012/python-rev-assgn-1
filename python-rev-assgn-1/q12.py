#Q12
score = 85
attendance = 0.92
behavior = True

passes = (score >= 80) and (attendance >= 0.9)

if passes:
    print(f"The student passes. Score: {score}, Attendance: {attendance}, Behavior: {behavior}")
else:
    print(f"The student does not pass. Score: {score}, Attendance: {attendance}, Behavior: {behavior}")