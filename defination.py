class definition:
    def __init__(self, name, **kwargs):
        
        if type(name) is not str:
            raise TypeError("Name must be a string.")
        
        if "struc" in kwargs and "type" in kwargs:
            raise ValueError("Cannot have both 'struc' and 'type' in the same definition.")
        
        self.name = name
        
        self.struc = kwargs.get("struc", None)
        self.alternative = kwargs.get("alternative", None)
        self.type = kwargs.get("type", None)
        self.required = kwargs.get("required", False)
        self.separator = kwargs.get("separator", None)
        self.repeat = kwargs.get("repeat", False)
        self.keyword = kwargs.get("keyword", None)
