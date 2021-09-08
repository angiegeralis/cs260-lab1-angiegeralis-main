'''
Author      : Angie Geralis
Class       : CS260
Date        : 9/5/21
Description : This is the tutorial for matplotlib for lab 1. Here we will create and push
two different plots - one using real data by reading a csv file and the other using the
mathematical functions for cubic and quadratic lines.
'''

import matplotlib.pyplot as plt
import numpy as np

################################################################################
# MAIN
################################################################################

'''
data = np.loadtxt("data/facebook_users.csv", dtype=int, delimiter=",")
print(data)
'''
def main():
    # TODO your code here
    years = []
    users = []
    fb_file = open('data/facebook_users.csv','r')
    # cycle through file, assign first index to years and second to number of users
    for line in fb_file:
        tokens = line.split(",") # split data based on commas
        years.append(int(tokens[0]))
        users.append(int(tokens[1]))
    print(years)
    print(users)
    plt.scatter(years, users, color="black")
    plt.xlabel("year")
    plt.ylabel("number of users (millions)")
    plt.title("FB Users Over Time")
    #create regression line
    #y = -432342.27 + 215.39 * x
    y=[]
    #cycle through years, input each year into regression line
    for i in range(len(years)):
        y.append(-432342.27 + 215.39 * years[i])
    plt.plot(years, y, color="blue")
    plt.show()

    # part b
    y_qvalues =[]
    quad_coefs = [0, 4, -1]       # y = 4x - x^2
    x_qvalues = np.linspace(0, 5, 10) # start at 0, end at 5, with 10 points total
    #cycle through x values, input coefficients into equation
    for i in range(len(x_qvalues)):
        y_qvalues.append(quad_coefs[0]+quad_coefs[1]*i+quad_coefs[2]*i*i)
    plt.plot(x_qvalues, y_qvalues, label="quadratic")

    y_cvalues = []
    cubic_coefs = [2, 0, -2, 1]   # y = 2 - 2x^2 + x^3
    x_cvalues = np.linspace(0, 5, 10) # start at 0, end at 5, with 10 points total
    #cycle through x values, input coefficients into equation
    for i in range(len(x_cvalues)):
        y_cvalues.append(cubic_coefs[0]+cubic_coefs[1]*i+cubic_coefs[2]*i*i+cubic_coefs[3]*i*i*i)
    plt.plot(x_cvalues, y_cvalues, label="cubic")
    plt.legend()
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("Graphing Cubic and Quadratic Functions")
    plt.show()
    plt.savefig("figures/quad_cubic.pdf", format='pdf')

pass

if __name__ == "__main__" :
    main()
