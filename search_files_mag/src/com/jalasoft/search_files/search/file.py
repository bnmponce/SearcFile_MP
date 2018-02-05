import time
from datetime import datetime

class File(object):

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def set_size(self, size):
        self.size = size

    def get_size(self):
        size_in_megas = self.size / 1048576
        return round(size_in_megas, 2)

    def set_is_file(self, flag):
        self.flag = flag

    def get_is_file(self):
        return self.flag

    def set_extension(self, extension):
        self.extension = extension

    def get_extension(self):
        return self.extension

    def set_date_created(self, date_created):
        self.date_created = self.convert_date(date_created)

    def get_date_created(self):
        return self.date_created

    def set_date_modified(self, date_modified):
        self.date_modified = date_modified

    def get_date_modified(self):
        return self.date_modified

    def set_date_accessed(self, date_accessed):
        self.data_accessed = date_accessed

    def get_date_accessed(self):
        return self.data_accessed

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def convert_date(self, date_in_float):
        """
        This method convert a date in float a string "%d-%b-%Y"; %d = day, %b = month and %Y = year
        :param date_in_float: date in float
        :return: return a date in string
        """
        time_in_date = time.gmtime(date_in_float)
        time_with_format = time.strftime("%m-%d-%Y", time_in_date)
        date_on_string = time_with_format.replace('-', '')
        date = datetime.strptime(date_on_string, '%m%d%Y')
        return date
