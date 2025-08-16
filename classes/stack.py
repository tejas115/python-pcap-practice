class Stack:
    def __init__(self):
        self.__stack_list =[]

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        if self.is_empty():
            return None
        val  = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def peek(self):
        if not self.is_empty():
            return self.__stack_list[-1]
        return None

    def is_empty(self):
        return len(self.__stack_list) == 0

    def size(self):
        return len(self.__stack_list)
    
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
            self.__sum += val
            Stack.push(self, val)

    def pop(self):
            val = Stack.pop(self)
            if val is not None:
                self.__sum -= val
            return val

    def get_sum(self):
            return self.__sum   
        

stack = AddingStack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Sum:", stack.get_sum())
print("Pop:", stack.pop())
print("Sum after pop:", stack.get_sum())