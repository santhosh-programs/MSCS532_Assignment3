import random


class HashTable:
    def __init__(self, bucket_size):
        self.bucket_size = bucket_size
        self.tables = [None for _ in range(bucket_size)]

    def compute_h(self, k):
        return k % 997
# Takes a key and value to insert into the hash table

    def insertNewElement(self, k, v):
        i = self.compute_h(k)
        n = self.tables[i]

        while n is not None:
            if n.k == k:
                n.v = v
                return

            n = n.next_entry

        new = MapEntry(k, v)
        new.next_entry = self.tables[i]
        self.tables[i] = new

    def searchElement(self, k):
        hash_idx = self.compute_h(k)
        n = self.tables[hash_idx]

        while n is not None:
            if n.k == k:
                return n.v

            n = n.next_entry
        return None  # Key not found
    # Hash function

    def delete(self, k):
        idxx = self.compute_h(k)
        entry = self.tables[idxx]
        prev = None

        while entry is not None:
            if entry.k == k:
                if prev is None:
                    self.tables[idxx] = entry.next_entry
                else:
                    prev.next_entry = entry.next_entry
                return
            prev = entry
            entry = entry.next_entry

    def display(self):
        if all(bucket is None for bucket in self.tables):
            print("The hash table is empty.")
            return

        for index, bucket in enumerate(self.tables):
            entries = []
            node = bucket
            while node:
                entries.append(f"{node.k}: {node.v}")
                node = node.next_entry

            if entries:
                print(f"Bucket {index}:")
                print("  " + ", ".join(entries))
            else:
                print(f"Bucket {index}: (empty)")


# Represents the Node or Entry item that will be added in the hash table
class MapEntry:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next_entry = None

    def __to_str__(self):
        return f"String Representation = MapEntry(key={self.k}, value={self.v})"


if __name__ == "__main__":
    hash_table = HashTable(17)

    hash_table.insertNewElement(1, 11)
    hash_table.insertNewElement(2, 11)

    hash_table.delete(1)
    print("After removing key 1:")
    hash_table.display()
