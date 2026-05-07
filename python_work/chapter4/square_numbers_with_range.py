squares = []
for value in range(1,11):
    #square = value ** 2
    squares.append(value ** 2)

print(squares)

#Advance code to square
squares = [value ** 2 for value in range(1,10000000)]
print(squares)