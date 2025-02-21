import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    highs = []
    for row in reader:
        temp = int(row[1])
        highs.append((temp - 32) * 5/9)

    print(highs)

    # plot data
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(highs, c='red')

    # Format plot
    plt.title("Dayly high temperature, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temerature (C)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()