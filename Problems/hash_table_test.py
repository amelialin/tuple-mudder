from hash_table import hash_create, hash_string, hash_insert

def test_hash_table():
    table = hash_create()
    assert hash_create() == [[], [], [], []]
    table = hash_insert(table, 'test0', 0)
    assert hash_insert(table, 'test0', 0) == [[], [('test0', 0)], [], []]
    table = hash_insert(table, 'test1', 1)
    assert hash_insert(table, 'test1', 1) ==[[('test1', 1)], [('test0', 0)], [], []]
    table = hash_insert(table, 'test2', 2)
    assert hash_insert(table, 'test2', 2) == [[('test1', 1)], [('test0', 0)], [], [('test2', 2)]]
    table = hash_insert(table, 'test3', 3)
    assert hash_insert(table, 'test3', 3) == [[('test1', 1)], [('test0', 0)], [('test3', 3)], [('test2', 2)]]
    table = hash_insert(table, 'test4', 4)
    assert hash_insert(table, 'test4', 4) == [[('test1', 1)], [('test0', 0), ('test4', 4)], [('test3', 3)], [('test2', 2)]]
    table = hash_insert(table, 'test0', 100)
    assert hash_insert(table, 'test0', 100) == [[('test1', 1)], [('test0', 100), ('test4', 4)], [('test3', 3)], [('test2', 2)]]
    table = hash_insert(table, 'test4', 400)
    assert hash_insert(table, 'test4', 400) == [[('test1', 1)], [('test0', 100), ('test4', 400)], [('test3', 3)], [('test2', 2)]]