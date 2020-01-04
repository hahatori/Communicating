import random 

class Agent:
    
    def __init__(self, environment, agents, neighbourhood):
        self.environment = environment
        self.store = 0
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.agents = agents
        self.neighbourhood = neighbourhood
        
    """  
    # No longer need loops through comparing distances between each agents.
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
    """   
    
    # Creat methods to calculate the distance to each of the other agents.
    def share_with_neighbours(self):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= self.neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
                
    # Put in here from model.py.   
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
   
# Creat Agent object to test print.
a = Agent("environment","agents","neighbourhood")
print(a.y, a.x)



            
                
       

   
