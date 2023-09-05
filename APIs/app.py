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

# API endpoint for retrieving employee details by ENO or DNAME.
@app.route('/api', methods=['GET'])
def get_employee_details():
    try:
        eno = request.args.get('ENO')
        dname = request.args.get('DNAME')

        if eno is not None:
            # If 'ENO' is provided, attempt to convert it to an integer.
            eno = int(eno)

            if eno in employees:
                # If the employee exists, return their details as a JSON response.
                return jsonify(employees[eno])
            else:
                # If the employee is not found, return a 404 response with a message.
                return jsonify({'message': 'Employee not found'}), 404

        elif dname is not None:
            # If 'DNAME' is provided, search for employees in the specified department.
            matching_employees = []

            for eno, employee in employees.items():
                if departments.get(employee['DNO']) == dname:
                    matching_employees.append(employee)

            if matching_employees:
                # If matching employees are found, return them as a JSON response.
                return jsonify(matching_employees)
            else:
                # If no employees are found for the given department, return a 404 response with a message.
                return jsonify({'message': 'No employees found for the given department'}), 404

        else:
            # If neither 'ENO' nor 'DNAME' is provided, return a 400 response with an error message.
            return jsonify({'message': 'Invalid request'}), 400

    except ValueError:
        # Handle the case where 'ENO' is provided but is not a valid integer.
        return jsonify({'message': 'Invalid ENO format'}), 400
    except Exception as e:
        # Handle unexpected errors and return a 500 response with an error message.
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(port=9000)        #runs on port 9000
