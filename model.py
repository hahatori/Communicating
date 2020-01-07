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

# Define arguments.
num_of_agents = 100     # Make a num_of_agents variable and assign it to 100
num_of_iterations = 10  # Make a num_of_iterations variable and assign it to 10
neighbourhood = 20      # Make a neighbourhood variable and assign it to 20
agents = []             # Creat agents list.
#rowlist = []            
environment = []        # Creat environment list.

# To load file.
with open("in.txt") as f:
    data = f.read().splitlines() # Only read
# The downloaded text format is not standard, so needs to change.
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
    f.write(line) # Only write
#f.close()


# Make the agents by putting into a for-loop.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood)) 
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)    # Make scatter plot.
#matplotlib.pyplot.show()

# Move the agents by putting into nest for-loops.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()                  # Calling move method from agent.
        agents[i].eat()                   # Calling eat method from agent.
        agents[i].share_with_neighbours() # Calling share_with_neighbours method from agent.

# Set properties and show the plot.
matplotlib.pyplot.xlim(0, 100)            # Set the x-axis range from 0 to 100.
matplotlib.pyplot.ylim(0, 100)            # Set the y-axis range from 0 to 100.
matplotlib.pyplot.title("Plot")           # Set plot title.
matplotlib.pyplot.imshow(environment)     # Display an image on the axes.

#for i in range(num_of_agents):
   # matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

# Use for-each loop iterator to put out agents.    
for self in agents:
    for agent in agents:
        agentframework.Agent.distance_between(self, agent) # Calling the method from agentframework.py.     

# Display the scatter dots plot.
matplotlib.pyplot.show()                  

