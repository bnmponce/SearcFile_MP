class File:

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