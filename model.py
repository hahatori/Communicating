import random
import operator
import matplotlib.pyplot
import agentframework
import csv

"""
# Put these codes into Agent.
def distance_between(self, agent):
    return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
"""

num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20
agents = []
rowlist = []
environment = []

# To load file.
with open("in.txt") as f:
    data = f.read().splitlines() 

    for row in data:
        rowlist = []
        for value in row.split(','):
            if value[-1] == '\\':
                value1 = value[0:(len(value)-1)]
                rowlist.append(int(value1))
            else:
                rowlist.append(int(value))
        environment.append(rowlist)

for line in agents:
    f.write(line)
#f.close()


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents, neighbourhood))
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#matplotlib.pyplot.show()

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #agents[i].move()
        #agents[i].eat()
        agents[i].share_with_neighbours()

# Set properties and show the plot.
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.title("Plot")
matplotlib.pyplot.imshow(environment)

#for i in range(num_of_agents):
   # matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

for self in agents:
    for agent in agents:
        distance = distance_between(self, agent)    

matplotlib.pyplot.show()

