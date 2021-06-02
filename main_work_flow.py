import os
os.system("pip install google-api-python-client")
os.system("pip install oauth2client")
__path__ = [os.path.dirname(os.path.abspath(__file__))]
from .operations import *
from .log import info
from datetime import date


today = date.today().__str__()
autoPath = os.path.dirname(os.path.abspath(__file__))
logfile = "Gdrive_file_download_" + str(today) + ".log"
Gdrive_file_log_path = os.path.join(os.path.join(autoPath, logfile))
print('Gdrive_file_log_path', Gdrive_file_log_path)

@info
def frame_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s-%(module)s-%(name)s-%(levelname)s : %(message)s',
                                  datefmt='%d-%b-%y %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    '''create logging file handler and set level to debug'''
    handler = logging.FileHandler(Gdrive_file_log_path, "w")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s-%(module)s-%(name)s-%(levelname)s : %(message)s',
                                  datefmt='%d-%b-%y %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


@info
def main():
    print("################## START #####################")

    while True:
        option = input("""Please choose one option from following:
        1.  Enter File Name
        2.  Terminate programme
        """)

        if int(option) == 1:
            print("################ Enter File Name ##################")
            print('You have selected Enter File Name')
            file_name = input('Enter File Name: ')
            print('Entered file ID is: {} '.format(file_name))
            download(file_name)

        elif int(option) == 2:
            print("################## Terminate programme ####################")
            print("You have selected Terminate programme option \n")
            print('Programme Terminated')
            break

        else:
            print('Sorry, that was incorrect input')
            continue

if __name__ == '__main__':
    frame_logger()
    main()
