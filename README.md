# Communicating
Make agents talking to each other by altering each other's variables

This project including [in.txt](https://github.com/hahatori/Communicating/blob/master/in.txt), [agentframework.py](https://github.com/hahatori/Communicating/blob/master/agentframework.py) and [model.py](https://github.com/hahatori/Communicating/blob/master/model.py).

## Contents

- [Details](#details)
- [Theoretical Results](#theoretical-results)
- [Actual Results](#actual-results)
- [Issues](#issues)

## Details

### The key elements:

**in.txt** is a text file with raster data.

**Agent** code can build agents to interact.

**Model** code can creat models for connecting developers and users.

### The self 

**Creat Class, Object and Method**

```sh
$ class Agent:   # Creat "Agent" class.    
      def eat(self): # Define "eat" method.
      pass    #An empty block.
      
  a = Agent() #Creat a object.
  a.eat()
  print a
```

**agentframework.py** :

```sh
$ import random 

  class Agent(): 

      def __init__(self, environment):  
          self.environment = environment 
          self.store = 0
          self.y = random.randint(0,99) 
          self.x = random.randint(0,99) 

      def move(self):
          if random.random() < 0.5:
              self.x = (self.x + 1) % 100
          else:
              self.x = (self.x - 1) % 100

          if random.random() < 0.5:
              self.y = (self.y + 1) % 100
          else:
              self.y = (self.y - 1) % 100

      def eat(self):
          if self.environment[self.y][self.x] > 10:
              self.environment[self.y][self.x] -= 10
          self.store += 10 

      def __str__(self):
         return "y= %s, x= %s" % (self.y, self.x)
          
  a = Agent("environment")
  print(a)
  print(a.move, a.eat)
  print("Location:%s" % id(a), a)
```

Output:

```sh
$ <bound method Agent.move of <__main__.Agent object at 0x117326a10>> <bound method Agent.eat of <__main__.Agent object at 0x117326a10>>
  y= 15, x= 36
  Location:4684147216 y= 15, x= 36
```

### Matplotlib

**Matplotlib** is a Python 2D drawing library that generates graphics in a variety of hardcopy formats and cross-platform interactive environments. With Matplotlib, developers can generate graphs, histograms, power spectra, bar charts, error graphs, scatter plots, etc. in just a few lines of code.

```sh
$ import matplotlib.pyplot as plt 

  plt.xlim(0, 100)          
  plt.ylim(0, 100) 
  plt.show()
```
Output:

![Matplotlib frame](https://github.com/hahatori/Python_Assignment1/blob/master/Matplotlib.png)

## Theoretical Results

Expect model to import the in.txt file and call the agent, the agent moves random coordinate points and calculates the distance between two sets of them, then the model displays an image on the axes, and the 10 points are randomly distributed over the images. 

## Actual Results

![Plot](https://github.com/hahatori/Python_Assignment1/blob/master/Communicating.png)

## Issues

1. ```__init__(self, environment):``` is a initialization method and it creates a formal parameter called **environment**. When creating a new instance of the class, we do not explicitly call the __init__ method, but pass the arguments in the parentheses following the class name. environment is a mutable object,and the variable passes in the object, all the Agents link to the same environment object. So when the Agents changes the environment data, it changes for all agents.

2. ```__str__(self):``` can return object and description property information, will be automatically called. ```str()``` built-in function uses ```__str__``` to display the string of the object.

3. The question of by finding the size of the agent's internal environment and using the size when randomly assigning their starting positions and working with boundary conditions, the agent can wander through the environment.
 
