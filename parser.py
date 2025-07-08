
required = "required"
struct = "struct"
type_ = "type"
repeat = "repeat"
separator = "separator"
keyword = "keyword"


keyword_defination = [
    "int",
    "for",
    "while",
    "if",
    "else",
    "elif",
    "continue",
    "break",
    "pass",
]

data_defination = {
    
}
global_definition = {

    "function": {
        struct: ["funct_name", "LPAREN", "param", "RPAREN", "COLON"],
        "function_name": {
            type_: "ID",
            required: True,
            keyword: False
        },
        "param": {
            type_: "ID",
            required: False,
            repeat: True,
            separator: "COMMA",
            keyword: False,
        }
    },
    "data": {
        struct: ["data_type", "COLON", "variable", 
                 "COLON", 
                 "data_type", "COLON","data"],
        
        
        
        "data_type": {
            type_: "ID",
            required: True,
            keyword: True
        },
        
        "variable": {
            type_: "STRING",
            required: True,
            keyword: True,
        },
        "data": {
            type_: data_defination,
            required: True,
            keyword: True,
        }
        
    }
}


defaults = {
    repeat:False,
    separator:None,
}
