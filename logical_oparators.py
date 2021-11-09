# and
# or
# not

high_income = True
good_credit = False
# good_credit = True
student = False  # True

# if high_income or good_credit:
# if high_income and good_credit:
# if high_income and good_credit:
# if not student:
if (high_income or good_credit) and not student:
    print('Eligible')
else:
    print("Not eligible")

# short circuit evaluation
if high_income and good_credit and not student:
    print('Eligible')
