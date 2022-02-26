num = 1
total = num
while True:
    if total > 1000:
        break
    else:
        total += num
        num += 1
print(num)