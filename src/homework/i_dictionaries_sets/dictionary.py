cities = {'Georgia': 'Atlanta', 'New York': 'Albany', 'California': 'San Diego'}

if 'FL' in cities:
    del cities['FL']  # This will raise a NameError because FL is not defined
cities['FL'] = 'Tallahassee'  # This will also raise a NameError because FL is not defined    
print(cities)
