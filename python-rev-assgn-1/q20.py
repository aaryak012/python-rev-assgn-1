#Q20
age_str = "23"
age = int(age_str)
is_eligible = (age >= 18) and(age < 65)
print(f"The person is {age} years old and eligible to vote (not a senior): {is_eligible}")