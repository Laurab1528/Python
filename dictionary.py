class CustomDict():
    def __init__(self):

        self.dictionary = None or {}

    def newentry(self,key,value):
        self.key = key
        self.value = value

        if key in self.dictionary :
            print(f"key '{key}' already exist")

        else:
            self.dictionary[key]= value
        return self.dictionary
    
    def looks(self,key):
        
        if key in self.dictionary:

            return self.dictionary[key]
        else:
            print(f"can't find entry for '{key}")