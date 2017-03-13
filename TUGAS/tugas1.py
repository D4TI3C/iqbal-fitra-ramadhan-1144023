import time
start_time = time.time()
print("Menghitung nilai rumus matematika menggunakan bahasa Hawaii")
i = raw_input("Masukan Nilai 1: ")
q = raw_input("Masukan Nilai 2: ")
b = raw_input("Masukan Nilai 3: ")
a = raw_input("Masukan Nilai 4: ")
l = raw_input("Masukan Nilai 5: ")

if i == 'kekahi':
	i=1

if i == 'elua':
	i=2

if i == 'ekolu':
	i=3

if i == 'eha':
	i=4

if i == 'elima':
	i=5

if i == 'eono':
	i=6

if i == 'ehiku':
	i=7

if i == 'ewalu':
	i=8

if i == 'eiwa':
	i=9

if i == 'ole':
	i=0

if q == 'kekahi':
	q=1

if q == 'elua':
	q=2

if q == 'ekolu':
	q=3

if q == 'eha':
	q=4

if q == 'elima':
	q=5

if q == 'eono':
	q=6

if q == 'ehiku':
	q=7

if q == 'ewalu':
	q=8

if q == 'eiwa':
	q=9

if q == 'ole':
	q=0
	
if b == 'kekahi':
	b=1

if b == 'elua':
	b=2

if b == 'ekolu':
	b=3

if b == 'eha':
	b=4

if b == 'elima':
	b=5

if b == 'eono':
	b=6

if b == 'ehiku':
	b=7

if b == 'ewalu':
	b=8

if b == 'eiwa':
	b=9

if b == 'ole':
	b=0
	
if a == 'kekahi':
	a=1

if a == 'elua':
	a=2

if a == 'ekolu':
	a=3

if a == 'eha':
	a=4

if a == 'elima':
	a=5

if a == 'eono':
	a=6

if a == 'ehiku':
	a=7

if a == 'ewalu':
	a=8

if a == 'eiwa':
	a=9

if a == 'ole':
	a=0
	
if l == 'kekahi':
	l=1

if l == 'elua':
	l=2

if l == 'ekolu':
	l=3

if l == 'eha':
	l=4

if l == 'elima':
	l=5

if l == 'eono':
	l=6

if l == 'ehiku':
	l=7

if l == 'ewalu':
	l=8

if l == 'eiwa':
	l=9

if l == 'ole':
	l=0
	
jumlah =(i*q)+(b/a-l) 
print ("hasil" , jumlah) 
print("time : %s detik " % (time.time() - start_time))