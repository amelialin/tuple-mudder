# from ex39 in LPTHW.

# makes a dict data structure.

def new(num_buckets=256): # this is an *initializer* function
    """Initializes a Map with the given number of buckets."""
    aMap = [] # initialize empty list
    for i in range(0, num_buckets):
        aMap.append([]) # adds 256 empty lists to the empty list aMap
    return aMap # looks sth like [[], [], [], ...]

def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
    return hash(key) % len(aMap) # 1) Converts key > hash, which is a big giant integer. 2) Converts hash > integer. In other words, takes modulo 256 of a big giant hash number so that we can put it somewhere in aMap

def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id] # returns the correct sublist in aMap, e.g. [[], [], *[]*, ... ]

def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    """
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket): # adds a counter variable, i, to each of the iterable things in the correct sublist. kv = key value pair. e.g. bucket = [(key1, value1), (key2, value2), ... ]
        k, v = kv # unpacks the key-value pair into two variables, k for key and v for value?
        if key == k:
            return i, k, v

    return -1, key, default # otherwise if key not found, return this

def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key) # i is the SLOT within the correct bucket. e.g. [(key1, value1), *(key2, value2)*, ... ]

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not exist, append to create it
        bucket.append((key, value)) # adds a new (key, value) tuple to the end of the bucket, like: [(key1, value1), *(key2, value2)*, ... (NEW KEY, NEW VALUE)]

def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key) # find the bucket it's in

    for i in xrange(len(bucket)): # why do we need xrange here? because we don't know how many tuples we've stuffed into a bucket, so this COULD be some huge range to iterate over.
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket: # if the bucket is nonempty (i.e., doesn't just look like [] )
            for k, v in bucket:
                print k, v

def dump(aMap):
    """Prints out each bucket, as well as what is in each bucket"""
    print "Total hash table size:", len(aMap)
    nonempty_buckets = 0.0
    for bucket in aMap:
        if bucket: # if the bucket is nonempty (i.e., doesn't just look like [] )
            nonempty_buckets += 1
            print "Bucket", aMap.index(bucket), ":"
            for k, v in bucket:
                print k, v
    print "Load: %0.2f%%" % (100 * nonempty_buckets / len(aMap))
       