#!python

from LinkedList import LinkedList


class HashTable(object):

    def __init__(self, num_buckets=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(num_buckets)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ["{!r}: {!r}".format(key, val) for key, val in self.items()]
        return "{" + ", ".join(items) + "}"

    def __repr__(self):
        """Return a string representation of this hash table."""
        return "HashTable({!r})".format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Time complexity: O(1) - we track the size in items()
        Space complexity: O(1) - only storing a single number"""
        # Calculate load factor: number of items / number of buckets
        return len(self.items()) / len(self.buckets)

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table."""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: O(1) - when the key is in the first node of the bucket
        Worst case running time: O(n) - when the key is at the end of a bucket with n items
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # Find the entry with the given key in that bucket, if one exists
        node = bucket.find(key)
        if node is not None:
            # Return the given key's associated value
            return node.data[1]
        else:
            raise KeyError("Key not found: {}".format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case running time: O(1) - when adding to an empty bucket or updating first item
        Worst case running time: O(n) - when updating last item in a bucket with n items
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # Find the entry with the given key in that bucket, if one exists
        node = bucket.find(key)
        if node is not None:
            # If found, update the value
            node.data = (key, value)
        else:
            # If not found, insert the new key-value entry
            bucket.append((key, value))

        # Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # If so, automatically resize to reduce the load factor
            self._resize(len(self.buckets) * 2)

    def delete(self, key):
        # THIS IS STRETCH WILL NEED TO IMPLEMENT DELETE IN LL
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in

        # Find the entry with the given key in that bucket, if one exists
        pass

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best case running time: O(n) - must traverse all n items to rehash them
        Worst case running time: O(n) - same as best case
        Space complexity: O(n) - need to store all n items temporarily"""
        # Store all current key-value entries
        all_entries = self.items()
        # Create a new list of new_size total empty linked list buckets
        self.buckets = [LinkedList() for _ in range(new_size)]
        # Insert each entry into the new buckets using the new size
        for key, value in all_entries:
            index = self._bucket_index(key)
            self.buckets[index].append((key, value))


def test_hash_table():
    ht = HashTable(4)
    print("HashTable: " + str(ht))

    print("Setting entries:")
    ht.set("I", 1)
    print("set(I, 1): " + str(ht))
    ht.set("V", 5)
    print("set(V, 5): " + str(ht))

    print("buckets: " + str(len(ht.buckets)))
    print("load_factor: " + str(ht.load_factor()))
    ht.set("X", 10)
    print("set(X, 10): " + str(ht))
    ht.set("L", 50)  # Should trigger resize
    print("set(L, 50): " + str(ht))

    print("buckets: " + str(len(ht.buckets)))
    print("load_factor: " + str(ht.load_factor()))

    print("Getting entries:")
    print("get(I): " + str(ht.get("I")))
    print("get(V): " + str(ht.get("V")))
    print("get(X): " + str(ht.get("X")))
    print("get(L): " + str(ht.get("L")))

    print("Deleting entries:")
    ht.delete("I")
    print("delete(I): " + str(ht))
    ht.delete("V")
    print("delete(V): " + str(ht))
    ht.delete("X")
    print("delete(X): " + str(ht))
    ht.delete("L")
    print("delete(L): " + str(ht))

    print("buckets: " + str(len(ht.buckets)))
    print("load_factor: " + str(ht.load_factor()))
