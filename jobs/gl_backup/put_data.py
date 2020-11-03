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
                target_file_path = os.path.abspath(os.path.join(parent,filename))
                break

    return target_filename, target_file_path


def put_data(date):

    filename, file_path = search(date)

    if filename is not None:
        try:
            ftp = FTP()
            print "Connecting ", X_LAB_FTP_HOST, X_LAB_FTP_PORT
            ftp.connect(X_LAB_FTP_HOST, X_LAB_FTP_PORT)
            ftp.login(X_LAB_FTP_USER, X_LAB_FTP_PWD.decode("base64"))
            ftp.cwd(GL_BACKUP_REMOTE_PATH)

            print "Uploading ", filename
            f = open(file_path, "rb")
            ftp.storbinary("STOR %s" % filename, f)
            f.close()

            ftp.quit()
        except:
            print "Failed to upload backup file: ", file_path


if __name__ == "__main__":
    # bash common/python.sh jobs/gl_backup/put_data.py date
    #
    # date 是要上傳的日期(預設是前一天)

    date = None

    if len(sys.argv) == 1:
            yesterday = datetime.now() - timedelta(days=1)
            date = datetime.strftime(yesterday, "%Y_%m_%d")
    elif len(sys.argv) == 2:
        date = sys.argv[2]

    put_data(date)
