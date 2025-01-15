from typing import Generic, TypedDict, Optional, TypeVar
import random as rand
#from __future__ import annotations

T = TypeVar('T')

class Node(TypedDict, Generic[T]):
    value : T
    prev : Optional['Node']
    #prev : Optional[Node] # need to import annotations for this to work, called forward referencing

class TomsStack():

    def __init__(self) -> None:
        self.head : Optional['Node[T]'] = None
        self.length : Optional[int] = 0

    
    def pop(self) -> Optional[T]:
        self.length = max(0, self.length - 1)
        
        if self.length == 0:
            popped = self.head
            self.head = None
            return None if popped is None else popped['value'] #will return None
        
        popped = self.head
        self.head = popped['prev']
        
        return self.head['value']

    def push(self, value : float) -> None:

        self.length += 1
        new_head : Node = {"value": value, "prev" : None}

        if self.head is None:
            self.head = new_head
            return
        
        new_head['prev'] = self.head
        self.head = new_head
    
    def peek(self) -> Optional[float]:
        return self.head['value'] if self.head is not None else None


if __name__ == "__main__":
    test_stack = TomsStack()

    for i in range(100):
        test_stack.push([])
        #test_stack.push(rand.randint(0,100))

    while test_stack.peek() is not None:
        print(test_stack.pop())