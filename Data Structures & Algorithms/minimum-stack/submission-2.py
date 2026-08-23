class MinStack:

    def __init__(self):
        self.__stack = []
        self.__minStack = []
        self.__length = 0

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if self.__length > 0:
            if self.__minStack[self.__length - 1] > val:
                self.__minStack.append(val)
            else:
                self.__minStack.append(self.__minStack[self.__length - 1])
        else:
            self.__minStack.append(val)
        self.__length += 1

    def pop(self) -> None:
        self.__minStack = self.__minStack[:-1]
        self.__stack.pop()
        self.__length -= 1


    def top(self) -> int:
        return self.__stack[self.__length - 1]

    def getMin(self) -> int:
        return self.__minStack[self.__length - 1]
