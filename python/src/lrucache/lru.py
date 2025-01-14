class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.cache = []
		self.lru = {}

	def refer(self, key):
		# not present in cache
		if key not in self.lru:
			if len(self.cache) >= self.capacity:
				last_key = self.cache.pop()
				del self.lru[last_key]
		# present in cache
		else:
			self.cache.remove(key)

		# update reference
		self.cache.insert(0, key)
		self.lru[key] = 0

	def display(self):
		for i in self.cache:
			print(i,end=' ')
		print('')
