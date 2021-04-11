from flask import Flask, request, Response
import DBLoadJob
import Employee
import json

app = Flask("Employee Management")

'''
Home Page: This will return all employee details.
Return: JSON
'''
@app.route("/",methods=['GET'])
def home():
    con = DBLoadJob.sql_connection()
    emp = None
    rows = DBLoadJob.sql_SelectAll(con)
    empLst = []
    for row in rows:
        emp = Employee.Employee(row[0], row[1], row[2], row[3], row[4], row[5])
        empLst.append(emp)
    return json.dumps(empLst, indent=2, cls=Employee.EmployeeEncoder)

'''
Query Page: This will return all employee details for the specified name.
Return: JSON
'''
@app.route("/QueryByName/<string:name>",methods=['GET'])
def QueryByName(name):
    con = DBLoadJob.sql_connection()
    emp = None
    rows = DBLoadJob.sql_SelectByName(con,name)
    empLst = []
    for row in rows:
        emp = Employee.Employee(row[0], row[1], row[2], row[3], row[4], row[5])
        empLst.append(emp)
    return json.dumps(empLst, indent=2, cls=Employee.EmployeeEncoder)

'''
New Employee Page: This will create new employee.
Return: 201
'''
@app.route('/newEmployee', methods=['POST'])
def newEmployee():
    emp = json.loads(request.data)
    con = DBLoadJob.sql_connection()
    DBLoadJob.sql_Insert(con, tuple(emp.values()))
    return Response(status=201)

'''
Bulk Insert Employee Page: This will create new employee in bulk.
Return: 201
'''
@app.route('/bulkNewEmployee', methods=['POST'])
def bulkNewEmployee():
    empLst = json.loads(request.data)
    con = DBLoadJob.sql_connection()
    lst = []
    for emp in empLst:
        lst.append(list(emp.values()))
    DBLoadJob.sql_bulkInsert(con, lst)
    return Response(status=201)

'''
Update Employee Page: This will create update employee.
Return: 201
'''
@app.route('/updateEmployee', methods=['PUT'])
def updateEmployee():
    emp = json.loads(request.data)
    con = DBLoadJob.sql_connection()
    DBLoadJob.sql_update(con, tuple(emp.values()))
    return Response(status=201)

'''
Update Bulk Employee Page: This will update employee in bulk.
Return: 201
'''
@app.route('/updateBulkEmployee', methods=['PUT'])
def updateBulkEmployee():
    empLst = json.loads(request.data)
    con = DBLoadJob.sql_connection()
    lst = []
    for emp in empLst:
        lst.append(list(emp.values()))
    DBLoadJob.sql_bulkUpdate(con, lst)
    return Response(status=201)

'''
Delete Employee Page: This will delete employee.
Return: 201
'''
@app.route('/deleteEmployee', methods=['DELETE'])
def deleteEmployee():
    id = json.loads(request.data)
    con = DBLoadJob.sql_connection()
    DBLoadJob.sql_delete(con, id['id'])
    return Response(status=200)

if(__name__ == "__main__"):
    app.run(debug=True)