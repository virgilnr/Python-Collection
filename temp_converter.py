#Masukkan nilai celcius
celcius = float(input("Masukkan temperatur dalam satuan celcius: "))
print("\nPilihlah mode untuk mengonversi skala celcius:\n 1.Celcius ke Kelvin\n 2.Celcius ke Fahrenheit\n 3.Celcius ke Rankine\n 4.Celcius ke Delisle\n 5.Celcius ke Newton\n 6.Celcius ke Reamur\n 7.Celcius ke Romer\n")
converter = int(input("Pilih mode konversi (1-7): "))
#Konversi suhu celcius
kelvin = celcius + 273.15
fahrenheit = celcius * 1.8 +32
rankine = 1.8 * (celcius + 491.67)
delisle = (100 - celcius)* 1.5
newton = celcius * 33/100
reamur = celcius * 0.8
romer = celcius * 21/40 + 7.5
#Percabangan
if converter==1:
    print("Suhu " + str(celcius) + "°C setara dengan " + str(kelvin) + "K.")
elif converter==2:
    print("Suhu " + str(celcius) + "°C setara dengan " + str(fahrenheit) + "°F.")
elif converter==3:
    print("Suhu " + str(celcius) + "°C setara dengan " + str(rankine) + "°Ra.")
elif converter==4:
    print("Suhu " + str(celcius) + "°C setara dengan " + str(delisle) + "°De.")
elif converter==5:
    print("Suhu " + str(celcius) + "°C setara dengan " + str(newton) + "°N.")
elif converter==6:
    print("Suhu " + str(celcius) + "°C setara dengan " + str(reamur) + "°Ré.")
elif converter==7:
    print("Suhu " + str(celcius) + "°C setara dengan " + str(romer) + "°Rø.")
else:
    print("Mode yang dimasukkan tidak valid.")