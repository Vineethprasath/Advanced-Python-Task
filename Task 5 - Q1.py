#People list with combination of both above and below 18
people = [
    {"name": "Kavin Prabhu N", "age": 25},
    {"name": "Sampath G", "age": 17},
    {"name": "Sinoj V", "age": 18},
    {"name": "Dhinesh S", "age": 28},
    {"name": "Rokesh", "age": 15},
    {"name": "Suresh", "age": 21},
    {"name": "Satheesh", "age": 19},
    {"name": "Vikash", "age": 12},
    {"name": "Yazhan", "age": 2}
]

#Removal of people who is under 18 and map the people whose age is equal to or more than 18
only_adults = filter(lambda person: person["age"] >= 18, people)
adult_names = list(map(lambda person: person["name"], only_adults))

#Print the list of only adults
print("Only Adults:",adult_names)