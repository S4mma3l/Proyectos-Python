identify -verbose cat.jpg


sudo apt-get install bsdmainutils
hexdump -C cat.jpg | head

sudo apt install binwalk
binwalk cat.jpg 

sudo apt install gwenview
gthumb cat.jpg

cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9

echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d

picoCTF{the_m3tadata_1s_modified}
