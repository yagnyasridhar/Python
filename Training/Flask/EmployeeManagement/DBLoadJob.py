import sqlite3
from sqlite3 import Error
import Employee

def sql_connection():
    try:
        con = sqlite3.connect('Employee.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    try:
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary integer, department text, position text, hireDate text)")
        con.commit()        
    except Error:
        print(Error)
    finally:
        con.close()

def sql_SelectAll(con):
    rows = None 
    try:   
        cursorObj = con.cursor()
        cursorObj.execute('Select * from employees')
        rows = cursorObj.fetchall()
        con.commit()
        cursorObj.close()
    except Error:
        print(Error)
    finally:
        con.close()
    return rows

def sql_SelectByName(con, name):
    rows = None 
    try:   
        cursorObj = con.cursor()
        stmt = ("Select * from employees where name in ('{0}')").format(name)
        print(stmt)
        cursorObj.execute(stmt)
        rows = cursorObj.fetchall()
        con.commit()
        cursorObj.close()
    except Error:
        print(Error)
    finally:
        con.close()
    return rows

def sql_insert(con, entities): 
    try:   
        cursorObj = con.cursor()    
        cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)    
        con.commit()
        cursorObj.close()
    except Error:
        print(Error)
    finally:
        con.close()

def sql_Insert(con, emp):  
    try:  
        cursorObj = con.cursor()    
        cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', emp)    
        con.commit()
        cursorObj.close()
    except Error:
        print(Error)
    finally:
        con.close()

def sql_bulkInsert(con, empLst):  
    try:  
        cursorObj = con.cursor()
        #print(empLst)
        cursorObj.executemany("INSERT INTO employees VALUES(?, ?, ?, ?, ?, ?)", empLst)
        con.commit()
        cursorObj.close()
    except Error:
        print(Error.__class__)
    finally:
        con.close()

def sql_update(con, empl):  
    try:  
        cursorObj = con.cursor()
        stmt = ("UPDATE employees SET name = '{1}', salary = {2}, department = '{3}', position = '{4}', hireDate = '{5}' where id = {0}").format(empl[0], empl[1], empl[2], empl[3], empl[4], empl[5])
        #print(stmt)
        cursorObj.execute(stmt)
        con.commit()
        cursorObj.close()
    except Error:
        print(Error)
    finally:
        con.close()

def sql_bulkUpdate(con, emplst): 
    try:   
        cursorObj = con.cursor()
        for empl in emplst:
            stmt = ("UPDATE employees SET name = '{1}', salary = {2}, department = '{3}', position = '{4}', hireDate = '{5}' where id = {0}").format(empl[0], empl[1], empl[2], empl[3], empl[4], empl[5])
            print(stmt)
            cursorObj.execute(stmt)
            con.commit()
        cursorObj.close()
    except Error:
        print(Error)
    finally:
        con.close()

def sql_delete(con,id):
    try:
        cursorObj = con.cursor()
        stmt = ("DELETE from  employees where id={0}").format(id)
        #print(stmt)
        cursorObj.execute(stmt)
        con.commit()
        cursorObj.close()
    except Error:
        print(Error)
    finally:
        con.close()

#con = sql_connection()
#sql_table(con)
#entities = (2, 'Sridhar', 2800000, 'IT', 'Tech', '2021-07-01')
#sql_insert(con, entities)
