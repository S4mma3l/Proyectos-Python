en esta prueba nos brindad 2 archivos:

static
ltdis.sh

este ultimo es un script de bash el cual cuando lo ejecutamos nos solicita un documento.

el comando seria de la siguiente manera:
./ltdis.sh static

el cual nos brinda tres archivos le hacemos una cat a el siguiente: static.ltdis.strings.txt

en el cual esta la flag pero para encontrarla de una vez podemos hacerlo de esta esta forma:
cat static.ltdis.strings.txt | grep pico
