import csv
import matplotlib.pyplot as plt

csv_file = open("country_vaccinations.csv")
reader = csv.reader(csv_file)

dataOfVaccine = dict()
header = 0
for row in reader:
    if row[3] != '' and row[4] != '':
        if(header == 0):
            header = 1
            continue
        if(row[0] in dataOfVaccine.keys()):
            dataOfVaccine[row[0]][0] += float(row[3])
            dataOfVaccine[row[0]][1] += float(row[4])
        else:
            dataOfVaccine[row[0]] = [float(row[3]), float(row[4])]

countryWithMaxDot = dict()
for _ in range(20):
    maxKey = max(dataOfVaccine, key=dataOfVaccine.get)
    countryWithMaxDot[maxKey] = dataOfVaccine[maxKey]
    dataOfVaccine.pop(maxKey)

plt.ylabel("Число вакцинированных на 1 млн")
plt.xlabel("Число доз")

country = list(countryWithMaxDot.keys())
vaccinePeople = list(int(i[1]/10**6) for i in  list(countryWithMaxDot.values()))
vaccineDot = list(int(i[1]/10**6) for i in list(countryWithMaxDot.values()))

print(f"{len(country)}: {len(vaccinePeople)}:{len(vaccineDot)}")

for cntry, vDot, vPeople in zip(country, vaccineDot, vaccinePeople):
  plt.annotate(cntry, xy = (vDot, vPeople),  xytext = (5,-5), textcoords = "offset points")

plt.scatter(vaccineDot, vaccinePeople)
plt.show()
print(list(int(i[1]/10**6) for i in  list(countryWithMaxDot.values())))
print(list(countryWithMaxDot.keys()))
