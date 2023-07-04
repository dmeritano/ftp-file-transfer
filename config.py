import json
import logging
from enum import Enum

#Global data
logger = logging.getLogger(__name__)
CONFIGURATION_FILE = 'appconfig.json'
class CONFIG:

    #App Keys
    FTP_HOST = ""


    def load(self):

        try:
            with open(CONFIGURATION_FILE, "r") as jsonfile:
                cfg = json.load(jsonfile)
                logger.info(f'Success loading configuration file {CONFIGURATION_FILE}: {cfg}')                
                return True, cfg
        except Exception as e:
            print("An exception occurred:", e)
            logger.error(f'Error loading configuration file {CONFIGURATION_FILE}, {e}')
            return False, None

        
        
        
class PARAMS(Enum):

    FTP_HOST = "ftphost"
    FTP_USER = "ftpuser"
    FTP_PASS = "ftppassword"
    FTP_FOLDER = "ftpfolder"
    LOCAL_FOLDER = "localfolder"
    FILE_PATTERN = "filepattern"