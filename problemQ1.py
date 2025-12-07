import matplotlib.pyplot as plt

x = [-10 ,-9 , -8 , -7 , -6 , -5 , -4 , -3 , -2 , -1 , 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
y = [] #because it value will be derived from x
for i in x:
    y.append(i**2)
print(x)
print(y)
plt.title("Square Function") #giving heading
plt.xlabel("X axis") # giving label to x-axis
plt.ylabel("Y axis")
plt.grid(True) # the lines behind the ploted point as in cartesian plain 
plt.plot(x, y , color = "green" , marker = "o", markerfacecolor = "blue"  , linewidth = 2 , markersize = 6) #plot the numbers which line color will be green and point color will be blue and the width of line is 2 and the size of point is 6
plt.show() #it show mena help in visualization of the ploted point