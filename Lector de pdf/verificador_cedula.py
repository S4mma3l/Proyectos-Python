from pypdf import PdfReader


reader = PdfReader("Lector de pdf\LISTA_DE_DEVOLUCIONES_DIMEX.pdf")
len(reader.pages)
data = reader.metadata, reader.metadata.title
# print(data)
page = reader.pages[0]


def data(page):
    for page in reader.pages:
        print(page.extract_text())


result = data
print(result)
with open("Lector de pdf/datos.txt", "w") as f:
    f.write(str(data))
