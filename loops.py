
#Basic Loop

for i in range(1, 11):
    print('Current value:', i)

#2
fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)


#3 - Using "Items" for Key and values 
teams = {
     "Colorado": "Rockies",
    "Chicago": "White Sox",
     "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
    }

for City, i in teams.items():
    print(City, ">>", i)


#4
numbers = [1, 2, 3, 4, 5, 6, -1, -4]

for i in numbers:
    if i % 2 != 0:
        continue
    print( i, "Even Number")

#Basic While loop
counter = 1
while counter <= 10:
    print("Current Value", counter)
    counter = counter + 1

#Practice 
Ticket = 100
while Ticket > 0:
    print( Ticket, "Tickets Availble")
    Ticket = Ticket - 1
print("Booking Full")



#nested
line_to_print = ''
for i in range (1, 10):
    for j in range (0, 12):
        line_to_print += str(i)
    print(line_to_print)
    line_to_print = ''   

#looping over list

countries = ['Thailand', 'Vietnam', 'Malaysia', 'UAE']

for i in countries:
    print(f" {i} contains {len(i)} letters!")

#Looping with a List of Tuples

new_hires = [('Mark Adams', 'SQL Analyst', 4000),
             ('Leslie Burton', 'HR Specialist', 2300),
             ('Dorothy Castillo', 'UX Designer', 3100)]

def remove_sql_specialists(people_list):
    filtered_list = []
    for person in people_list:
        name, job_title, salary = person
        if "SQL" not in job_title:
            filtered_list.append(person)
    return filtered_list

cleaned_list = remove_sql_specialists(new_hires)
print(cleaned_list)

        
#