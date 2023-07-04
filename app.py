import os
import config
import logging
import datetime
import ftpclient
from config import PARAMS

logging.basicConfig(filename='ftp-transfer.log', filemode='a', format='%(asctime)s - %(name)-20s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger("app")


# Main data
app_config = None


def get_file_to_transfer():    
    iso_date = datetime.date.today().strftime('%Y%m%d')            
    file = app_config[PARAMS.FILE_PATTERN.value]    
    file = file.replace("[yyyymmdd]", iso_date)
    file_path = os.path.join(app_config[PARAMS.LOCAL_FOLDER.value], file)    
    #Test if file exist
    if os.path.isfile(file_path):
        return file
    else:
        return None


# Defining main function
def main():
    logger.info("Application started")

    global app_config

    #Load configuration
    success, cfg = config.CONFIG().load()
    if (not success):
        logger.error("Cofiguracion no cargada. No se puede continuar")
        return    
    
    #Make config global
    app_config = cfg

    #Get file to transfer
    file_to_transfer = get_file_to_transfer()

    ftp = ftpclient.FTPCLIENT(app_config)
    ftp.transfer_file(file_to_transfer)
    
    logger.info("Application finished")

# Main
if __name__=="__main__":    
    main()