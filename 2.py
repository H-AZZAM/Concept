Books_Name = [
    "Book H - 7",
    "Book A - 3",
    "Book N - 5",
    "Book A - 10",
    "Book H - 2",
    "Book A - 4",
    "Book N - 15",
    "Book A - 1"
]


books = {} #key (titles) - value (days)


for new_books in Books_Name:
    title, days = new_books.split(" - ") #"book H":9
    days = int(days) 
    if title in books:  
        books[title] += days 
    else:  
        books[title] = days 


most_borrowed = max(books, key=books.get)  
least_borrowed = min(books, key=books.get) 
average_days = sum(books.values()) / len(books)  
unique_titles = set(books.keys())  
sorted_books = sorted(books.items(), key=lambda x: x[1], reverse=True)  


print(f"Most borrowed book: {most_borrowed} - {books[most_borrowed]} days")
print(f"Least borrowed book: {least_borrowed} - {books[least_borrowed]} days")
print(f"Average borrowing time: {average_days:.2f} days")
print(f"Unique book titles: {unique_titles}")
print("Books sorted by borrowed days:")

for title, days in sorted_books:
    print(f"{title}: {days} days")