from datetime import datetime
from src.com.jalasoft.search_files.utils.logging import logger


class SearchUtil():


    def convert_date(self, date_in_float):
        """
        This method convert a date in float a string "%d-%b-%Y"; %d = day, %b = month and %Y = year
        :param date_in_float: date in float
        :return: return a date in string
        """
        logger.info("convert_date: Enter with date to convert %s" % date_in_float)
        time_in_date = datetime.fromtimestamp(date_in_float)
        date = datetime.strftime(time_in_date, '%m%d%Y')
        logger.info("convert_date: Exit > Returning date %s" % date)
        return date

