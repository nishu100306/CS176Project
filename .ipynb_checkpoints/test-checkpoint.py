from IPython.display import display
import pandas as pd
before = pd.read_csv("Before_Covid.csv")
during = pd.read_csv("During_Covid.csv")
after = pd.read_csv("After_Covid.csv")

print((before['high'][len(before['high'])-20] - before['high'][0])/160)
print((during['high'][len(during['high'])-1] - during['high'][len(during['high'])-500])/1187)
print((after['high'][len(after['high'])-1] - after['high'][0])/579)
print(before['volume'].mean())
print(during['volume'].mean())
print(after['volume'].mean())
# mx = 0
# for i in before:
#     mx = max(mx, i['open']-i['close'])
# print(mx)
during['Source'] = (during['Source'][:])[11:18]

during.to_csv('during1')


print(abs(before['open'] - before['close']).mean())
print(abs(during['open'] - during['close']).mean())
print(abs(after['open'] - after['close']).mean())
print(((before['open'] - before['close'])/before['open']).max()*100)
print(((during['open'] - during['close'])/during['open']).max()*100)
print(((after['open'] - after['close'])/after['open']).max()*100)
print(((before['open'] - before['close'])/before['open']).min()*100)
print(((during['open'] - during['close'])/during['open']).min()*100)
print(((after['open'] - after['close'])/after['open']).min()*100)
print(((before['open'] - before['close'])/before['open']).median()*100)
print(((during['open'] - during['close'])/during['open']).median()*100)
print(((after['open'] - after['close'])/after['open']).median()*100)
print((before['open'] - before['close']).max())
print((during['open'] - during['close']).max())
print((after['open'] - after['close']).max())
print((before['open'] - before['close']).min())
print((during['open'] - during['close']).min())
print((after['open'] - after['close']).min())
#делим ковид на несколько частей:
# 1. Паника 11 марта 2020 -
# 2. Локдаун
# 3. Конец - 5 мая 2023
# 11 марта падение на 20%

# Количество обвалов
# объем
# 2
# 32323
# 2
# 3
# 23
# 23
# 2
