numeri = [1,2,3,4,5,6,7,8,9,10]
n = 3
m = 2

# creiamo il primo range per la casistica di "1"
y = range(1,2)
for j in y:
  print(j)

  print("\n")

# creiamo il secondo range per la casistica di "2"
z = range(2,3)
for k in z:
   k = (k+(k-1))/m
   print(k)

print ("\n")
# creiamo il range per la casistica delle restanti medie "3 : 10"
x= range(3,11)
for i in x:
    i = (i+(i-1)+(i-2))/n
    print(i)

print("\n")