class PriorityQueueSortedList:

    def __init__(self):
        self._data = []
        # self._size = 0
    
    def add(self, awal, prio):

        if len(self._data)!= 0:
            pointer = 0
            while self._data[pointer][1] < prio:
                pointer += 1

            self._data.insert(pointer, (awal, prio))


        else:
            self._data.append((awal, prio))

    def peek(self):
        print(self._data[0])

    def update(self, awal, prio):
        pointer = 0

        for i in range(len(self._data)):
            if self._data[i][1] != prio:
                self._data[pointer] = (awal, prio)
    
    def remove(self):
        del self._data[0]

    def removePriority(self, prio):
        print("Data prioritas tertinggi:")
        pointer = 0

        while self._data[pointer][1] != prio:
            pointer += 1
        del self._data[pointer]

    def printIsiQueue(self):
        print("Isi semua Queue: ", end="")

        for i in self._data[:-1]:
            
            print("{}," .format(i), end=" ")
        print("{}" .format(self._data[-1]))

sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()
