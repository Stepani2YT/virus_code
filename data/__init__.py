import pyautogui as pg
from os import system,mkdir,chdir
from multiprocessing import cpu_count
mkdir('logs')
chdir('logs')


def run(screenshot=True,WIA_LOGS=True,DISM_LOGS=True,WindowsUpdateLog=True,CBS_LOGS=True, processors_count=True):
    if screenshot == True:
        pg.screenshot('Desktop.png')
    if WIA_LOGS == True:
        system('@echo off')
        system('echo -----------------------WIA LOGS--------------------------- >> WIA_LOGS.TXT')
        system('echo -----------------------WIA LOGS--------------------------- >> ALL_LOGS.TXT')
        system('TYPE C:\windows\debug\WIA\wiatrace.log >> WIA_LOGS.TXT')
        system('TYPE C:\windows\debug\WIA\wiatrace.log >> ALL_LOGS.TXT')
    if DISM_LOGS == True:
        system('@echo off')
        system('echo -----------------------DISM LOGS--------------------------- >> DISM_LOGS.TXT')
        system('echo -----------------------DISM LOGS--------------------------- >> ALL_LOGS.TXT')
        system('TYPE C:\Windows\Logs\DISM\dism.log >> DISM_LOGS.TXT')
        system('TYPE C:\Windows\Logs\DISM\dism.log >> ALL_LOGS.TXT')
    if WindowsUpdateLog == True:
        system('@echo off')
        system('echo --------------------WindowsUpdateLog----------------------- >> ALL_LOGS.TXT')
        system('echo --------------------WindowsUpdateLog----------------------- >> WINDOWS_UPDATE_LOGS.TXT')
        system('powerShell Get-WindowsUpdateLog >> WINDOWS_UPDATE_LOGS.TXT')
        system('powerShell Get-WindowsUpdateLog >> ALL_LOGS.TXT')
    if CBS_LOGS == True:
        system('@echo off')
        system('echo -----------------------CBS LOGS---------------------------- >> ALL_LOGS.TXT')
        system('echo -----------------------CBS LOGS---------------------------- >> CBS_LOGS.TXT')
        system('TYPE C:\Windows\Logs\CBS\CBS.log >> ALL_LOGS.TXT')
        system('TYPE C:\Windows\Logs\CBS\CBS.log >> CBS_LOGS.TXT')
    if processors_count == True:
        cpu = cpu_count()
        open('cpus.txt', 'w').write(f'Processors count: {cpu}')
