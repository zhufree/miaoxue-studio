import math
card = 500
ticket = 15
discount = 0.9
A = 0
B = card
count = 0
while A <= math.ceil(B):
    count += 1
    A += ticket
    B += ticket*(discount**count)
print(count)