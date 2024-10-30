# bloom_filter.py
import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size
    
    def _hashes(self, item):
        hashes = []
        for i in range(self.num_hashes):
            hash_digest = hashlib.md5((str(i) + item).encode('utf-8')).hexdigest()
            hashes.append(int(hash_digest, 16) % self.size)
        return hashes

    def add(self, item):
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def contains(self, item):
        return all(self.bit_array[hash_value] == 1 for hash_value in self._hashes(item))
