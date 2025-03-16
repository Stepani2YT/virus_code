try:
    from wget import download
    from os import system
except:
    print("EROOR")


def download_(url,filename, start_file=True):
    download(url, filename)
    if start_file == True:
        try:
            system('cls')
        except:
           system('clear')
        system(filename)