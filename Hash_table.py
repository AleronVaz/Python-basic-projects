class HashTable:
    def __init__(self):
        # The main storage
        self.collection = {}

    def hash(self, line):
        # Sum the Unicode values of the string
        return sum(ord(char) for char in line)

    def add(self, key, value):
        h = self.hash(key)
        
        # If the hash index doesn't exist yet, create a nested dictionary
        if h not in self.collection:
            self.collection[h] = {}
        
        # Store the key-value pair inside that nested dictionary
        self.collection[h][key] = value

    def lookup(self, key):
        h = self.hash(key)
        
        # Check if the hash exists and if the specific key is inside it
        if h in self.collection and key in self.collection[h]:
            return self.collection[h][key]
        return None

    def remove(self, key):
        h = self.hash(key)
        
        # Only attempt to delete if the hash and the specific key exist
        if h in self.collection and key in self.collection[h]:
            del self.collection[h][key]
            
            # Optional: If the nested dictionary is now empty, 
            # you could remove the hash index entirely:
            if not self.collection[h]:
                del self.collection[h]


