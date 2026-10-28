class TimeMap:

    def __init__(self):
        self.timemap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        timemap = self.timemap

        if key not in timemap:
            timemap[key] = []
        
        timemap[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        timemap = self.timemap

        if key not in timemap:
            return ""

        lower = 0
        upper = len(timemap[key]) - 1

        key_list = timemap[key]

        while lower <= upper: 
            middle = lower + ((upper-lower) // 2)

            if timestamp == key_list[middle][0]:
                return key_list[middle][1]
            
            if timestamp < key_list[middle][0]:
                upper = middle - 1

            if timestamp > key_list[middle][0]:
                lower = middle + 1

        if upper == -1:                               
            return ""
        return key_list[upper][1]
            