class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library in {self.city}, {self.street}, "
            f"{self.zip_code}, open hours: {self.open_hours}, "
            f"phone: {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone


def __str__(self):
    return (
        f"Employee: {self.first_name} {self.last_name}, "
        f"Hire Date: {self.hire_date}, "
        f"Birth Date: {self.birth_date}, "
        f"Address: {self.city}, {self.street}, "
        f"{self.zip_code}, Phone: {self.phone}"
    )


class Book:
    def __init__(
        self,
        library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages


def __str__(self):
    return (
        f"Book in {self.library}, "
        f"Publication Date: {self.publication_date}, "
        f"Author: {self.author_name} {self.author_surname}, "
        f"Number of Pages: {self.number_of_pages}"
    )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date


def __str__(self):
    books_list = "\n".join(str(book) for book in self.books)
    return (
        f"Order Date: {self.order_date}\n"
        f"{self.employee}\n"
        f"{self.student}\n"
        f"Books:\n{books_list}"
    )


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
