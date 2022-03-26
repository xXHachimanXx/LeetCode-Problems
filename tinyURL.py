import random
import string

# docs: https://docs.google.com/document/d/1ZMWy7fINMc3VMzDk-uJOnH4uG6V1q-XdnEITk6CxYg4/edit
class Solution:
	def __init__(self):
		self.hash_table = {}

	def create_key(self, length):
		key = ''
		while True:
			for _ in range(length):
				key += random.choice(string.ascii_letters)
			if key in self.hash_table:
				key = ''
				continue
			else:
				break
		return key

	def encode(self, longUrl):
		key = self.create_key(6)
		self.hash_table[str(key)] = longUrl
		return 'http://tinyurl.com/' + key
		

	def decode(self, shortUrl):
		key = shortUrl[19:]
		return self.hash_table[str(key)]