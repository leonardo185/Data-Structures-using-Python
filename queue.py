
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if(self.__rear >= self.get_max_size() -1):
            #print("Full")
            return True
        else:
            return False
        #Remove pass and write the logic to check whether Queue is full. If the queue is full, return true else return false.

    def enqueue(self,data):
        if(self.is_full() == False):
            self.__rear+=1
            self.__elements[self.__rear] = data
        else:
            print("Full.")
        #Remove pass and write the logic to enqueue an element. Enqueue should be done only if queue is not full. Otherwise display appropriate message.

    def display(self):
        for i in range(len(self.__elements)):
            if(self.__elements[i]!=None):
                print(self.__elements[i])
            else:
                continue
        #Remove pass and write the logic to display all the queue element(s).

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

queue1=Queue(5)
#Enqueue all the required element(s).
queue1.enqueue("Tom")
queue1.enqueue("Leo")
queue1.enqueue("Hari")
queue1.enqueue("Kamalesh")
queue1.enqueue("Santhosh")
queue1.enqueue("Karthi")
#Display all the elements in the queue.
queue1.display()
