import csv
with open('AQI_20180717095248.csv', 'r', encoding='utf-8-sig') as i:
    reader = csv.reader(i)
    init=int(50)
    for row in reader:
        if row[2] == 'AQI':
            pass

        else:
            if int(row[2])< int(init):
                init = row[2]
                place = row[1]
                location = row[0]
    print(place,location,init)

        