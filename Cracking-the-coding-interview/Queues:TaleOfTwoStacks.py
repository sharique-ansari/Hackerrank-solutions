class MyQueue(object):
    def __init__(self):
        self.firststack = []
        self.secondstack = []

    def put(self, value):
        self.firststack.append(value)

    def peek(self):
        self.prepare()
        a=self.secondstack.pop()
        self.secondstack.append(a)
        return a

    def pop(self):
        self.prepare()

        self.secondstack.pop()


    def prepare(self):

        if not self.secondstack :
            while self.firststack:
                self.secondstack.append(self.firststack.pop())





queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())