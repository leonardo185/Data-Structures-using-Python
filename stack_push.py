class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if(self.__top == (self.get_max_size() - 1)):
            #print("Full")
            return True
        else:
            return False

        #Remove pass and write the logic to check whether stack is full. If the stack is full, return true else return false.

    def push(self,data):
        if(not self.is_full()):
            self.__top +=1
            self.__elements[self.__top] = data
        else:
            self.is_full()

        #Remove pass and write the logic to push element into the stack. Element should be pushed only if the stack is not full. Otherwise, display appropriate message
    def is_empty(self):
        if(self.__top == -1):
            return True
        else:
            return False
        #Remove pass and write the logic to check whether stack is empty. If the stack is empty, return true else return false.

    def pop(self):
        if(not self.is_empty()):
            self.__elements[self.__top] = None
            self.__top-=1
        #Remove pass and write the logic to pop an element. Pop the element only if stack is not empty. Otherwise, display appropriate message

    def display(self):
        #print(*self.__elements)
        for i in range(len(self.__elements)):
            if(self.__elements[i] != None):
                print(self.__elements[i])
            else:
                continue

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

stack1=Stack(5)
#Push all the required element(s).
stack1.push("Shirt1")
stack1.push("leo")
stack1.push("karthi")
stack1.push("hari")
stack1.push("dinesh")

stack1.push("dinesh")

stack1.display()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.display()
