# Create a new Python file in this folder called hash.py
# Create a dictionary called countryMap, where the the KEYS are the name of a country (i.e. a String), and the VALUE for each key is the name of that country's
# capital city.
# For Example:
#    countryMap = {
#        'UnitedKingdom': 'London',
#        'Sweden': 'Stockholm',
#        'Canada': 'Ottawa',
#    }
#    What does print countryMap['Sweden'] return?

country_map = {"united_kingdom" : "london", "sweden" : "stockholm", "canada" : "ottawa", "south_africa" : "johannesburg", "russia" : "moscow", "america" : "washington"}
for country in country_map.keys():
    print(country_map.keys())
    country = input("Enter a country's name: \n")
    print(country_map[country])
