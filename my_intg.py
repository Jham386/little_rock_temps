#Takes in daily little rock temperatures, sorts, gets integrals
import numpy as np

#Opens text file, sorts day data line by line into array, sorts array into huge array
def sort_data():
    all_data = []
    with open("temp_data.txt", 'r') as file:
        next(file)
        for line in file:
            day = [item.strip() for item in line.split()]
            all_data.append(day)

    #Neats up list, removing \t and \n
    all_data = [item for item in all_data if item not in ['\n', '\t']]
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

    return highs, lows, averages

def my_intg(highs, lows, averages):
    counter = 0
    integral_h = 0
    integral_l = 0
    integral_a = 0

    #All have same number of days
    while counter < len(highs) - 1:
        integral_h += ((counter + 1) - counter) * (1/2) * (highs[counter + 1] + highs[counter])
        integral_l += ((counter + 1) - counter) * (1/2) * (lows[counter + 1] + lows[counter])
        integral_a += ((counter + 1) - counter) * (1/2) * (averages[counter + 1] + averages[counter])

        counter += 1
        
    print(integral_h, integral_l, integral_a)

def main():
    high_array, low_array, average_array = sort_data()
    my_intg(high_array, low_array, average_array)

main()
