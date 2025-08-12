
# Parser Grammar Definition for PyOS
# This file defines the grammar rules for parsing PyOS data structures

# Grammar definition constants
required = "required"
struct = "struct"
type_ = "type"  
repeat = "repeat"
separator = "separator"
keyword = "keyword"
optional = "optional"
alternatives = "alternatives"

# Keywords in the language
keyword_defination = [
    "int", "str", "float", "bool", "list", "dict", "tuple",
    "for", "in", "while", "if", "else", "elif", "True", "False", "None",
    "continue", "break", "pass", "f"
]



# Data type definitions for values
data_defination = {
    "value": {
        alternatives: [
            "primitive_value",
            "collection_value", 
            "expression_value",
            "template_call",
            "f_string_value"
        ],
        
        "primitive_value": {
            alternatives: ["STRING", "INT", "FLOAT", "ID"]
        },
        
        "collection_value": {
            alternatives: ["list_value", "tuple_value", "dict_value"],
            
            "list_value": {
                struct: ["LBRACKET", "value_list", "RBRACKET"],
                "value_list": {
                    struct: ["value"],
                    repeat: True,
                    separator: "COMMA",
                    required: False
                }
            },
            
            "tuple_value": {
                struct: ["LPAREN", "value_list", "RPAREN"],
                "value_list": {
                    struct: ["value"],
                    repeat: True,
                    separator: "COMMA",
                    required: False
                }
            },
            
            "dict_value": {
                struct: ["LBRACE", "dict_items", "RBRACE"],
                "dict_items": {
                    struct: ["dict_item"],
                    repeat: True,
                    separator: "COMMA",
                    required: False
                },
                "dict_item": {
                    struct: ["key", "COLON", "value"],
                    "key": {
                        alternatives: ["STRING", "ID"]
                    },
                    
                }
            }
        },
        
        "expression_value": {
            alternatives: [
                "arithmetic_expr",
                "comparison_expr", 
                "conditional_expr",
                "comprehension_expr"
            ],
            
            "arithmetic_expr": {
                struct: ["value", "arithmetic_op", "value"],
                "arithmetic_op": {
                    alternatives: ["PLUS", "MINUS", "STAR", "SLASH", "MOD"]
                }
            },
            
            "comparison_expr": {
                struct: ["value", "comparison_op", "value"],
                "comparison_op": {
                    alternatives: ["GT", "LT", "GE", "LE", "EQEQ", "NOTEQ"]
                }
            },
            
            "conditional_expr": {
                struct: ["IF", "value", "comparison_op", "value", "COLON", "value", "ELSE", "COLON", "value"],
                "comparison_op": {
                    alternatives: ["GT", "LT", "GE", "LE", "EQEQ", "NOTEQ"]
                }
            },
            
            "comprehension_expr": {
                struct: ["LBRACKET", "value", "FOR", "ID", "IN", "iterable", "RBRACKET"],
                "iterable": {
                    alternatives: ["range_call", "list_value", "ID"],
                    "range_call": {
                        struct: ["ID", "LPAREN", "INT", "RPAREN"]
                    }
                }
            }
        },
        
        "template_call": {
            struct: ["ID", "LPAREN", "template_args", "RPAREN"],
            "template_args": {
                struct: ["value"],
                repeat: True,
                separator: "COMMA",
                required: False
            }
        },
        
        "f_string_value": {
            struct: ["ID", "STRING"],
            "ID": {
                keyword: "f"
            }
        }
    }
}

