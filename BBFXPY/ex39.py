#-*-conding:Utf-8 -*-

# create a mapping of state to abbreviation
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New york' :'NY',
    'Michigan':'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' :'Jacksonville'
}

#Add some more cities
cities['NY'] = 'New York'
cities["OR"] = 'Portland'

#print out some cities
print("-"*15)
print("NY state has:",cities['NY'])
print("OR state has:",cities["OR"])

#print some states
print("-" * 15)
print("Michign's abbreviation is:",states['Michigan'])
print("Florida's abbreviation is:",states['Florida'])

#do it by using the state then cities dict
print("-" * 15)
print("Michigan has :",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

#print every state abbreviation

print('*'* 20)
for state,abbrev in states.items():
    print("%s is abbreviation %s" % (state,abbrev))

#print every city in state
print('*' * 20)
for abbrev,city in cities.items():
    print("%s has the city %s" % (abbrev,city))

#now do both at the same time

print("*" * 20)
for state,abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state,abbrev,cities[abbrev]))

print("*" * 20)
# safely get a abbreviationg by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry,no texas")

#get a city with a default value

city =cities.get('TX','Does not exist')
print("The city for the state 'TX' is: %s" % city)