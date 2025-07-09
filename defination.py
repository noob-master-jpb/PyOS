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
        self.required = required
        
    def separator(self, separator):
        self.separator = separator
        
    def repeat(self, repeat):
        self.repeat = repeat
        
    def keyword(self, keyword):
        self.keyword = keyword
        
    def assign(self,**kwargs):
        
        # Check for mutual exclusivity
        exclusive_keys = ["struct", "type", "alternatives"]
        present_keys = [key for key in exclusive_keys if key in kwargs]
        if len(present_keys) > 1:
            raise ValueError(f"Cannot have multiple exclusive keys: {present_keys}")
        
        if ("struct" in kwargs) and not (self.type or self.alternatives):
            self.struct = kwargs["struct"]
        elif "struct" in kwargs:
            raise ValueError("Cannot set 'struct' when 'type' or 'alternatives' are already defined.")
            
        if ("alternatives" in kwargs) and not (self.type or self.struct):
            self.alternatives = kwargs["alternatives"]
        elif "alternatives" in kwargs:
            raise ValueError("Cannot set 'alternatives' when 'type' or 'struct' are already defined.")
            
        if ("type" in kwargs) and not (self.alternatives or self.struct):
            self.type = kwargs["type"]
        elif "type" in kwargs:
            raise ValueError("Cannot set 'type' when 'alternatives' or 'struct' are already defined.")
            
        if "required" in kwargs:
            self.required = kwargs["required"]

        if "repeat" in kwargs:
            self.repeat = kwargs["repeat"]            
            if self.repeat and not self.separator:
                raise ValueError("repeat cannot be set to False if separator is set.")
             
        if ("separator" in kwargs) and self.repeat:
            self.separator = kwargs["separator"]
        else:
            raise ValueError("separator can only be set if repeat is True.")

        if "keyword" in kwargs:
            self.keyword = kwargs["keyword"]
        

def create_grammar():
    """Create the complete PyOS grammar with object references"""
    
    # Step 1: Create all definition objects first (empty)
    defs = {}
    
    # Create all the definitions from parser.py
    definition_names = [
        "value", "primitive_value", "collection_value", "expression_value",
        "template_call", "f_string_value", "list_value", "tuple_value", 
        "dict_value", "value_list", "dict_items", "dict_item", 
        "arithmetic_expr", "comparison_expr", "conditional_expr",
        "comprehension_expr", "arithmetic_op", "comparison_op",
        "iterable", "range_call", "template_args"
    ]
    
    for name in definition_names:
        defs[name] = definition(name)
    
    # Step 2: Link them together with actual object references
    
    # Main value definition
    defs["value"].alternatives = [
        defs["primitive_value"],
        defs["collection_value"], 
        defs["expression_value"],
        defs["template_call"],
        defs["f_string_value"]
    ]
    
    # Primitive values
    defs["primitive_value"].alternatives = ["STRING", "INT", "FLOAT", "ID"]
    
    # Collection values
    defs["collection_value"].alternatives = [
        defs["list_value"], 
        defs["tuple_value"], 
        defs["dict_value"]
    ]
    
    # List value
    defs["list_value"].struct = ["LBRACKET", defs["value_list"], "RBRACKET"]
    
    # Tuple value
    defs["tuple_value"].struct = ["LPAREN", defs["value_list"], "RPAREN"]
    
    # Dict value
    defs["dict_value"].struct = ["LBRACE", defs["dict_items"], "RBRACE"]
    
    # Value list (used by both lists and tuples)
    defs["value_list"].struct = [defs["value"]]
    defs["value_list"].repeat = True
    defs["value_list"].separator = "COMMA"
    defs["value_list"].required = False
    
    # Dict items
    defs["dict_items"].struct = [defs["dict_item"]]
    defs["dict_items"].repeat = True
    defs["dict_items"].separator = "COMMA"
    defs["dict_items"].required = False
    
    # Dict item
    defs["dict_item"].struct = ["STRING", "COLON", defs["value"]]
    
    # Expression values
    defs["expression_value"].alternatives = [
        defs["arithmetic_expr"],
        defs["comparison_expr"], 
        defs["conditional_expr"],
        defs["comprehension_expr"]
    ]
    
    # Arithmetic expression
    defs["arithmetic_expr"].struct = [defs["value"], defs["arithmetic_op"], defs["value"]]
    defs["arithmetic_op"].alternatives = ["PLUS", "MINUS", "STAR", "SLASH"]
    
    # Comparison expression
    defs["comparison_expr"].struct = [defs["value"], defs["comparison_op"], defs["value"]]
    defs["comparison_op"].alternatives = ["GT", "LT", "GE", "LE", "EQEQ", "NOTEQ"]
    
    # Conditional expression
    defs["conditional_expr"].struct = [
        "ID", defs["value"], defs["comparison_op"], defs["value"], 
        "COLON", defs["value"], "ID", "COLON", defs["value"]
    ]
    
    # Comprehension expression
    defs["comprehension_expr"].struct = [
        "LBRACKET", defs["value"], "ID", "ID", "ID", defs["iterable"], "RBRACKET"
    ]
    
    # Iterable
    defs["iterable"].alternatives = [defs["range_call"], defs["list_value"], "ID"]
    
    # Range call
    defs["range_call"].struct = ["ID", "LPAREN", "INT", "RPAREN"]
    
    # Template call
    defs["template_call"].struct = ["ID", "LPAREN", defs["template_args"], "RPAREN"]
    
    # Template args
    defs["template_args"].struct = [defs["value"]]
    defs["template_args"].repeat = True
    defs["template_args"].separator = "COMMA"
    defs["template_args"].required = False
    
    # F-string value
    defs["f_string_value"].struct = ["ID", "STRING"]
    defs["f_string_value"].keyword = "f"
    
    return defs

# Create the grammar
GRAMMAR = create_grammar()

# Export commonly used definitions
primitive_value = GRAMMAR["primitive_value"]
value_list = GRAMMAR["value_list"]
list_value = GRAMMAR["list_value"]
tuple_value = GRAMMAR["tuple_value"]
dict_value = GRAMMAR["dict_value"]
value = GRAMMAR["value"]

# Helper functions
def get_definition(name):
    """Get a definition by name"""
    return GRAMMAR.get(name)

def print_grammar():
    """Print all grammar definitions for debugging"""
    for name, def_obj in GRAMMAR.items():
        print(f"{name}: {def_obj}")

if __name__ == "__main__":
    # Test the grammar
    print("PyOS Grammar Definitions:")
    print("=" * 40)
    
    # Test circular references work
    print(f"value alternatives: {[alt.name if hasattr(alt, 'name') else alt for alt in value.alternatives]}")
    print(f"list_value struct: {[item.name if hasattr(item, 'name') else item for item in list_value.struct]}")
    print(f"value_list struct: {[item.name if hasattr(item, 'name') else item for item in value_list.struct]}")
    
    print("\nGrammar created successfully!")
    print(f"Total definitions: {len(GRAMMAR)}")