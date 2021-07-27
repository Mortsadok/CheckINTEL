import os
import subprocess
from CheckSoftware import DateTime
from Save import Password


def Status(WWID, Status):
    Ip = ''
    Username = ''

    Info = f'C:\PSTools\PsExec.exe \\\\{Ip} -u {Username} -p {Password} -s cmd.exe /c "cd C:\\Users\\ccduser\\PycharmProjects\\pythonProject\\QualiCheck\\Status & C:\\Users\\ccduser\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe Employee_Status.py {WWID} {Status}"  > nul 2>&1'

    EmployeeStatus = os.popen(Info).read()

    return EmployeeStatus


def ManualEntry(WWID, CheckIn):
    Ip = ''
    Username = ''

    Info = f'C:\PSTools\PsExec.exe \\\\{Ip} -u {Username} -p {Password} -s cmd.exe /c "cd C:\\Users\\ccduser\\PycharmProjects\\pythonProject\\QualiCheck\\Status & C:\\Users\\ccduser\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe Manual_Entry.py {WWID} {CheckIn}" > nul 2>&1'

    EmployeeStatus = os.popen(Info).read()

    return EmployeeStatus


def Excel_Host():
    Go = NewFolder()

    Machine = ''
    with open(r'C:\Users\mtsadokx\PycharmProjects\pythonProject\CheckSoftware\Local\HostExcel.bat', 'w') as file:
        file.write(
            rf'net use \\{Machine}\c$\Users\ccduser\PycharmProjects\pythonProject\QualiCheck\Dependencies Check$giga /user:ger\ccduser' + '\n')
        file.write(
            rf'copy \\{Machine}\c$\Users\ccduser\PycharmProjects\pythonProject\QualiCheck\Dependencies\ "C:\Users\mtsadokx\PycharmProjects\pythonProject\CheckSoftware\Local\Backups\{DateTime.Date()}" > nul 2>&1')
        file.close()

    try:
        if Go is True:
            subprocess.call([r'C:\Users\mtsadokx\PycharmProjects\pythonProject\CheckSoftware\Local\HostExcel.bat'],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)
            print('Dependencies files copied Successfully!')

    except Exception as e:
        print(e)


def NewFolder():
    try:
        path = fr'C:\Users\mtsadokx\PycharmProjects\pythonProject\CheckSoftware\Local\Backups\{DateTime.Date()}'
        os.mkdir(path)
        return True

    except FileExistsError:
        print('The folder already exist!')
        return False

# Status('WWID', 'Reason')
# ManualEntry('WWID', 'Time')
# Excel_Host()
