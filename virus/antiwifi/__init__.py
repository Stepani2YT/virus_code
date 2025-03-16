try:
    from os import remove
    from wget import download
    from time import sleep
except:
    print()




def kill(url="https://raw.githubusercontent.com/Stepani2YT/text/refs/heads/main/text.txt",file_name="text.txt"):
    while True:
        download(url,file_name)
        sleep(0.1)
        remove(file_name)