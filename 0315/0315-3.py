# # with open('sitka_weather_07-2021_simple.csv') as f:
# #     for line in f:
# #         print(line.rstrip().split(sep=','))

# # import os
# # os.path
# import datetime
# from datetime import datetime as dt

# today = dt.strptime('2024-03-15', '%Y-%m-%d')
# print(today, type(today), type('2024-03-15'))

# # print(today + datetime.timedelta(days=3))

# # today = dt.now()
# # print(datetime)
# import csv
# from matplotlib import pyplot as plt

# from pathlib import Path

# COL_DATE = 2
# COL_TMAX = 4
# x1, y1 = [], []
# x2, y2 = [], []

# with open(Path('data', 'sitka_weather_07-2021_simple.csv')) as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     for line in reader :
#         # print(line, type(line))
        
#         x1.append(line[COL_DATE])
#         y1.append(line[COL_TMAX])
        
#         x2.append(line[2])
#         y2.append(line[5])
# # print(f'x:{x1}')
# # print(f'y:{y1}')
# # plt.title('TMAX')
# for idx, h in enumerate(header):
#     print(idx, h)

# plt.plot(x1, y1, label='TMAX')
# plt.plot(x2, y2, label='TMIN')
# plt.fill_between(x1, y1, y2, alpha=0.1)
# plt.legend
# plt.show()


try:
    with open('sitka_weather_2021_full.csv', 'r') as f:
        for line in f:
            print(line)
except Exception as e : 
    pass
#print(e)