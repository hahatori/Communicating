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

**self** represents an instance of a class, not a class. self.class points to the class.

```sh
$ class Agent:       
      def eat(self): 
          print(self)
          print(self.__class__)
      
  a = Agent() 
  print (a)
  a.eat()  
```
Output:

```sh
$ <__main__.Agent object at 0x12253fc10>
  <__main__.Agent object at 0x12253fc10>
  <class '__main__.Agent'>
```

**self** needs to be defined at definition time, but is passed in automatically when called :

```sh
$ class Agent(object): 
  def __init__(self, name, age): 
    self.name = name 
    self.age = age 
  
  def SetName(self,name): 
    self.name = name 
  
  def SetAge(self,age): 
    self.age = age 
  
  def GetName(self): 
    return self.name 
  
  def GetAge(self): 
    return self.age 
  
u = User('Obama',17) 
print u.GetName() 
print u.GetAge() 
```

Output:

```sh
$ Obama
  17
```

## Theoretical Results

**Communication** allows programs to run to adjust each other's variables, or to call functions within each other and pass information, or to retrieve information from each other.

Move below statement to **agentframework.py** :

```sh
$ def distance_between(self, agent):
    return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
```

Then use ```agentframework.Agent.distance_between(self, agent) ``` to call it in the model. 

## Actual Results

![Plot](https://github.com/hahatori/Python_Assignment1/blob/master/Communicating.png)

## Issues

1. ```__init__(self, environment):``` is a initialization method and it creates a formal parameter called **environment**. When creating a new instance of the class, we do not explicitly call the __init__ method, but pass the arguments in the parentheses following the class name. environment is a mutable object,and the variable passes in the object, all the Agents link to the same environment object. So when the Agents changes the environment data, it changes for all agents.

2. ```__str__(self):``` can return object and description property information, will be automatically called. ```str()``` built-in function uses ```__str__``` to display the string of the object.

3. The question of by finding the size of the agent's internal environment and using the size when randomly assigning their starting positions and working with boundary conditions, the agent can wander through the environment.
 
