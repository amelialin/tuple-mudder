#  Implement a simple hash table. Implement three functions; define semantics where unclear. Keys and values are strings only.
# hash_string(string) -> integer
# hash_create() -> table
# hash_insert(table, key, value)
# hash_get(table, key) -> value
# hash_remove(table, key) 

def hash_create():
    """Creates a table with 256 empty buckets."""
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
    # print table
    # print bucket
    for i, tuples in enumerate(table[bucket]):
        # print tuples[0], tuples[1]
        # print i, tuples
        if tuples[0] == key:
            print 'Entry already exists'
            # print bucket, i, tuples
            # print table[bucket][i]
            table[bucket][i] = (key, value)
            # print tuples
            return table
    table[bucket].append((key, value))
    print table

if __name__ == "__main__":
    from sys import argv
    script, key, value = argv
    table = hash_create()
    print hash_insert(table, 'test0', 0)
    print hash_insert(table, 'test1', 1)
    print hash_insert(table, 'test2', 2)
    print hash_insert(table, 'test3', 3)
    print hash_insert(table, 'test4', 4)
    print hash_insert(table, 'test0', 100)
    print hash_insert(table, 'test4', 400)