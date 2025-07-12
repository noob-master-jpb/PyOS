class definition:
    def __init__(self, name, **kwargs):
        
        if type(name) is not str:
            raise TypeError("Name must be a string.")
        
        if "struct" in kwargs and "type" in kwargs and "alternatives" in kwargs:
            raise ValueError("Cannot have both 'struct' and 'type' in the same definition.")
        
        if ("repeat" not in kwargs) and ("separator" not in kwargs):
            raise ValueError("repeat must be set to True for separator to be valid.")
        self.name = name
        
        self.struct = kwargs.get("struct", None)
        self.alternatives = kwargs.get("alternatives", None)
        self.type = kwargs.get("type", None)
        self.required = kwargs.get("required", False)
        self.repeat = kwargs.get("repeat", False)
        
        self.separator = kwargs.get("separator", None)
        self.keyword = kwargs.get("keyword", False)
        
        
    def stuct(self,stuct,):
        if self.type or self.alternatives:
            raise ValueError("Cannot set 'struct' when 'type' or 'alternatives' are defined.")
        self.struct = stuct
        
    def alternatives(self, alternatives):
        if self.type or self.struct:
            raise ValueError("Cannot set 'alternatives' when 'type' or 'struct' are defined.")
        self.alternatives = alternatives
        
    def type(self, type):
        if self.alternatives or self.struct:
            raise ValueError("Cannot set 'type' when 'alternatives' or 'struct' are defined.")
        self.type = type
        
    def required(self, required):
        if self.separator and not self.repeat:
            raise ValueError("repeat cannot be set to False if separator is set.")
        self.required = required
        
    def separator(self, separator):
        if self.repeat and not separator:
            raise ValueError("separator can only be set if repeat is True.")
        self.separator = separator
        
    def repeat(self, repeat):
        self.repeat = repeat
        
    def keyword(self, keyword):
        self.keyword = keyword
        
    def assign(self,**kwargs):
        """
        Needs to be improved in future versions.
        """
        if not kwargs:
            print("Warning: No arguments provided to assign.")
            return
        
        exclusive_keys = ["struct", "type", "alternatives"]
        present_keys = [key for key in exclusive_keys if key in kwargs]
        if len(present_keys) > 1:
            raise ValueError(f"Cannot have multiple exclusive keys: {present_keys}")
        
        if ("struct" in kwargs):
            if (self.type or self.alternatives):
                raise ValueError("Cannot set 'struct' when 'type' or 'alternatives' are already defined.")
            self.struct = kwargs["struct"]
            
        if ("alternatives" in kwargs): 
            if (self.type or self.struct):
                raise ValueError("Cannot set 'alternatives' when 'type' or 'struct' are already defined.")
            self.alternatives = kwargs["alternatives"]
            
        if ("type" in kwargs):
            if (self.alternatives or self.struct):
                raise ValueError("Cannot set 'type' when 'alternatives' or 'struct' are already defined.")
            self.type = kwargs["type"]
            
        if "required" in kwargs:
            self.required = kwargs["required"]

        if "repeat" in kwargs:
            self.repeat = kwargs["repeat"]            
            if self.repeat and not self.separator:
                raise ValueError("repeat cannot be set to False if separator is set.")
             
        if ("separator" in kwargs): 
            if not self.repeat:
                raise ValueError("separator can only be set if repeat is True.")
            self.separator = kwargs["separator"]

        if "keyword" in kwargs:
            self.keyword = kwargs["keyword"]
        

primitive_values = definition("primitive_values")


collection = definition("collection")


expression = definition("expression")
arithmrtic_expr = definition("arithmrtic_expr") 
conditional_expr = definition("conditional_expr")
comparison_expr = definition("comparison_expr")


template_call = definition("template_call")
template_args = definition("template_args")

f_string_value = definition("fstring")

value = definition("value")

assignment = definition("assignment")

assignment_target = definition("assignment_target")
simple_key = definition("simple_key")
typed_key = definition("typed_key")
f_string_key = definition("f_string_key")

assignment_value = definition("assignment_value")
simple_value = definition("simple_value")
typed_value = definition("typed_value")
function_call_value = definition("function_call_value")
comprehension_value = definition("comprehension_value")


function_header = definition("function_header")
function_name = definition("function_name")
param_list = definition("param_list")
param = definition("param")

property_def = definition("property_def")
property_name = definition("property_name")
property_value = definition("property_value")

