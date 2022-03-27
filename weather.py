
##Takes in daily Little Rock area temperatures from 2000 to 2022, graphs, and gets major temp events.
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Opens text file, sorts day data line by line into array, sorts array into huge array
def sort_data():
    all_data = []
    with open("/home/julia/Textfiles/temp_data.txt", 'r') as file:
        next(file)
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

    return all_data, highs, lows, averages, dates

#Gets record high and lows
def get_records(highs, lows, dates):
    
    #Lowest, highest temp
    lowest_low = 0
    highest_high = 0
    #Day/s the lowest low and highest high occured
    hh_day = 0
    ll_day = 0
    #Variable for date format from dates
    ll_date = []
    hh_date = []

    for high in highs:
        if high > highest_high:
            highest_high = high

    hh_day = np.argwhere(highs == highest_high)

    for low in lows:
        if low < lowest_low:
            lowest_low = low

    ll_day = np.argwhere(lows == lowest_low)

    #Find proper date format
    for array in ll_day:
        for day in array:
            ll_date.append(dates[day])
    for array in hh_day:
        for day in array:
            hh_date.append(dates[day])

    return lowest_low, ll_date, highest_high, hh_date

#Get's yearly highs and lows
def get_yearly_records(highs, lows, dates):

    #Substitute variables, will loop through highs and lows and get rid of 50 value (will be higher than 50 and lower than 50 for all years)
    h = 50
    l = 50
    yearly_records = dict({2000: [h, l], 2001: [h, l], 2002: [h, l], 2003: [h, l], 2004: [h, l], 2005: [h, l], 2006: [h, l], 2007: [h, l], 2008: [h, l], 2009: [h, l], 2010: [h, l], 2011: [h, l], 2012: [h, l], 2013: [h, l], 2014: [h, l], 2015: [h, l], 2016: [h, l], 2017: [h, l], 2018: [h, l], 2019: [h, l], 2020: [h, l], 2021: [h, l], 2022: [h, l]})

    #Leap years: 2000, 2004, 2008, 2012, 2016, 2020 (has 366 days, not 365)
    counter = 0
    year = 2000
    
    while counter < len(dates):

        if year % 4 == 0:
            counter2 = 1
        else:
            counter2 = 0
        if year == 2022:
            counter1 = 31 #Only Jan. data in 2022
        else:
            counter1 = 365
            
        for value in range(counter, (counter + counter1 + counter2)):
            if highs[value] > yearly_records[year][0]:
                yearly_records[year][0] = highs[value]
            if lows[value] < yearly_records[year][1]:
                yearly_records[year][1] = lows[value]
        counter = counter + counter1 + counter2
        year += 1
            
    return yearly_records

def graph_highs_lows(yearly_records, record_high, record_low, highs, lows):
    #Split up data so can graph it
    x_axis = list(dict.keys(yearly_records))

    #Exclude 2022, since not complete
    x_axis.remove(2022) 

    series1 = []
    series2 = []
    for year in yearly_records:
        if year == 2022:
            break
        else:
            series1.append(yearly_records[year][0])
            series2.append(yearly_records[year][1])

    #High plot
    fig1,ax1 = plt.subplots()
    ax1.scatter(x_axis, series1, label = "Yearly Highs", color = "red")
    ax1.legend()
    ax1.set_title("Record Yearly Highs")
    ax1.set_xlabel("Years, 2000 - 2021")
    ax1.set_xticks(np.arange(2000, 2021, 2))
    ax1.set_ylabel("Temperature in Farenheit")
    fig1.savefig("Highs.png")

    #Low plot
    fig2, ax2 = plt.subplots()
    ax2.scatter(x_axis, series2, label = "Yearly Lows", color = "blue")
    ax2.set_title("Record Yearly Lows")
    ax2.set_xlabel("Years, 2000 - 2021")
    ax2.set_xticks(np.arange(2000,2021, 2))
    ax2.set_ylabel("Temperature in Farenheit")
    fig2.savefig("Lows.png")
    
def graph_averages(averages, dates):

    #Graphs averages over 2000 - Jan. 2022
    fig3, ax3 = plt.subplots()
    ax3.plot(range(0, len(dates)), averages, color = "orange")
    ax3.set_title("Daily Averages from 2000 - Jan, 2022")
    ax3.set_xlabel("Days, from Jan 1st, 2000 - Jan 31st, 2022") 
    ax3.set_ylabel("Temperature in Farenheit")
    fig3.savefig("Averages.png")
    

#Executes all functions
def main():
    day_array, high_array, low_array, average_array, date_array = sort_data()    
    record_low, low_date, record_high, high_date = get_records(high_array, low_array, date_array)
    year_records = get_yearly_records(high_array, low_array, date_array)
    records_graph = graph_highs_lows(year_records, record_high, record_low, high_array, low_array)
    average_graph = graph_averages(average_array, date_array)

#Swings the axe, executes main()
main()

