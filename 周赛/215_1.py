class OrderedStream:

    def __init__(self, n: int):
        self.len = n
        self.list_n = []
        for i in range(n):
            self.list_n.append(0)
        self.ptr = 0

    def insert(self, id: int, value: str):
        tag = id - 1
        self.list_n[tag] = value
        output = []
        while self.ptr < self.len and self.list_n[self.ptr]:
            output.append(self.list_n[self.ptr])
            self.ptr +=1
        return output

if __name__ == '__main__':
    demo = OrderedStream(5)

    print(demo.insert(3,'c'))
    print(demo.insert(1,'a'))
    print(demo.insert(2,'b'))
    print(demo.insert(5,'e'))
    print(demo.insert(4,'d'))