# Main grammar definitions
global_definition = {
    
    # Assignment patterns
    "assignment": {
        struct: ["assignment_target", "COLON", "assignment_value"],
        
        "assignment_target": {
            alternatives: [
                "simple_key",
                "typed_key", 
                "f_string_key"
            ],
            
            "simple_key": {
                alternatives: ["STRING", "ID"]
            },
            
            "typed_key": {
                struct: ["type_annotation", "COLON", "key_name"],
                "type_annotation": {
                    alternatives: ["ID"],
                    keyword: True
                },
                "key_name": {
                    alternatives: ["STRING", "ID"]
                }
            },
            
            "f_string_key": {
                struct: ["ID", "STRING"],
                "ID": {
                    keyword: "f"
                }
            }
        },
        
        "assignment_value": {
            alternatives: [
                "simple_value",
                "typed_value",
                "function_call_value",
                "comprehension_value"
            ],
            
            "simple_value": {
                struct: ["value"]
            },
            
            "typed_value": {
                struct: ["type_annotation", "COLON", "value"],
                "type_annotation": {
                    alternatives: ["ID"],
                    keyword: True
                }
            },
            
            "function_call_value": {
                struct: ["type_annotation", "LPAREN", "call_args", "RPAREN"],
                "type_annotation": {
                    alternatives: ["ID"],
                    keyword: True
                },
                "call_args": {
                    struct: ["value"],
                    repeat: True,
                    separator: "COMMA",
                    required: False
                }
            },
            
            "comprehension_value": {
                struct: ["value", "FOR", "ID", "IN", "iterable"]
            }
        }
    },
      
    # Function definitions
    "function_header": {
        struct: ["function_name", "LPAREN", "param_list", "RPAREN", "COLON"],
        
        "function_name": {
            type_: "ID",
            required: True,
            keyword: False
        },
        
        "param_list": {
            struct: ["param"],
            repeat: True,
            separator: "COMMA",
            required: False,
            
            "param": {
                type_: "ID",
                required: True,
                keyword: False
            }
        }
    },
    
    # Property definitions (for objects like "tag")
    "property_def": {
        struct: ["property_name", "COLON", "property_value"],
        
        "property_name": {
            alternatives: ["STRING", "ID"]
        },
        
        "property_value": {
            alternatives: ["STRING"]
        }
    },
    

}

# Default values for grammar rules
defaults = {
    repeat: False,
    separator: None,
    required: True,
    keyword: False,
    optional: False
}

# Helper function to resolve grammar rules
def resolve_rule(rule_name, definition_dict=None):
    """
    Resolve a grammar rule by name from the appropriate definition dictionary
    """
    if definition_dict is None:
        definition_dict = global_definition
    
    if rule_name in definition_dict:
        return definition_dict[rule_name]
    elif rule_name in data_defination:
        return data_defination[rule_name]
    else:
        return None

