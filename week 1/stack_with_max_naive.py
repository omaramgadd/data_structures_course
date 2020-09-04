import sys


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__max = []
        self.return_list = []

    def Push(self, a):
        if len(self.__stack) < 1:
            self.__stack.append(a)
            self.__max.append(a)
        else:
            self.__stack.append(a)
            if a >= self.__max[-1]:
                self.__max.append(a)
            else:
                self.__max.append(self.__max[-1])

    def Pop(self):
        assert (len(self.__stack))
        self.__stack.pop()
        self.__max.pop()

    def maxi(self):
        self.return_list.append(self.__max[-1])

    def printing(self):
        return self.return_list


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            stack.maxi()
    the_list = stack.printing()
    for element in the_list:
        print(element)
