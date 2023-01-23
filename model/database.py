import sqlite3

#  this command creates a connection
conn = sqlite3.connect('students.db')

c = conn.cursor()  # my cursor

# creates a table
c.execute("""CREATE TABLE students (
            Name TEXT,
            Age INTEGER,
            Pin Number REAL
    )""")

c.execute("INSERT INTO students VALUES ('Nathan Kim', 17, 1.9)") # inserts data into a table

all_students = [
    ('Max Wu', 16, 1.8),
    ('Drake Graham', 36, 1.7),
    ('Alex Lu', 16, 1.83),
    ('Bob', 16, 1.98)
]
c.executemany("INSERT INTO students VALUES (?, ?, ?)", all_students) #data inside the list will appear in the (?,?,?)

# selects the data
c.execute("SELECT * FROM students")
print(c.fetchall())

conn.commit() # commit

conn.close() # closes the connection and makes the file