# Main parser class
class PyOSParser:
    def __init__(self):
        self.tokens = []
        self.position = 0
        self.current_token = None
    
    def parse(self, tokens):
        """
        Main parsing function that processes a list of tokens
        """
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[0] if tokens else None
        
        return self.parse_document()
    
    def parse_document(self):
        """
        Parse the entire document as a series of assignments or objects
        """
        result = []
        
        while self.current_token is not None:
            if self.match_token("INDENT") or self.match_token("NEWLINE"):
                self.advance()
                continue
                
            item = self.parse_top_level_item()
            if item:
                result.append(item)
        
        return result
    
    def parse_top_level_item(self):
        """
        Parse a top-level item (assignment, object, etc.)
        """
        if self.current_token and self.current_token[0] == "STRING":
            # Could be an object definition or simple assignment
            return self.parse_assignment_or_object()
        elif self.current_token and self.current_token[0] == "ID":
            # Could be typed assignment or function call
            return self.parse_typed_assignment()
        else:
            self.advance()
            return None
    
    def parse_assignment_or_object(self):
        """
        Parse either a simple assignment or object definition
        """
        # Implementation would depend on lookahead
        # For now, assume simple assignment
        return self.parse_assignment()
    
    def parse_assignment(self):
        """
        Parse a key:value assignment
        """
        key = self.current_token[1] if self.current_token else None
        self.advance()
        
        if not self.match_token("COLON"):
            return None
        self.advance()
        
        value = self.parse_value()
        
        return {"type": "assignment", "key": key, "value": value}
    
    def parse_typed_assignment(self):
        """
        Parse a typed assignment like int:"1":int:"3"
        """
        type_hint = self.current_token[1] if self.current_token else None
        self.advance()
        
        if not self.match_token("COLON"):
            return None
        self.advance()
        
        key = self.current_token[1] if self.current_token else None
        self.advance()
        
        if self.match_token("COLON"):
            self.advance()
            value = self.parse_value()
        else:
            value = None
            
        return {"type": "typed_assignment", "type_hint": type_hint, "key": key, "value": value}
    
    def parse_value(self):
        """
        Parse a value (primitive, collection, expression, etc.)
        """
        if not self.current_token:
            return None
            
        token_type, token_value = self.current_token
        
        if token_type in ["STRING", "INT", "FLOAT"]:
            self.advance()
            return {"type": "primitive", "value": token_value}
        elif token_type == "ID":
            return self.parse_identifier_value()
        elif token_type == "LBRACKET":
            return self.parse_list()
        elif token_type == "LPAREN":
            return self.parse_tuple()
        elif token_type == "LBRACE":
            return self.parse_dict()
        else:
            self.advance()
            return None
    
    def parse_identifier_value(self):
        """
        Parse identifier-based values (function calls, variables, etc.)
        """
        name = self.current_token[1]
        self.advance()
        
        if self.match_token("LPAREN"):
            # Function call
            self.advance()
            args = self.parse_argument_list()
            if self.match_token("RPAREN"):
                self.advance()
            return {"type": "function_call", "name": name, "args": args}
        else:
            # Simple identifier
            return {"type": "identifier", "name": name}
    
    def parse_list(self):
        """
        Parse a list [item1, item2, ...]
        """
        if not self.match_token("LBRACKET"):
            return None
        self.advance()
        
        items = []
        while self.current_token and not self.match_token("RBRACKET"):
            if self.match_token("COMMA"):
                self.advance()
                continue
            item = self.parse_value()
            if item:
                items.append(item)
        
        if self.match_token("RBRACKET"):
            self.advance()
            
        return {"type": "list", "items": items}
    
    def parse_tuple(self):
        """
        Parse a tuple (item1, item2, ...)
        """
        if not self.match_token("LPAREN"):
            return None
        self.advance()
        
        items = []
        while self.current_token and not self.match_token("RPAREN"):
            if self.match_token("COMMA"):
                self.advance()
                continue
            item = self.parse_value()
            if item:
                items.append(item)
        
        if self.match_token("RPAREN"):
            self.advance()
            
        return {"type": "tuple", "items": items}
    
    def parse_dict(self):
        """
        Parse a dictionary {key1: value1, key2: value2, ...}
        """
        if not self.match_token("LBRACE"):
            return None
        self.advance()
        
        items = []
        while self.current_token and not self.match_token("RBRACE"):
            if self.match_token("COMMA") or self.match_token("NEWLINE") or self.match_token("INDENT"):
                self.advance()
                continue
                
            # Parse key
            key = self.parse_value()
            if not key:
                break
                
            if not self.match_token("COLON"):
                break
            self.advance()
            
            # Parse value
            value = self.parse_value()
            
            items.append({"key": key, "value": value})
        
        if self.match_token("RBRACE"):
            self.advance()
            
        return {"type": "dict", "items": items}
    
    def parse_argument_list(self):
        """
        Parse a comma-separated list of arguments
        """
        args = []
        while self.current_token and not self.match_token("RPAREN"):
            if self.match_token("COMMA"):
                self.advance()
                continue
            arg = self.parse_value()
            if arg:
                args.append(arg)
        return args
    
    def match_token(self, expected_type):
        """
        Check if current token matches expected type
        """
        return (self.current_token and 
                self.current_token[0] == expected_type)
    
    def advance(self):
        """
        Move to the next token
        """
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None
