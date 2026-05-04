"""Lab 15: plotting a formula with matplotlib
Author: Ben Garcia

program uses matplotlib to plot an Archimedian Spiral

The formula for an Archimedian Spiral is r = a + b * theta
where r is the radius, theta is the angle, and a and b are constants that determine the shape of the spiral. 
In this program, we will use a = 0 and b = 0.05 to create a simple spiral.

"""
import matplotlib.pyplot as plt
import math

def main():
    """Main function to plot an Archimedian spiral."""
    t = 100

    x_values = []
    y_values = []
    #iterate through all 100 points (t) and calculate the x any y values for each point using spiral function
    


    #set graph parameters and styling 
    plt.plot(x_values, y_values)
    plt.title("Archimedian Spiral")
    plt.xlabel("Horizontal Distance from Center")
    plt.ylabel("Vertical Distance from Center")
    plt.grid()
    plt.axis("equal")
    plt.show()


def spiral(t):
    """Returns an x, y point on an Archimedian spiral."""
    
    a = 0
    b = 0.05
    r = a + b * t
    x = r * math.sin(t)
    y = r * math.cos(t)

    return x, y
    

if __name__ == "__main__":
    main()