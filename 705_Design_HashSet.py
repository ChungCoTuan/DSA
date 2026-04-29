class MyHashSet:

    def __init__(self):
        # Chọn một số nguyên tố làm kích thước để giảm thiểu xung đột (collision)
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Hàm hash đơn giản
        return key % self.size

    def add(self, key):
        hash_key = self._hash(key)
        # Nếu key chưa tồn tại trong "thùng" (bucket) thì mới thêm vào
        if key not in self.table[hash_key]:
            self.table[hash_key].append(key)

    def remove(self, key):
        hash_key = self._hash(key)
        # Nếu tìm thấy key thì xóa đi
        if key in self.table[hash_key]:
            self.table[hash_key].remove(key)

    def contains(self, key):
        hash_key = self._hash(key)
        # Kiểm tra sự tồn tại
        return key in self.table[hash_key]

# Cách sử dụng (LeetCode sẽ tự gọi các phương thức này):
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)