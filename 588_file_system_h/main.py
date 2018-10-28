class FileSystem(object):

    def __init__(self):
        self.sub_dir = collections.defaultdict(set)
        self.content = collections.defaultdict(lambda :"")
        self.is_file = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if self.is_file.get(path, False):
            file_name = path[path.rfind("/") + 1:]
            return [file_name]
        folders = self.sub_dir[path]
        return sorted(folders)
        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        self.mk_dir_file(path, False)


    # Still needs to differentiate file and folder
    def mk_dir_file(self, path, is_file):
        # path does not end with / and starts with /
        segs = path.split("/")
        for l in range(1, len(segs)):
            # Careful here
            parent_path = "/".join(segs[:l]) if l > 1 else "/"
            folder = segs[l]
            self.sub_dir[parent_path].add(folder)
        if is_file:
            self.is_file[path] = True

            
    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        self.mk_dir_file(filePath, True)
        self.content[filePath] += content
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.content[filePath]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)


# Careful places. 
# Root folder can be thought as ""
# path of root, "/".join([""]) return ""

# For file, needs to return itself. So just storing sub_dir is not enough. 