class FileMaster():
    """
    This kata requires you to write an object that receives a file path and does operations on it
    Example: 
        master = FileMaster('/Users/person1/Pictures/house.png')
        master.extension() -> 'png'
        master.filename() -> 'house'
        master.dirpath() -> '/Users/person1/Pictures/'
    """
    def __init__(self, filepath):
        self.filepath = filepath
        
    def extension(self):
        return self.filepath.split("/")[-1].split(".")[-1]
        
    def filename(self):
        return self.filepath.split("/")[-1].split(".")[-2]
        
    def dirpath(self):
        return "/".join(self.filepath.split("/")[:-1]) + "/"
