ages_men = []
ages_women = []
total_ages = 0

for _ in range(10):
    age = int(input("Enter the age: "))
    gender = input("Enter the gender (M/F): ").upper()
    total_ages += age
    if gender == 'M' 'm':
        ages_men.append(age)
    elif gender == 'F' 'f':
        ages_women.append(age)

average_women = sum(ages_women) / len(ages_women) if ages_women else 0
average_men = sum(ages_men) / len(ages_men) if ages_men else 0
average_group = total_ages / 10

print(f"Average age of women: {average_women}")
print(f"Average age of men: {average_men}")
print(f"Average age of the group: {average_group}")