class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, obj):
        self.__next = obj

    def get_data(self) -> str:
        return self.__data

    def set_data(self, obj):
        self.__data = obj


class Stack:
    def __init__(self):
        self.top = None
        self.bot = None

    def push(self, obj: StackObj):
        if self.top is None:
            self.top = obj
            return
        cur_node = self.top
        while True:
            if cur_node.get_next() is None:
                result = self.bot
                self.bot = obj
                cur_node.set_next(self.bot)
                return result
            cur_node = cur_node.get_next()

    def pop(self):
        if self.top is None:
            return
        cur_node = self.top
        while True:
            if cur_node.get_next() == self.bot:
                pop_item = self.bot
                cur_node.set_next(None)
                self.bot = cur_node
                return pop_item
            cur_node = cur_node.get_next()

    def __add__(self, other):
        self.push(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        for i in other:
            self.push(StackObj(i))
        return self

    def __imul__(self, other):
        return self.__mul__(other)

    def __simple_list(self):
        res = []
        cur_node = self.top
        while True:
            if cur_node == self.bot:
                res.append(cur_node)
                return res
            res.append(cur_node)
            cur_node = cur_node.get_next()

    def __len__(self):
        return len(self.__simple_list())

    def __getitem__(self, item):
        if item not in range(0, len(self.__simple_list())):
            raise IndexError
        else:
            return self.__simple_list()[item]

    def __setitem__(self, key, value: StackObj):
        if key not in range(0, len(self.__simple_list())):
            raise IndexError
        if key == 0:
            movement = self.__simple_list()[key+1]
            self.top = value
            self.top.set_next(movement)
        elif key+1 > len(self.__simple_list()) - 1:
                prev = self.__simple_list()[key - 1]
                jump_over = None
                prev.set_next(value)
                prev.get_next().set_next(jump_over)
                self.bot = prev.get_next()
        else:
            prev = self.__simple_list()[key - 1]
            jump_over = self.__simple_list()[key].get_next()
            prev.set_next(value)
            prev.get_next().set_next(jump_over)






st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[0] = StackObj("obj2-new")
for i in range(0, len(st)):
    print(st[i].get_data())