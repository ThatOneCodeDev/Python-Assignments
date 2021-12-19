airport_codes = {
    'Washington': 'IAD',
    'San Francisco': 'SFO',
    'Chicago': 'ORD',
    'London': 'LHR',
    'Amsterdam': 'AMS'
}

new_airport_codes = {
    'London': 'LCY',
    'Vancouver': 'YVR',
    'Los Angeles': 'LAX'
}

print(airport_codes.get('Los Angeles', 'na'))
print(airport_codes.get('London', 'na'))
airport_codes.update(new_airport_codes)
print(airport_codes.get('Los Angeles', 'na'))
print(airport_codes.get('London', 'na'))