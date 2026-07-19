#Q10
is_student = True
has_discount = False
can_apply = is_student or has_discount
print(can_apply)
is_eligible = is_student and has_discount
print(is_eligible)
