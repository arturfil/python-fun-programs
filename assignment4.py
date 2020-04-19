""" Name: Arturo Filio
    Class: CSC498
    C11303326
"""

"""
  IMPORTANT NOTE, Please see that the graphs will print one by one, you have to close one in order to see the next one, same goes for the final result
  with the data frame chaned with  the new added smoothed curve.

  thanks
"""

# Assignment 4 pandas and numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sp

# here we are importing the file
pd.set_option('display.max_rows', 123)
df = pd.read_csv("Florida_temp_mean_1895_2017.csv")

# Here we interpolate the values
df = df.interpolate()

# set the values after interpolation
year = df['Year'].values
temperature = df['Temperature'].values
anomaly = df['Anomaly'].values

# here we print the information
# print(df)

# here we get the mean && std. dev.
temp_avg = np.mean(temperature)
temp_std = np.std(temperature)

print(f"The average temperature is {temp_avg}")
print(f"The standard deviation of the temperature is {temp_std}")

# create plot 
graph = df.plot(x='Year', y="Temperature", kind="line", marker="o")

# show the plot points and lines of temperature vs years
plt.xlabel('Years')
plt.ylabel('Temperature (F)')
plt.title('Average Temperature each year')

plt.show()
# # graph = plt.plot(df)

axes = plt.axes()
axes.grid()
axes.set_axisbelow(True)
plt.hist(temperature, bins=20, histtype = 'stepfilled')
plt.show()

# Smoothing the curve
axes = plt.axes()

# initial year vs temp graph
# plt.plot(year,temperature,marker = 'o')
# plt.xlabel('Year')
# plt.ylabel('Temperature')
# plt.title('Raw Signal')
# axes.grid()
# plt.show()

# smooth signal correlation
smoothsignal = np.correlate(temperature,[.2,.2,.2,.2,.2], mode = 'same')
# print(smoothsignal) <- test to see if the data is getting "rolled over"
plt.subplot(2,1,1)
plt.plot(year,smoothsignal)
plt.gca().grid(True)
plt.xlabel('Year')
plt.ylabel('Temperature (F)')
plt.title('Moving average smooth curve')
plt.show()

#plt.subplot(2,1,2)
C = np.zeros(21,dtype = 'float')
C.fill(1/21)
smooth_sp = sp.correlate(temperature,C,mode = 'nearest')

plt.plot(year,smooth_sp)
plt.gca().grid(True)
plt.title('smooth signal with scipy')
plt.xlabel('Year')
plt.ylabel('Temperature (F)')
plt.tight_layout(pad = 1.0)
plt.show()

df['Smoothed_Signal'] = smooth_sp

print("\n\n")
print(df)

print("\n\nEnd of script...")


