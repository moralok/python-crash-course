import csv
import matplotlib.pyplot as plt
from datetime import datetime


file_name = 'chapter16/death_valley_2014.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取日期和最高气温
    dates, highs, lows = [], [], []
    for row in reader:
        try: 
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(row[0], 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式
plt.title("Daily high and low temperature - 2014\nDead Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Tmperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
# plt.savefig("chapter16/16-6.png")
