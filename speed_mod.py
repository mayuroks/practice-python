single = ['','one','two','three','four','five','six','seven','eight','nine']
double = ['','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
hund = ['','hundred']

number = 2

lent = 0

num = str(number)
number = list(num)

print(num)

number = [int(i) for i in number]
lent = len(number)

ans = ""
if lent == 3:
  single[number[0]],hund[1],double[number[0] + 1],single[number[2]])
elif lent == 2:
  print(double[number[0] - 1],single[number[1]])
else:
  print(single[number[0]])
