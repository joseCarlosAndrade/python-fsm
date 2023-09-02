# Finite State Machine for general purpose

My implementation of a Finite State Machine using Python 3 with OOP.

----

A **Finite State Machine** is a way of representing a problem through possible states that the process can achieve, and then, based on the current state and on the events that are happening, it can change to other states or stay as it is.
For a solid example, check `example.py``.

----

## How to implement

The `state.py` defines what is a state. It must be inherited by all children state classes.
It creates static methods and elements that are shared by all children.
The children (states machine classes) must be layed like the following example:

```python
     class StateOne(State):
        '''State description (documentation)
        '''

         def event(self):
             # Conditions that return the other states as classes like:
             if condition:
                 return StateTwo
             else:
                 return self # returns itself, doesnt change state

    class StateTwo(State):
        '''
        StateTwo description
        '''
        
        def event(self):
            return StateOne
```

----

### Basic Event List operations

Handles the event list operation and it's layed like:

- `getAll()` -> return an array with all the events

- `add(data : str)` -> add operation; param: str (event)

- `remove(data : str)` -> remove operation; param: str (event)

- `contains(data : str)` -> returns `True` if event (str) is in event list; 

- `pop()` -> pop operation; para: str (event)

- `clear()` -> clear operation; clears the entire event array

Here's an example of how to manipulate the events:

    machine = StateOne()
    machine.add("read_all_bases") # adds the event read_all_bases to the event list
    machine.updateEvent() # updates the current event
