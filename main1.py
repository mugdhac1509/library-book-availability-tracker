my_books = ["cat in the hat", "harry potter", "dork diaries", "percy jackson"]
copies = [2, 0, 5, 1]

library_dict = {b: c for b, c in zip(my_books, copies)}
print("library stock:", library_dict)

available_books = [b for b in my_books if library_dict[b] > 0]
print("available:", available_books)

choice = input("what book do you want? ")
if choice not in library_dict or library_dict[choice] == 0:
    print("sorry not available")
    exit()

fees = [2, 4, 3, 5]
extra = int(input("enter extra fee: "))
new_fees = list(map(lambda x: x + extra, fees))
print("fees:", new_fees)

idx = my_books.index(choice)
print("your fee is:", new_fees[idx])
library_dict[choice] = library_dict[choice] - 1
print("final library summary:", library_dict)