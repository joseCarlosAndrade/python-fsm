'''
Usage example: simple FSM

Stopped -- start --> Moving (repeat until 'wall' is inserted to event list) -- target_reached --> Stopped (returns to start)
                      ^  |
                      |  | (wall)
                      |  v
                   BreakingWall (repeat until wall is not on event list anymore)


'''
from state import State
import time

# FSM MODELLING (I recommend to put these on a separated file)

class Stopped(State):
    
    def event(self):
        if self.contains('start') and not self.contains('target_reached'):
            
            return Moving()

        return self

class Moving(State):
    
    def event(self):
        if self.contains('wall'):
            return BreakingWall()
        
        elif self.contains('target_reached'):
            return Stopped()

        return self

class BreakingWall(State):
    
    def event(self):
        if self.contains('wall'):
            return self
    
        else:
            return Moving()
        

    
# FSM IMPLEMENTATION

walls = 2
car = Stopped("nome")
while True:
    time.sleep(1)
    # print(car)
    print(f'\n================================================================\n\
Current state and event list: {car}; Event List: {car.getAll()}\n\n')
   

    if car == 'Stopped' and not car.contains('target_reached'):
        print(car, 'Adding start to the event list...')
        # do stuff to start
        car.add('start')
    
    if car == 'Stopped' and car.contains('target_reached'): # if stopped and target is reached, finish
        print('Stopped with target reached: exiting cycle..')
        break

    if car == 'Moving':
        # print(car)
        if walls > 0:
            walls -= 1
            # do stuff to encounter wall
            print('Encountered a wall, adding wall to event list..')
            car.add('wall')
            
        else:
            # do stuff to reach target
            print('Target reached, adding target_reached to event list..')
            car.add('target_reached')

    
    if car == 'BreakingWall':
        # print(car)
        # do stuff to break wall
        print('Breaking wall..')
        time.sleep(1)
        print('Wall broke, popping wall from event list...')
        car.pop()
    

    
    car = car.event() # updates state based on stored events


print(f"Cycle is finished. Event list: {car.getAll()}")