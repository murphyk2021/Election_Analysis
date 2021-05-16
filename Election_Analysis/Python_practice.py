print("Hello World")
counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])
    
counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
        print("Arapahoe or El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe is in th list of counties and El Paso is not in the list of counties")

#Iterate through lists and tuples    
for county in counties:
    print(county)

numbers=[0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

#Get the keys of a dictionary
counties_dict={"Arapahoe":422829, "Denver": 463353, "Jefferson":432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#Get the Key-Value Pairs of a dictionary
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#Iterate through a list of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters":463353},{"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[0])

#Get the values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
            print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])
    print(county_dict['county'])

for county_dict in voting_data:
        print(county_dict['county'])   

for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')

for county_dict in voting_data:
        print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")  

for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']:,} registered voters.")  