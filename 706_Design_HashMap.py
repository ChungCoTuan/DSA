class MyHashMap:

    def __init__(self):
        # Khởi tạo 1000 bucket để lưu trữ
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Hàm băm đơn giản: chia lấy dư cho kích thước bảng
        return key % self.size

    def put(self, key, value):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        
        # Kiểm tra xem key đã tồn tại trong bucket chưa
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                # Nếu tồn tại, cập nhật giá trị mới và kết thúc
                bucket[i][1] = value
                return
        
        # Nếu chưa tồn tại, thêm cặp [key, value] mới vào bucket
        bucket.append([key, value])

    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        
        # Tìm kiếm key trong bucket tương ứng
        for k, v in bucket:
            if k == key:
                return v
        
        # Nếu không tìm thấy, trả về -1 theo yêu cầu đề bài
        return -1

    def remove(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        
        # Duyệt qua bucket để tìm và xóa cặp tương ứng
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return