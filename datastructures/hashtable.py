"""
MikeMcMahon - 9/24/2016

insertion is typically O(1) HOWERVER worst case is O(N) in the event we have to linearly probe and find an empty bucket
what happens when we don't have enough space? We have to increase the size of our table which sucks...
"""


class MyHashTable(object):

    class HashElement(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __str__(self):
            return "{} - {}".format(str(self.key), self.value)

    def __init__(self):
        self._default_size = 50
        self._hashtable = [None for _ in range(self._default_size)]
        self._table_size = self._default_size
        self._grow_size = 10
        self._keyset = set()

    def insert(self, key, value):
        hash_idx = hash(key) % self._table_size

        if self._is_empty(hash_idx):
            self._hashtable[hash_idx] = MyHashTable.HashElement(key, value)
            return

        # We have to linearly probe until we find an empty spot
        hash_idx += 1
        while hash_idx and hash_idx != hash(key) % self._table_size:
            # Wrap back around to the beginning in case our idx is max
            hash_idx %= self._table_size

            if self._is_empty(hash_idx):
                self._hashtable[hash_idx] = MyHashTable.HashElement(key, value)
                break
            hash_idx += 1
        else:
            # At this point we have wrapped the entire table so we have to grow it
            self._grow_table()
            self.insert(key, value)

        self._keyset.add(key)

    def _grow_table(self):
        # Grow our table
        temp = list(self._hashtable)
        self._hashtable += [None for _ in range(self._grow_size)]
        self._table_size += self._grow_size

        # Recompute the hashes of everything
        self._hashtable = [None for _ in range(self._table_size)]

        for node in temp:
            self.insert(node.key, node.value)

    def _is_empty(self, idx):
        if not self._hashtable[idx]:
            return True

    def search(self, key, default=None):
        hash_idx = hash(key) % self._table_size

        if not self._hashtable[hash_idx]:
            return default

        if self._hashtable[hash_idx] and self._hashtable[hash_idx].key == key:
            return self._hashtable[hash_idx].value

        # Can't find it in O(1) time to linear probe for it

        hash_idx += 1
        while hash_idx and hash_idx != hash(key) % self._table_size:
            # Wrap back around to the beginning in case our idx is max
            hash_idx %= self._table_size
            if self._hashtable[hash_idx] and self._hashtable[hash_idx].key == key:
                return self._hashtable[hash_idx].value
            hash_idx += 1
        else:
            # At this point we have wrapped the entire table and found no matching (WORST CASE)
            return default

    def delete(self, key):
        if key not in self._keyset:
            return KeyError("key not found in hash table")

        hash_idx = hash(key) % self._table_size

        if self._hashtable[hash_idx] and self._hashtable[hash_idx].key == key:
            self._hashtable[hash_idx] = None
            self._keyset.remove(key)
            return

        # Can't find it in O(1) time to linear probe for it
        hash_idx += 1
        while hash_idx and hash_idx != hash(key) % self._table_size:
            # Wrap back around to the beginning in case our idx is max
            hash_idx %= self._table_size
            if self._hashtable[hash_idx] and self._hashtable[hash_idx].key == key:
                self._hashtable[hash_idx] = None
                self._keyset.remove(key)
                return
            hash_idx += 1
        else:
            # At this point we have wrapped the entire table and found no matching (WORST CASE)
            # Strangly we should never ever ever hit this because we manage the keyset and guard
            # But i feel this could happen in some strange world, maybe someone fiddling with the internals?
            raise KeyError("Key not found in hash table")


def main():
    hashme = [(str(_), _) for _ in range(100)]
    hashtable = MyHashTable()
    for to_hash in hashme:
        k, v = to_hash
        hashtable.insert(k, v)

    print(hashtable.search('5'))
    print(hashtable.search('idontexist', 'idontexist'))

    hashtable.delete('1')
    try:
        hashtable.delete('idontexist')
    except KeyError as ex:
        print(ex)

    print(hashtable)

if __name__ == "__main__":
    main()
