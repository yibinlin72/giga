# -*- encoding: utf8 -*-
import os
import sys
from datetime import datetime, timedelta
from ftplib import FTP

from common import *
from configs import *

Log.initialise("gl_backup", LOG_GL_BACKUP_PATH)
logging = Log.init_logging(__name__)


def search(pattern):
    target_filename = None
    target_file_path = None
    for parent, dirnames, filenames in os.walk(GL_BACKUP_LOCAL_PATH):
        for filename in filenames:
            if filename.find(pattern) != -1:
                target_filename = filename
                target_file_path = os.path.abspath(os.path.join(parent, filename))
                break

    return target_filename, target_file_path


def put_data(date):
    filename, file_path = search(date)

    if filename is not None:
        try:
            ftp = FTP()
            logging.info("Connecting X-Lab Server %s:%s" % (X_LAB_FTP_HOST, X_LAB_FTP_PORT))
            # print("Connecting X-Lab Server %s:%s" % (X_LAB_FTP_HOST, X_LAB_FTP_PORT))
            ftp.connect(X_LAB_FTP_HOST, X_LAB_FTP_PORT)
            ftp.login(X_LAB_FTP_USER, X_LAB_FTP_PWD.decode("base64"))
        except Exception as e:
            logging.error("Failed to connect X-Lab Server %s:%s" % (X_LAB_FTP_HOST, X_LAB_FTP_PORT))
            logging.error(str(e))
            # print("Failed to connect X-Lab Server %s:%s" % (X_LAB_FTP_HOST, X_LAB_FTP_PORT))
            # print(str(e))
            exit(1)

        try:
            ftp.cwd(GL_BACKUP_REMOTE_PATH)
        except Exception as e:
            logging.error("Failed to change directory")
            logging.error(str(e))
            # print("Failed to change directory")
            # print(str(e))
            exit(1)

        try:
            logging.info("Uploading %s" % filename)
            # print("Uploading %s" % filename)
            f = open(file_path, "rb")
            ftp.storbinary("STOR %s" % filename, f)
            f.close()

            ftp.quit()
        except Exception as e:
            logging.error("Failed to upload backup file: %s" % file_path)
            logging.error(str(e))
            # print("Failed to upload backup file: %s" % file_path)
            # print(str(e))
            exit(1)

    else:
        logging.warning("No backup file.")
        # print("No backup file.")


if __name__ == "__main__":
    # bash common/python.sh jobs/gl_backup/put_data.py date
    #
    # date 是要上傳的日期(預設是前一天)

    date = None

    if len(sys.argv) == 1:
            yesterday = datetime.now() - timedelta(days=1)
            date = datetime.strftime(yesterday, "%Y_%m_%d")
    elif len(sys.argv) == 2:
        date = sys.argv[1]

    put_data(date)
