# Wrong - shared list!
class TodoList:
    items = []  # Class attribute

list1 = TodoList()
list1.items.append("Buy milk")

list2 = TodoList()
print(list2.items)  # ['Buy milk'] - Oops!

# Right - instance attribute
class TodoListSec:
    def __init__(self):
        self.items = []  # Each instance gets its own


l1 = TodoListSec()
l1.items.append('Shree Ram')

l2= TodoListSec()
l2.items.append('Jay Ram')
print(f'l1: {l1.items}')
print(f'l2: {l2.items}')


# -------------=-------------
# Wrong - attribute might not exist
class Counter:
    def increment(self):
        self.count += 1  # Error if count doesn't exist!

# Show error: 'Counter' object has no attribute 'count'
# c1 = Counter()
# c1.increment()
# print(c1.count) 


# Right - initialize in __init__
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1