# import csv
#
# rows = [
#     ["first_name", "last_name", "email"],
#     ["Joe", "Smith", "joesmith@gmail.com"],
#     ["Rose", "Miller", "rosemiller@gamil.com"],
#     ["Kate", "William", "katewilliam@gamil.com"],
#     ["Adam", "Brown", "adambrown@gamil.com"],
#     ["Agatha", "Gracia", "agathagracia@gmail.com"],
#     ["Sharik", "Martinez", "sharikmartinez@gmail.com"]
# ]
# with open("names.csv", "w", newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerows(rows)
import csv
rows = [
    {"first_name": "Joe", "last_name": "Smith", "email": "joesmith@gmail.com"},
    {"first_name": "Rose", "last_name": "Miller", "email": "rosemiller@gamil.com"},
    {"first_name": "Kate", "last_name": "William", "email": "katewilliam@gamil.com"},
    {"first_name": "Adam", "last_name": "Brown", "email": "adambrown@gamil.com"},
    {"first_name": "Agatha", "last_name": "Gracia", "email": "agathagracia@gmail.com"},
    {"first_name": "Sharik", "last_name": "Martinez", "email": "sharikmartinez@gmail.com"}
]
with open("names.csv", "w", newline="") as csv_file:
    fieldnames = ["first_name", "last_name", "email"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerows(rows)


new_rows = [
    {"first_name": "Anna", "last_name": "Grayson", "email": "annagraysone@gmail.com"},
    {"first_name": "Antony", "last_name": "Clark", "email": "antonyclark@gmail.com"}
]

with open("names.csv", "a", newline="") as csv_file:
    fieldnames = ["first_name", "last_name", "email"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Don't write header again, just rows
    csv_writer.writerows(new_rows)
