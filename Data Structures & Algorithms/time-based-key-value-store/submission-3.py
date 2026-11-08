class TimeMap:

    def __init__(self):
        self.timemap = dict()
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:

            self.timemap[key] = []
        self.timemap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        arr = self.timemap[key]
        # find the index to insert timestamp
        l,r = 0,len(arr)
        while (l< r):
            mid = (l + r) // 2
            if (arr[mid][0]>timestamp):
                r = mid
            else:
                l = mid + 1
        
        if(l >=1 and arr[l-1][0]<=timestamp):
            return arr[l-1][1]
        
        else:
            return ""

        
