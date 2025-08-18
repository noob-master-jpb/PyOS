from defination import Definition

value = Definition("value")

primitive_value = Definition("primitive_values")

iterable = Definition("iterable")
collection_value = Definition("collection")
list_value = Definition("list_value")
value_list = Definition("value_list")
tuple_value = Definition("tuple_value")

dict_value = Definition("dict_value")
dict_items = Definition("dict_items")
dict_item = Definition("dict_item")
key = Definition("key")



expression_value = Definition("expression")
arithmrtic_expr = Definition("arithmrtic_expr") 
conditional_expr = Definition("conditional_expr")
comparison_expr = Definition("comparison_expr")
comprehension_expr = Definition("comprehension_expr")

arithmetic_op = Definition("arithmetic_op")
comparison_op = Definition("comparison_op")


template_call = Definition("template_call")
template_args = Definition("template_args")

f_string_value = Definition("fstring")


assignment = Definition("assignment")

assignment_target = Definition("assignment_target")
simple_key = Definition("simple_key")
typed_key = Definition("typed_key")
f_string_key = Definition("f_string_key")

assignment_value = Definition("assignment_value")
simple_value = Definition("simple_value")
typed_value = Definition("typed_value")
comprehension_value = Definition("comprehension_value")


function_header = Definition("function_header")
function_name = Definition("function_name")
call_args = Definition("call_args")
param = Definition("param")
function_call_value = Definition("function_call_value")

property_def = Definition("property_def")
property_value = Definition("property_value")
property_item = Definition("property_item")
property_items = Definition("property_items") 


value.alternatives((
    primitive_value, 
    collection_value, 
    expression_value,
    template_call,
    f_string_value
))

primitive_value.alternatives(("STRING", "INT", "FLOAT", "ID"))
collection_value.alternatives((
    list_value,
    tuple_value,
    dict_value
))

value_list.struct((value))
value_list.repeat(True)
value_list.separator("COMMA")
value_list.required(False)
list_value.struct(("LBRACKET", value_list, "RBRACKET"))
tuple_value.struct(("LPAREN", value_list, "RPAREN"))
dict_value.struct(("LBRACE", dict_items, "RBRACE"))

dict_items.struct((dict_item,))
dict_items.repeat(True)
dict_items.separator("COMMA")
dict_items.required(False)
dict_item.struct((key, "COLON", value))
key.alternatives(("STRING", "ID"))

expression_value.alternatives((
    arithmrtic_expr,
    conditional_expr,
    comparison_expr,
    comprehension_expr
))

arithmetic_op.alternatives(("PLUS", "MINUS", "STAR", "SLASH", "MOD"))
arithmrtic_expr.struct((value, arithmetic_op, value))  # Remove quotes

comparison_op.alternatives(("GT", "LT", "GE", "LE", "EQEQ", "NOTEQ"))
comparison_expr.struct((value, comparison_op, value))  # Remove quotes

iterable.alternatives((collection_value, "ID", "RANGE_CALL"))  # Remove quotes

conditional_expr.struct((value, "IF", value, "COLON", value, "ELSE", "COLON", value))


comprehension_expr.struct(("LBRACKET", value, "FOR", "ID", "IN", iterable, "RBRACKET"))

template_args.struct((value,))
template_args.repeat(True)
template_args.separator("COMMA")
template_args.required(False)
template_call.struct(("ID", 
                      "LPAREN", 
                      template_args, 
                      "RPAREN"))

f_string_value.struct(("F", "STRING"))

simple_key.struct(("ID",))
typed_id = Definition("typed_id")

typed_key.struct(("TYPE","COLON", "STRING"))
assignment_target.alternatives((simple_key,typed_key,f_string_key,"PROPERTY"))

typed_value.struct(("TYPE", "COLON", value))
assignment_value.alternatives(
    (value,typed_value,comprehension_value,function_call_value,property_value)
)

call_args.struct((value,))
call_args.repeat(True)
call_args.separator("COMMA")
call_args.required(False)

function_call_value.struct(
    ("ID", "LPAREN", call_args, "RPAREN")
)


comprehension_value.struct(
    (value, "FOR", "ID", "IN", iterable, )
)
assignment.struct(
    (assignment_target,"COLON",assignment_value)
)

function_name.struct(("ID",))

param.struct(("ID",))  # Single parameter is just an ID

param_list = Definition("param_list")
param_list.struct((param,))      
param_list.repeat(True)          
param_list.separator("COMMA")    
param_list.required(False)       

function_header.struct(
    (function_name, "LPAREN", param_list, "RPAREN", "COLON")
)

property_item.struct(("STRING", "COLON", "STRING"))

property_items.struct((property_item,))
property_items.repeat(True)
property_items.separator("COMMA")

property_value.struct(("LBRACKET", property_items, "RBRACKET"))

property_def.struct(
    ("PROPERTY", "COLON", property_value)
)
