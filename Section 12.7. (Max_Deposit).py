money = int(input("Введите сумму для вклада на депозит "))

per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
percent_list = list(per_cent.values())

deposit = [i*money*0.01 for i in percent_list]
deposit = list(map(round, deposit))

# print(deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))