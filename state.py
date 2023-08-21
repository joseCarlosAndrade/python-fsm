from typing import List

class State:
    '''
    ## Main State Class (parent)

    My implementation (jota ce) of a FSM in python using OOP.

    A __Finite State Machine__ is a way of representing a problem through possible 
    states that the process can achieve, and then, based on the current state and
    on the events that are happening, it can change to other states or stay as it is.

    For a solid example, check example.py.
 
    ----

    This is the class that represents what is a state. It must be inherited by all state childs classes.
    It creates static methods and elements that are shared by all children.

    The children (states machine classes) must be layed like the following example:
    
    >>> class StateOne(State):
    >>>     def event(self):
    >>>         # Conditions that return the other states as classes like:
    >>>         if condition:
    >>>             return StateTwo()
    >>>         else:
    >>>             return self # returns itself, doesnt change state

    ----

    ### Basic Event List operations

    Handles the event list operation and it's layed like:\n
            getAll() -> return an array with all the events \n
            add(data : str) -> add operation; param: str (event)\n
            remove(data : str) -> remove operation; param: str (event)\n
            contains(data : str) -> checks if event (str) is in event list\n
            pop() -> pop operation; para: str (event)\n
            clear() -> clear operation; clear the entire array\n

            >>> machine = StateOne()
            >>> machine.add("read_all_bases") # adds the event read_all_bases to the event list

    '''
    __allowedOperations = [-1, 0, 1, 2, 3, 4]
    __eventList = []


    def __init__(self, name="") -> None:
        self.name = name # TODO: is this really useful?
        

    def __repr__(self) -> str:
        return 'none' 
    
    # State Machine operations

    def add(self, data : str) -> None:
        '''Add the data (str) element to event list
        '''
        State.__eventOp(0, data)
    
    def remove(self, data : str) -> None:
        '''Remove the data (str) element to event list
        '''
        State.__eventOp(1, data)
    
    def contains(self, data : str) -> bool:
        '''Checks if data (str) element is contained within event list
        '''
        return State.__eventOp(2, data )

    def pop(self) -> None:
        '''Pops the last element from event list
        '''
        State.__eventOp(3)
    
    def clear(self) -> None:
        '''Clears all event list array
        '''
        State.__eventOp(4)
    
    def getAll(self) -> List[str]:
        '''Return the event list as an array of str
        '''
        return State.__eventOp(-1)
    
    @classmethod
    def __eq__(cls,comparison):
        '''Comparison class method that is called when the comparison
        between an instance of this class is compared with another element
        '''
        return cls.__name__ == comparison
    

    @staticmethod
    def __eventOp(operation : int, data :str = ""):
        '''
        TODO: does it need to be static? 
        Handles the event list operation and it's layed like:\n
            -1 -> return an array with all the events \n
            0 -> add operation; param: str (event)\n
            1 -> remove operation; param: str (event)\n
            2 -> checks if event (str) is in event list\n
            3 -> pop operation; para: str (event)\n
            4 -> clear operation; clear the entire array\n

            >>> SomeState.eventOp(0, "read_all_bases") # adds the event\
                             read_all_bases to the event list
        '''

        if operation not in State.__allowedOperations:
            raise Exception("Operation not found")
        
        
        if operation == 0: # Add
            State.__eventList.append(data)

        elif operation == 1: # Remove
            if data in State.__eventList:
                State.__eventList.remove(data)
            
            else:
                print("Event not in list")
        
        elif operation == 2: # Check if in list
            if data in State.__eventList:
                return True
            
            return False

        elif operation == 3: # Pop
            if len(State.__eventList) > 0:
                State.__eventList.pop()
            else:
                print("Event list empty")

        elif operation == 4: # Clear all
            State.__eventList = []
            
        elif operation == -1:
            return State.__eventList

    @classmethod
    def __str__(cls) -> str:
        '''Returns the name of the state by getting its name.
        Each child state class must have names layed like:
        
        >>> class StateName(State):
        >>> machine = StateName()
        >>> print(machine)
            \'StateName\'
        '''
        return cls.__name__
    
    def getName(self):
        return self.name

# EXAMPLes

if __name__ == "__main__":

    class StateOne(State):
        '''
        StateOne documentation
        '''

        def event(self):
            # conditions
            # if condition:
            #   return StateTwo
            return self

    class StateTwo(State):
        '''
        StateTwo documentation
        '''
        
        def event(self):
            return StateOne()


    a = StateOne("flying")
    b = StateTwo("landing")
    print(a, b)
    # a.__eventOp(0, "reached") 
    a.add("reached")
    a.add("on_base") 
    print(a.getAll())
    # b.eventOp(0, "landed")
    b.add("landed")
    print(b.getAll())
    b.pop()
    print(a.getAll())

    if a == 'StateOne':
        print(f"it is equal (__eq__() being called): {a}")
    else:
        print('not')
    '''
    Output:
    >>> StateOne StateTwo
    >>> ['reached', 'on_base']
    >>> ['reached', 'on_base', 'landed']
    >>> ['reached', 'on_base']
    '''