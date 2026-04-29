class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {name: i for i, name in enumerate(list1)}
        
        min_sum = float('inf')
        res = []
        
        for j, name in enumerate(list2):
            if name in index_map:
                total = j + index_map[name]
                
                if total < min_sum:
                    min_sum = total
                    res = [name]
                elif total == min_sum:
                    res.append(name)
        
        return res