from flask import Flask, request, jsonify

app = Flask(__name__)

# Create in-memory database as dictionaries
departments = {
    10: 'Admin',
    20: 'Accounts',
    30: 'Sales',
    40: 'Marketing',
    50: 'Purchasing'
}

employees = {
    1: {'ENO': 1, 'ENAME': 'Amal', 'DNO': 10, 'SALARY': 30000},
    2: {'ENO': 2, 'ENAME': 'Shyamal', 'DNO': 30, 'SALARY': 50000},
    3: {'ENO': 3, 'ENAME': 'Kamal', 'DNO': 40, 'SALARY': 10000},
    4: {'ENO': 4, 'ENAME': 'Nirmal', 'DNO': 50, 'SALARY': 60000},
    5: {'ENO': 5, 'ENAME': 'Bimal', 'DNO': 20, 'SALARY': 40000},
    6: {'ENO': 6, 'ENAME': 'Parimal', 'DNO': 10, 'SALARY': 20000}
}

@app.route('/api', methods=['GET'])
def get_employee_by_eno():
    try:
        eno = int(request.args.get('ENO'))
        if eno in employees:
            return jsonify(employees[eno])
        else:
            return jsonify({'message': 'Employee not found'}), 404
    except ValueError:
        return jsonify({'message': 'Invalid ENO format'}), 400

@app.route('/api/employees_by_dname', methods=['GET'])
def get_employees_by_dname():
    try:
        dname = request.args.get('DNAME')
        matching_employees = []

        for eno, employee in employees.items():
            if departments.get(employee['DNO']) == dname:
                matching_employees.append(employee)

        if matching_employees:
            return jsonify(matching_employees)
        else:
            return jsonify({'message': 'No employees found for the given department'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(port=9000)
