from datetime import datetime
from src.com.jalasoft.search_files.utils.logging import logger
from src.com.jalasoft.search_files.utils.search_utils import SearchUtil


class File(object):
    """
    This class allow us to set and get all the file, folder attributes
    """
    logger.info("File: Enter")
    search_util = SearchUtil()


    def set_file_folder_name(self, name):
        """
        This method set a file or folder name without path
        :param name: File or Folder name
        """
        logger.info("set_file_folder_name: Enter with name = %s" % name)
        self.name = name

    def get_file_folder_name(self):
        """
        This method get the file or folder name
        :return: <String> File or folder name
        """
        logger.info("get_file_folder_name: Enter")
        return self.name

    def set_path(self, path):
        """
        This method set the file and folder path
        :param path: File or folder path
        """
        logger.info("set_path: Enter with path")
        self.path = path

    def get_path(self):
        """
        This method  help us to get the file or folder path
        :return: File or folder path
        """
        logger.info("get_path: Enter")
        return self.path

    def set_size(self, size):
        """
        This method set the file and folder size
        :param size:Receives the file or folder size
        """
        logger.info("set_size: Enter with size = %s" % size)
        size_in_megas = size / 1048576
        new_size = round(size_in_megas, 2)
        self.size = new_size

    def get_size(self):
        """
        This method help us to get the file and folder size after perform operations to convert bytes on MB
        :return: The file and folder size on MB
        """
        # size_in_megas = self.size / 1048576
        # return round(size_in_megas, 2)
        logger.info("get_size: Enter")
        return self.size

    def set_is_file(self, flag):
        """
        This method set a flag True if the path is a file and False if the path is a folder
        :param flag: File path
        """
        logger.info("set_is_file: Enter wiht flag = %s" % flag)
        self.flag = flag

    def get_is_file(self):
        """
        This method return True if the path is a file and False if it's a folder
        :return: boolean values
        """
        logger.info("get_is_file: Enter")
        return self.flag

    def set_extension(self, extension):
        """
        This method set the file extension and set None if the path is a folder
        :param extension: File extension
        """
        logger.info("set_extension: Enter with extension = %s" % extension)
        self.extension = extension

    def get_extension(self):
        """
        This method help us to get the file extension
        :return: File extension or None if the path is a folder
        """
        logger.info("get_extension: Enter")
        return self.extension

    def set_date_created(self, date_created):
        """
        This method set the file and folder date creation
        :param date_created: The date when the folder or file were created
        """
        logger.info("set_date_created: Enter with date = %s" % date_created)
        self.date_created = self.search_util.convert_date(date_created)

    def get_date_created(self):
        """
        This method return the date when a file or folder were created
        :return: Date when a file or folder were created
        """
        logger.info("get_date_created: Enter")
        return self.date_created

    def set_date_modified(self, date_modified):
        """
        This method set the date when the file and folder were modified
        :param date_modified: Date when a file or folder were modified
        """
        logger.info("set_date_modified: Enter with date modified = %s" % date_modified)
        self.date_modified = self.search_util.convert_date(date_modified)

    def get_date_modified(self):
        """
        This method returns the date when a file or folder were modified
        :return: Date when the folder or file were modified
        """
        logger.info("get_date_modified: Enter")
        return self.date_modified

    def set_date_last_access(self, date_accessed):
        """
        This method set the last access date of a file or folder
        :param date_accessed: Date of last access to file or folder
        """
        logger.info("set_date_last_access: Enter with date last accessed = %s" % date_accessed)
        self.date_accessed = self.search_util.convert_date(date_accessed)

    def get_date_last_access(self):
        """
        The method get the last access date fo a file or folder
        :return: Date of last access to file ro folder
        """
        logger.info("get_date_access: Enter")
        return self.date_accessed

    def set_owner(self, owner):
        """
        This method set the file or folder owner
        :param owner: File or folder owner
        """
        logger.info("set_owner: Enter with owner = %s" % owner)
        self.owner = owner

    def get_owner(self):
        """
        This method returns the file or folder owner
        :return: File or folder owner
        """
        logger.info("get_owner: Enter")
        return self.owner
