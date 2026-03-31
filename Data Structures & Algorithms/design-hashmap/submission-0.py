class MyHashMap:

    def __init__(self):
        self.data=[]
        

    def put(self, key: int, value: int) -> None:
        if self.data:
            for i in self.data:
                if i[0]==key:
                    i[1]=value
                    return
            else:
                self.data.append([key,value])
        else:
            self.data.append([key,value])
        

    def get(self, key: int) -> int:
        if self.data:
            for i in self.data:
                if i[0]==key:
                    return i[1]
        return -1
        

    def remove(self, key: int) -> None:
        if self.data:
            for i in self.data:
                if i[0]==key:
                    self.data.remove(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)