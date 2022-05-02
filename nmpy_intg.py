#Sorts data in file and returns integral of data
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
    highs = np.array([], dtype = int)
    lows = np.array([], dtype = int)
    averages = np.array([], dtype = float)

    for date in range(total_days):
        highs = np.append(highs, all_data[date][1])
        lows = np.append(lows, all_data[date][2])
        averages = np.append(averages, all_data[date][3])

    return highs, lows, averages

def nmpy_int(highs, lows, averages):
#All have 8067 days, can use this list for them all
    days = range(len(highs))
    #Gets actual area using numpy.trapz()
    high_answer = np.trapz(highs, days)
    low_answer = np.trapz(lows, days)
    average_answer = np.trapz(averages, days)

    print(high_answer, low_answer, average_answer)

def main():
    high_array, low_array, average_array = sort_data()
    nmpy_int(high_array, low_array, average_array)

main()
