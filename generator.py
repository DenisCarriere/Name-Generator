import csv
import random
import string
from datetime import date


class Names(object):
	dictionary_folder = 'Dictionary/'
	female_first_name = []
	male_first_name = []
	last_name = []
	location = []


	def __init__(self):
		self.load_female_first_name()
		self.load_male_first_name()
		self.load_last_name()
		self.load_location()

	def load_female_first_name(self):
		f = open(self.dictionary_folder + 'dist.female.first')
		for line in f.readlines():
			name = line.split(' ')[0]
			if name:
				self.female_first_name.append(name)
		print 'Female Names:', len(self.female_first_name)

	def load_male_first_name(self):
		f = open(self.dictionary_folder + 'dist.male.first')
		for line in f.readlines():
			name = line.split(' ')[0]
			if name:
				self.male_first_name.append(name)
		print 'Male Names:', len(self.male_first_name)

	def load_last_name(self):
		f = open(self.dictionary_folder + 'dist.all.last')
		for line in f.readlines():
			name = line.split(' ')[0]
			if name:
				self.last_name.append(name)
		print 'Last Names:', len(self.last_name)

	def load_location(self):
		f = open(self.dictionary_folder + 'Canadian_Locations.txt')
		reader = csv.DictReader(f,fieldnames=['City','Province','Population'], dialect='excel-tab')
		for line in reader:
			name = '{0}, {1}'.format(line.get('City'), line.get('Province'))
			self.location.append(name)
		print 'Locations:', len(self.location)


class Person(object):
	def __init__(self, names):
		# Load Names
		self.names = names

		# Get Information
		self.sexe = self.get_sexe()
		self.first_name = self.get_first_name()
		self.last_name = self.get_last_name()
		self.initial = self.get_initial()

		self.service_number = self.get_service_number()
		self.passport_number = self.get_passport_number()
		self.place_of_birth = self.get_place_of_birth()
		self.date_of_birth = self.get_date_of_birth()


	def get_sexe(self):
		return random.choice(['male','female'])


	def get_first_name(self):
		if self.sexe == 'male':
			return random.choice(self.names.male_first_name).title()

		elif self.sexe == 'female':
			return random.choice(self.names.female_first_name).title()


	def get_last_name(self):
		return random.choice(self.names.last_name).title()


	def get_initial(self):
		initial = ''
		length = random.choice([1,1,1,1,1,1,1,2,2,2,2,3])
		for i in xrange(length):
			initial += random.choice(self.names.female_first_name)[0]
		return initial


	def get_service_number(self):
		# Format = A01 234 567
		letter = random.choice(string.ascii_lowercase).upper()
		Num1 = random.randint(0,9)
		Num2 = random.randint(0,9)
		Num3 = random.randint(0,9)
		Num4 = random.randint(0,9)
		Num5 = random.randint(0,9)
		Num6 = random.randint(0,9)
		Num7 = random.randint(0,9)
		Num8 = random.randint(0,9)

		return '{0}{1}{2} {3}{4}{5} {6}{7}{8}'.format(letter, Num1, Num2, Num3, Num4, Num5, Num6, Num7, Num8)


	def get_passport_number(self):
		# Format = AA012345
		letter1 = random.choice(string.ascii_lowercase).upper()
		letter2 = random.choice(string.ascii_lowercase).upper()
		Num1 = random.randint(0,9)
		Num2 = random.randint(0,9)
		Num3 = random.randint(0,9)
		Num4 = random.randint(0,9)
		Num5 = random.randint(0,9)
		Num6 = random.randint(0,9)

		return '{0}{1}{2}{3}{4}{5}{6}{7}'.format(letter1, letter2, Num1, Num2, Num3, Num4, Num5, Num6)
		
	def get_place_of_birth(self):
		return random.choice(self.names.location)

	def get_date_of_birth(self):
		min_age = 25
		max_age = 55
		start_date = date.today().replace(year=2013 - max_age).toordinal()
		end_date = date.today().replace(year=2013 - min_age).toordinal()
		birthday = date.fromordinal(random.randint(start_date, end_date))
		year = birthday.year
		month = birthday.month
		day = birthday.day

		return '{0}/{1}/{2}'.format(year, month, day)

	def row(self):
		return {
			'first_name': self.first_name,
			'last_name': self.last_name,
			'initial': self.initial,
			'sexe': self.sexe,
			'passport_number': self.passport_number,
			'service_number': self.service_number,
			'place_of_birth': self.place_of_birth,
			'date_of_birth': self.date_of_birth}

	def __repr__(self):
		return '{0} {1} {2} {3}'.format(
			self.first_name, 
			self.initial, 
			self.last_name,
			self.place_of_birth)

def generate_names(total):
	name = 'Name_Generator_{0}.csv'.format(total)
	fieldnames = ['first_name', 'last_name', 'initial', 'sexe', 'passport_number', 'service_number', 'place_of_birth', 'date_of_birth']
	f = open(name, 'wb')
	writer = csv.DictWriter(f, fieldnames=fieldnames, dialect='excel')
	writer.writeheader()
	names = Names()

	for i in xrange(total):
		person = Person(names=names)
		writer.writerow(person.row())

	f.close()


if __name__ == '__main__':
	#names = Names()
	#person = Person(names=names)
	#print person


	generate_names(700)