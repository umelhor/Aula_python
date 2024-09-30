count=0
for _ in range(10):
    numbers= int(input(f"enter number:"))
    if 10<= numbers <=50:
        count +=1
        print(f"numbers between 10 and 50: {count}")