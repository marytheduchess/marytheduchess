#page 115 make several dictionaries 
users = {	
	'Pet1': {
		'Owner': 'mary',
		'Breed': 'dog',
		'Name': 'kobe',
		},
		
		'Pet2': {
			'Owner': 'jessica',
			'Breed': 'ball python',
			'Name': 'peety',
			},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	owner = user_info['Owner']
	breed = user_info['Breed']
	name = user_info['Name']
	
	
print("\tOwner: " + owner.title())
print("\tBreed: " + breed.title())
print("\tName: " + name.title())

#page 112 practice again
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())


#pg 115 practice 6-9 favorite places
favorite_places = {
	'Mary': ['Vancouver', 'St. Tropez'],
	'Onyongo': ['New York', 'France'],
	'Lea': ['Owatonna', 'Dreamland'],
	}
for name, places in favorite_places.items():
	print("\n" + name.title() + "'s favorite places are:")
	for places in places:
		print("\t" + places.title())
	
