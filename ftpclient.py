import ftplib
import logging
import os
from config import PARAMS

logger = logging.getLogger(__name__)

class FTPCLIENT:

    def __init__(self, app_config):
        self.app_config = app_config


    def transfer_file(self, file_to_transfer):

        try:

            logger.info(f'Uploading file: {file_to_transfer}')

            with ftplib.FTP(host=self.app_config[PARAMS.FTP_HOST.value], 
                            user=self.app_config[PARAMS.FTP_USER.value], passwd=self.app_config[PARAMS.FTP_PASS.value]) as ftp:    
                
                logger.info("Connected to FTP Server")

                status = ftp.getwelcome()
                for msg in status.split("\n"):
                    logger.info(f'Server status connected: {msg}')
                                
                remote = self.app_config[PARAMS.FTP_FOLDER.value]
                local = self.app_config[PARAMS.LOCAL_FOLDER.value]
                
                status = ftp.cwd(remote)
                for msg in status.split("\n"):
                    logger.info(f'Server status changing to remote dir "{remote}": {msg}')

                #Transfer file
                file_path = os.path.join(local, file_to_transfer)
                with open(file_path, 'rb') as file:
                    status = ftp.storbinary(f'STOR {file_to_transfer}', file)
                    for msg in status.split("\n"):
                        logger.info(f'Server status upload response: {msg}')                    
                    logger.info(f'Success uploading file {file_to_transfer} to FTP server')
            
            "Process ended"
            logger.info("Disconnected from FTP Server")
            return True
        
        except Exception as e:
            print(f"An exception occurred uploading file {file_to_transfer}:", e)
            logger.error(f'Error uploading file {file_to_transfer} to FTP server: {e}')
            return False

