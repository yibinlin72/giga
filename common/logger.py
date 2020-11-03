# -*- coding: utf-8 -*-
import logging
import os
import sys

from configs import LOG_ROOT


def touch(file_nm, times=None):
    with open(file_nm, 'a'):
        os.utime(file_nm, times)


class Log(object):
    __logging = None
    log_format = "%(asctime)s %(main_name)s %(basename)s %(levelname)s : %(message)s"

    @staticmethod
    def initialise(name, filename, level=logging.INFO, max_bytes=65536000, backup_count=3):
        if Log.__logging is not None:
            return

        formatter = logging.Formatter(Log.log_format)
        Log.__logging = logging.getLogger(name)
        Log.__logging.setLevel(level)
        Log.__logging.propagate = True

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        Log.__logging.addHandler(console_handler)

        py4j_logger = logging.getLogger('py4j.java_gateway')
        logging._acquireLock()
        try:
            py4j_logger.setLevel(logging.WARN)
            # py4j_logger.addHandler(file_handler)
        except Exception:
            pass
        finally:
            logging._releaseLock()

    @staticmethod
    def init_logging(module_name):
        basename = os.path.basename(os.path.abspath(module_name))
        main_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]

        extra = {
            'main_name': main_name,
            'basename': basename
        }
        if Log.__logging is None:
            Log.initialise("default_log", "%s/default.log" % LOG_ROOT)
        return logging.LoggerAdapter(logger=Log.__logging, extra=extra)
