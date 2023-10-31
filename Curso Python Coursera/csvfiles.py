#  CSV es comma separated values
import csv
f = open ("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    item, cantidad, descripcion, largo, ancho, espesor = row
    print ("item: {}, cantidad: {}, descripcion: {}, largo: {}, ancho: {}, espesor: {}".format(item, cantidad, descripcion, largo, ancho, espesor))

#  crear archivos CSV

host =[["workstation.local", "192.168.10.2"], ["webserver.cloud", "192.168.1.0"]]
with open ("host.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(host)

# leer y escribir archivos csv con diccionarios

with open("csv_file.csv") as software:
    reader = csv.DictReader (software)
    for row in reader:
        print(("{} has {} users").format(row["largo"]. row["ancho"]))
