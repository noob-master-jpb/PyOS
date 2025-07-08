
required = "required"
struct = "struct"
type_ = "type"
repeat = "repeat"
separator = "separator"


definition = {

    "function": {
        struct: ["funct_name", "LPAREN", "param", "RPAREN", "COLON"],
        "function_name": {
            type_: "ID",
            required: True
        },
        "param": {
            type_: "ID",
            required: False,
            repeat: True,
            separator: "COMMA",
        }
    },
    "data": {
        struct: ["variable", "COLON", "data"],
        "variable": {
            type_: "ID",
            required: True
        },
        "data": {
            type_: ["int", "float", "string", "bool", "list", "tuple","dict"],
            required: True
        }
        
    }
}

defaults = {
    repeat:False,
    separator:None,
}
