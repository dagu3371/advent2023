import re
with open('input.txt', 'r') as file:
    lines = file.readlines()
sum = 0
digits = {'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}
regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
def convert_to_int(s):
    if s.isdigit():
        res = s
    else:
        res = digits[s]
    return res
for line in lines:
    dd = re.findall(regex, line)
    first = convert_to_int(dd[0])
    last = convert_to_int(dd[-1])
    sum += int(first + last)
print(sum)