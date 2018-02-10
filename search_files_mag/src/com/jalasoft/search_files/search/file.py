from datetime import datetime

class File(object):
    """
    This class allow us to set and get all the file, folder attributes
    """
    def set_file_folder_name(self, name):
        """
        This method set a file or folder name without path
        :param name: File or Folder name
        """
        self.name = name

    def get_file_folder_name(self):
        """
        This method get the file or folder name
        :return: <String> File or folder name
        """
        return self.name

    def set_path(self, path):
        """
        This method set the file and folder path
        :param path: File or folder path
        """
        self.path = path

    def get_path(self):
        """
        This method  help us to get the file or folder path
        :return: File or folder path
        """
        return self.path

    def set_size(self, size):
        """
        This method set the file and folder size
        :param size:Receives the file or folder size
        """
        self.size = size

    def get_size(self):
        """
        This method help us to get the file and folder size after perform operations to convert bytes on MB
        :return: The file and folder size on MB
        """
        size_in_megas = self.size / 1048576
        return round(size_in_megas, 2)

    def set_is_file(self, flag):
        """
        This method set a flag True if the path is a file and False if the path is a folder
        :param flag: File path
        """
        self.flag = flag

    def get_is_file(self):
        """
        This method return True if the path is a file and False if it's a folder
        :return: boolean values
        """
        return self.flag

    def set_extension(self, extension):
        """
        This method set the file extension and set None if the path is a folder
        :param extension: File extension
        """
        self.extension = extension

    def get_extension(self):
        """
        This method help us to get the file extension
        :return: File extension or None if the path is a folder
        """
        return self.extension

    def set_date_created(self, date_created):
        """
        This method set the file and folder date creation
        :param date_created: The date when the folder or file were created
        """
        self.date_created = self.convert_date(date_created)

    def get_date_created(self):
        """
        This method return the date when a file or folder were created
        :return: Date when a file or folder were created
        """
        return self.date_created

    def set_date_modified(self, date_modified):
        """
        This method set the date when the file and folder were modified
        :param date_modified: Date when a file or folder were modified
        """
        self.date_modified = self.convert_date(date_modified)

    def get_date_modified(self):
        """
        This method returns the date when a file or folder were modified
        :return: Date when the folder or file were modified
        """
        return self.date_modified

    def set_date_last_access(self, date_accessed):
        """
        This method set the last access date of a file or folder
        :param date_accessed: Date of last access to file or folder
        """
        self.date_accessed = self.convert_date(date_accessed)

    def get_date_last_access(self):
        """
        The method get the last access date fo a file or folder
        :return: Date of last access to file ro folder
        """
        return self.date_accessed

    def set_owner(self, owner):
        """
        This method set the file or folder owner
        :param owner: File or folder owner
        """
        self.owner = owner

    def get_owner(self):
        """
        This method returns the file or folder owner
        :return: File or folder owner
        """
        return self.owner

    def convert_date(self, date_in_float):
        """
        This method convert a date in float a string "%d-%b-%Y"; %d = day, %b = month and %Y = year
        :param date_in_float: date in float
        :return: return a date in string
        """
        time_in_date = datetime.fromtimestamp(date_in_float)
        date = datetime.strftime(time_in_date, '%m%d%Y')
        return date
