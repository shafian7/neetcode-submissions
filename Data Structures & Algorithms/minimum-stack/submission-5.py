class MinStack:

    def __init__(self):
        self.__stack = []
        self.__minStack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if len(self.__minStack):
            if self.__minStack[-1] > val:
                self.__minStack.append(val)
            else:
                self.__minStack.append(self.__minStack[-1])
        else:
            self.__minStack.append(val)

    def pop(self) -> None:
        self.__stack.pop()
        self.__minStack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__minStack[-1]
