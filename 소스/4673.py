# 셀프넘버

numbers = list(range(1,10001))
remove_list = []

for number in numbers:
    for n in str(number):
        number += int(n)
    if number <= 10000:
        remove_list.append(number)

for remove_num in set(remove_list):  # set으로 중복값 제거
    numbers.remove(remove_num)

for self_num in numbers:
    print(self_num)