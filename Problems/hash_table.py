#  Implement a simple hash table. Implement three functions; define semantics 
# where unclear. Keys and values are strings only.
# hash_string(string) -> integer
# hash_create() -> table
# hash_insert(table, key, value)
# hash_get(table, key) -> value
# hash_remove(table, key) 

# Computational complexity...maybe would only depend on if what the complexity 
# of hash(string) is, for increasing length of string? Looks like O(n) 
# according to the internets.

def hash_create():
    """Creates a table with 10 empty buckets."""
    table = []
    for i in range(4):
        table.append([])
    return table

def hash_string(string):
    """Takes a string as input, outputs an integer."""
    bucket = hash(string) % 4
    return bucket

def hash_insert(table, key, value):
    """Inserts a value into the specified table for the specified key."""
    bucket = hash_string(key)
    for i, tuples in enumerate(table[bucket]):
        if tuples[0] == key: # if key already exists
            table[bucket][i] = (key, value)
            return table
    table[bucket].append((key, value)) # if key does not already exist
    return table

if __name__ == "__main__":
    from sys import argv
    script, key, value = argv
    table = hash_create()
    print hash_insert(table, key, value)