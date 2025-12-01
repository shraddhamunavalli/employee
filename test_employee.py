from employee import employee_details
def test_employee_details():
    excepted_output = (
        "Employee Name: alice\n"
        "Employee ID: E1001\n"
        "Department: IT\n"
        "Salary: 55000"
    )
    assert employee_details("alice","E1001","IT",55000)== excepted_output
    
