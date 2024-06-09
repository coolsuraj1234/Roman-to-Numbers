roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
input1 = input("please enter the Roman number").upper()
len1 = len(input1)
ans = 0
for i in range(len1):
    if i+1 < len1:
        roman_2 = roman[input1[i+1]]
    else:
        roman_2 = 0
    if roman[input1[i]] >= roman_2:
        ans = ans + roman[input1[i]]
    else:
        ans = ans - roman[input1[i]]

print(ans)
