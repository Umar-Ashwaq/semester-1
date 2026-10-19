def interger_values_between_0_and_value_given(a):
    for i in range(a):
        if i % 2 == 0:
            print(i)
        continue
    return i
value = interger_values_between_0_and_value_given(15)
print(value)