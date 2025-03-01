principle =0
rate =0
time=0

while True:
    principle=float(input("Enter your principle:"))
    if principle<0:
        print("Principle can't be less that or equal to zero ")
    else:
        break
while True:
    rate=float(input("Enter your interest:"))
    if rate<0:
        print("Interest rate  can't be less that or equal to zero ")
    else:
        break

while time <=0:
    time=float(input("Enter your interest:"))
    if time<0:
        print("Interest rate  can't be less that or equal to zero ")
    else:
        break

total=principle * pow((1+rate/100,time))
print(f"Balance after {time} year/s: ${total:2f}")
