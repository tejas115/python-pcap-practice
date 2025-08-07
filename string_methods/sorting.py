d1 = 50
d2 = '5.0'
# s1 = '10 20 30 40'.sort()
s1 = sorted('10 20 30 40')

digit_sum = d1 + float(d2) + int(s1[-1])  # expected outcome 59.0
string_sum = str(d1) + d2 + s1[-1] # expected outcome '505.04'

print(digit_sum)
print(string_sum)