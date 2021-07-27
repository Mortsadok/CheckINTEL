import shutil
import DateTime


def Backupfiles():
    if DateTime.Day() != 'Friday' and DateTime.Day() != 'Saturday':
        shutil.copytree(r"C:\Users\ccduser\PycharmProjects\pythonProject\QualiCheck\Dependencies",
                        rf"C:\QualiCheck-Backup\{DateTime.Month()}\{DateTime.Date()}")


Backupfiles()
