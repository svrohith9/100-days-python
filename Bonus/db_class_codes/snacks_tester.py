# import the modules and classes
import sqlite3
from contextlib import closing

# connect to the database and set the row factory
conn = sqlite3.connect("snacks.db")
#conn.row_factory = sqlite3.Row

# execute a SELECT statement

with closing(conn.cursor()) as c:
    query = '''select city, count(*) as TotalTransactions, 
                   sum(quantity * unitprice) as CityTotal
                    from snacks
                    group by city
                    order by 3 desc'''
    c.execute(query)
    summary = c.fetchall()



# display the results

for row in summary:
    print(row[0], "|", row[1], "|", "{:,.2f}".format(row[2]))
print()


##
### execute an INSERT statement
##name = "A Fish Called Wanda"
##year = 1988
##minutes = 108
##categoryID = 1
##with closing(conn.cursor()) as c:
##    query = '''INSERT INTO Movie
##               (name, year, minutes, categoryID)
##               VALUES (?, ?, ?, ?)'''
##    c.execute(query, (name, year, minutes, categoryID))
##    conn.commit()
##print(name, "inserted.")
##
### execute an UPDATE statement
##minutes = 81
##with closing(conn.cursor()) as c:
##    query = '''UPDATE Movie
##               SET minutes = ?
##               WHERE name = ?'''
##    c.execute(query, (minutes, name))
##    conn.commit()
##print(name, "updated.")
##
### execute a DELETE statement
##with closing(conn.cursor()) as c:
##    query =  '''DELETE FROM Movie
##                WHERE name = ?'''
##    c.execute(query, (name,))
##    conn.commit()
##print(name, "deleted.")
