#1. Extending Stack Class Behavior
class Stack:
    def __init__(self):
        self._stk=[]

    def push(self,val):
        self._stk.append(val)

    def pop(self):
        val =self._stk[-1]
        del self._stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__count=0

    def get_counter(self):
        return self.__count

    def pop(self):
        self.__count+=1
        return super().pop()

stk=CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

#2a. Implementing a queue class from scratch (intermediate difficulty)
class QueueError(Exception):
    pass
class Queue:
    def __init__(self):
        self._queue=[]
    def put(self,val):
        self._queue.append(val)
    def get(self):
       if len(self._queue)==0:
           raise QueueError("Queue is empty")
       val=self._queue[0]
       del self._queue[0]
       return val
que= Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue Error")

#Extending a Queue Class Capability in Part 2a
class SuperQueue(Queue):
    def __init__(self):
        super().__init__()
    def isempty(self):
        return len(self._queue)==0

que= SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

#3. Timer Class
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours=hours
        self.__minutes=minutes
        self.__seconds=seconds
    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"
    def next_second(self):
        self.__seconds += 1
        if self.__seconds ==60:
            self.__seconds = 0
            self.__minutes+=1
            if self.__minutes==60:
                self.__minutes=0
                self.__hours+=1
                if self.__hours==24:
                    self.__hours=0
    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds <0:
            self.__seconds=59
            self.__minutes=-1
            if self.__minutes<0:
                self.__minutes=59
                self.__hours-=1
                if self.__hours<0:
                    self.__hours=23
timer= Timer(23,59,59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

#4. Weeker Class
class WeekDayError(Exception):
    pass
class Weeker:
    __days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    def __init__(self,day):
        if day not in self.__days:
            raise WeekDayError
        self.__index=self.__days.index(day)
    def __str__(self):
        return self.__days[self.__index]
    def add_days(self,n):
        self.__index=(self.__index+n)%7
    def subtract_days(self,n):
        self.__index=(self.__index-n)%7
try:
    weekday=Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday=Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

#Challenges
#I had some issues with the single and double underscores when writing my code that created Attribute errors in the __init__
#I had some difficulty with the Timer section using the prev and next _second operations, I kept getting errors that I had trouble solving
#I had some formatting trouble during the timer portion of the assignment. I had to search how to format time with the :02d code
#I had problems with the SuperQueue code section