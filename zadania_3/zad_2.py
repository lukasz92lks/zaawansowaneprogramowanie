from klasy_zad_2.student import Student
from klasy_zad_2.employee import Employee
from klasy_zad_2.library import Library
from klasy_zad_2.book import Book
from klasy_zad_2.order import Order


library1 = Library(
    "Warsaw", "Main Street", "00-001", "9:00-17:00", "123-456-789"
)
library2 = Library(
    "Katowice", "Second Street", "30-002", "10:00-18:00", "987-654-321"
)

book1 = Book(library1, "2020-01-01", "John", "Doe", 300)
book2 = Book(library2, "2021-02-02", "Jane", "Smith", 250)
book3 = Book(library1, "2019-03-03", "Alice", "Johnson", 400)
book4 = Book(library2, "2022-04-04", "Bob", "Brown", 150)
book5 = Book(library1, "2018-05-05", "Charlie", "Davis", 500)


employee1 = Employee(
    "Michael",
    "Scott",
    "2005-06-15",
    "1975-03-15",
    "Scranton",
    "Paper Street",
    "18540",
    "570-555-1234",
)
employee2 = Employee(
    "Pam",
    "Beesly",
    "2007-09-01",
    "1979-03-25",
    "Scranton",
    "Paper Street",
    "18540",
    "570-555-5678",
)
employee3 = Employee(
    "Jim",
    "Halpert",
    "2006-01-10",
    "1978-10-01",
    "Scranton",
    "Paper Street",
    "18540",
    "570-555-9012",
)


student1 = Student("Adam", [70, 80, 90])
student2 = Student("Anna", [40, 50, 60])
student3 = Student("Piotr", [85, 90, 95])


order1 = Order(employee1, student1, [book1, book2], "2023-01-15")
order2 = Order(employee2, student2, [book3, book4, book5], "2023-02-20")

print(order1)
print()
print(order2)
