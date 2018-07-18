list_total_x = []
list_total_y = []
list_total_plus_xy = []
list_total_minus_xy = []

eight_queens = [[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]

for i in eight_queens:
    list_total_x.append(i[0])
    list_total_y.append(i[1]) 
    list_total_plus_xy.append(i[0] + i[1])
    list_total_minus_xy.append(i[0] - i[1])

set(list_total_x)
set(list_total_y)
set(list_total_plus_xy)
set(list_total_minus_xy)

if len(set(list_total_x)) == 8 \
    and len(set(list_total_y)) == 8 \
    and len(set(list_total_plus_xy)) == 8 \
    and len(set(list_total_minus_xy)) == 8:
    print(True)
else:
    print(False)


