import hashlib
class HashTable:
    
    def __init__(self, size: int = 8):
        """Initialise the hash table."""
        self.size: int = size
        self.table: list[list[tuple[str, str | int]]] = [[] for _ in range(self.size)]
        self.item_count: int = 0
        self.load_factor_threshold: float = .8
    def __str__(self):
        return f"HashTable: {self.table}"
    def _hash(self, key:str, base:int=31)->int:
        """A Simple hash function"""
        hash_val=0
        for char in key:
            hash_val = (hash_val * base + ord(char)) % self.size
        return hash_val

    def _resize(self) -> None:
        """Resize the hash table to double its current size"""
        table_copy= self.table
        self.size*=2
        self.item_count=0
        self.table=[[] for _ in range(self.size)]
        for bucket in table_copy:
            for key, value in bucket:
                self.insert(key, value)
#    def insert(self, key, value):
#        """Insert or update a key-value pair."""
#
#        index = self._hash(key)
#        bucket = self.table[index]
#
#        if len(bucket)>0:
#            self.table[index]= [key,value] # type: ignore
#            return
#        bucket.append((key, value))
#        self.item_count+=1
#        load_factor=self.item_count/self.size
#        print(load_factor>=self.load_factor_threshold)
#        if load_factor>= self.load_factor_threshold:
#            self._resize()
    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
    
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Add new key if not found
        self.item_count+=1
        load_factor=self.item_count/self.size
        print(load_factor>=self.load_factor_threshold)
        if load_factor>= self.load_factor_threshold:
            self._resize()

    def get(self, key):
        """Retrieve a value by its key. Return None if the key is not found."""
        index = self._hash(key)
        
        if self.table[index]:
            for item in self.table:
                if item[0]==key:
                    return self.table[index][0][1]
        else:
            return None

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        if self.get(key):
            pass
    def display(self):
        pass

if __name__=="__main__":
    ht = HashTable(size=4) # Start with a small size to demonstrate resizing

    print(ht)


    print("\n>>> Inserting initial items...")

    ht.insert("name", "Alice")

    ht.insert("age", 30)

    ht.insert("city", "London")

    print(ht)


    print("\n>>> Inserting more items...")

    ht.insert("country", "UK") # This will trigger a resize (0.8)

    ht.insert("mane", "A lion's hair") # Possible collision with 'name'

    ht.insert("anime", "Akira") # Another collision

    print(ht)


    print("\n>>> Getting values...")

    print(f"Name: {ht.get('name')}")

    print(f"City: {ht.get('city')}")

    print(f"Job: {ht.get('job')}") # Should be None


    print("\n>>> Updating a value...")

    ht.insert("name", "Bob")

    print(f"Updated Name: {ht.get('name')}")

    print(ht)


    print("\n>>> Deleting a value...")

    #deleted = ht.delete("age")

    #print(f"Was 'age' deleted? {deleted}")

    print(f"Value for 'age': {ht.get('age')}") # Should be None

    print(ht)
        