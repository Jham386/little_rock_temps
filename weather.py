##Takes in daily Little Rock area temperatures from 2000 to 2022, graphs, and gets major temp events.
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Opens text file, sorts day data line by line into array, sorts array into huge array
def sort_data():
    all_data = []
    with open("/home/julia/Textfiles/temp_data.txt", 'r') as file:
        for line in file:
            day = [item.strip() for item in line.split()]
            all_data.append(day)

    #Neats up list, removing \t and \n
    all_data = [item for item in all_data if item not in ['\n', '\t']]

    #Gets total number of days (aka lists) in all_data
    total_days = len(all_data)
    
    #Converts highs, lows, and averages into int, int, and float respectively
    for date in range(total_days):
        for value in range(1,3):
            all_data[date][value] = int(all_data[date][value])
    for date in range(total_days):
            all_data[date][3] = float(all_data[date][3])
    
    #Stores dates, high, low, and average temp data into seperate numpy arrays
    dates = []
    highs = np.array([], dtype = int)
    lows = np.array([], dtype = int)
    averages = np.array([], dtype = float)

    for date in range(total_days):
        dates.append(all_data[date][0])
        highs = np.append(highs, all_data[date][1])
        lows = np.append(lows, all_data[date][2])
        averages = np.append(averages, all_data[date][3])
    
def main():
    weather_arrays = sort_data()
    
main()

