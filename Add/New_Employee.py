import ast


def EmployeeCheck(Values):
    Value = open(r'..\Dependencies\EmployeeCheck.txt', "w")
    Value.write(str(Values))
    Value.close()
    return Value


def EmployeeState(Values):
    Value = open(r'..\Dependencies\EmployeeState.txt', "w")
    Value.write(str(Values))
    Value.close()
    return Value


def Value_Is_Changed(Values):
    Value = open(r'..\Dependencies\Remembered_Values.txt', "w")
    Value.write(str(Values))
    Value.close()
    return Value


State = open(r'..\Dependencies\EmployeeState.txt', "r").read()
EState = ast.literal_eval(State)

Check = open(r'..\Dependencies\EmployeeCheck.txt', "r").read()
CState = ast.literal_eval(Check)

Values = open(r'..\Dependencies\Remembered_Values.txt', "r").read()
ENUM = ast.literal_eval(Values)

WWID_NEW = input('WWID?\n')

EState.update({str(WWID_NEW): '0'})
EmployeeState(EState)

CState.update({str(WWID_NEW): '0'})
EmployeeCheck(CState)

ENUM.update({str(WWID_NEW): '3'})
Value_Is_Changed(ENUM)

Firstname = input('New Employee Firstname?\n')
Lastname = input('New Employee Lastname?\n')
WWID = input('New Employee WWID?\n')
Phone = input('New Employee Phone?\n')
TeamLeader = input('New Employee Team Leader?\n')

with open("..\Dependencies\EmployeeDatabase.txt", "a") as AddEmployee:
    AddEmployee.write(f'\n{Firstname} {Lastname} {WWID} {Phone} {TeamLeader}')

print(f'Employee: {Firstname} {Lastname}\nAdded Successfully!\n')
