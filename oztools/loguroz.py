# developed by OZ
#
#
#
#
#
#
from __future__ import print_function

import os
from datetime import datetime


class Loguroz:
    """
    small loguru clone for easy logging

    """

    def __init__(self, path, max_size=100000, file_name='echodns.log'):
        """
        initialize logger

        params:
            path: [str] path location
            max_size: [int] max size of log before rebuild
            file_name: [str] name of log file

        """
        now = datetime.now()
        date = now.strftime("%Y%m%d_")
        self.path = os.path.join(path, 'logs')
        self.max_size = max_size
        self.file_name = date + file_name
        self.file_path = os.path.join(self.path, self.file_name)

        if not os.path.exists(self.path):
            os.makedirs(self.path)
        if not os.path.exists(self.file_path):
            # os.mknod(self.file_path)
            open(self.file_path, "w+")


    def check_size(self):
        """
        log file size monitoring

        """
        try:
            if os.path.getsize(self.file_path) > self.max_size:
                if os.path.exists(self.file_path + '.old.log'):
                    os.remove(self.file_path + '.old.log')
                os.rename(self.file_path, self.file_path + '.old.log')
                with open(self.file_path, 'w') as log_file:
                    print('{0}\tInfo\t\t[Logger] New Log started.'.format(self.time_now()), file=log_file)
        except Exception as e:
            print('{0}\tWarning\t\t[Logger] Could not delete old log.'.format(self.time_now()), file=log_file)



    def info(self, msg, ip='\t'):
        """
        log as information

        """
        self.check_size()
        with open(self.file_path, 'a') as log_file:
            print('{0}\tInfo\t\t{1}\t{2}'.format(self.time_now(), ip, msg), file=log_file)
        print('{0}\tInfo\t\t{1}\t{2}'.format(self.time_now(), ip, msg))

    def warning(self, msg, ip='\t'):
        """
        log as information

        """
        self.check_size()
        with open(self.file_path, 'a') as log_file:
            print('{0}\tWarning\t\t{1}\t{2}'.format(self.time_now(), ip, msg), file=log_file)
        print('{0}\tWarning\t\t{1}\t{2}'.format(self.time_now(), ip, msg))

    def time_now(self):
        """
        returns the current timestamp

        returns:
            time as [str]

        """
        now = datetime.now()
        current_time = now.strftime("%Y/%m/%d \t %H:%M:%S")
        return current_time
