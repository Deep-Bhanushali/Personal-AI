import csv
import sqlite3

conn = sqlite3.connect('jarvis.db')
cursor = conn.cursor() 


# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()

# cursor.execute("UPDATE contacts set name='HETVI' where name='HETAVI'")
# cursor.execute("DELETE FROM contacts WHERE mobile_no='9224681115'")
conn.commit()
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# desired_columns = [0, 1]  # Columns to select: id, name, mobile_no

# with open('contacts.csv', 'r', encoding='utf-8') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns]
#         cursor.execute('INSERT INTO contacts (id,name,mobile_no) VALUES (null,?,?)', tuple(selected_data))

# conn.commit()
# conn.close()