from defination import Definition

value = Definition("value")

primitive_value = Definition("primitive_values")


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
function_call_value = Definition("function_call_value")
comprehension_value = Definition("comprehension_value")


function_call_value = Definition("function_call_value")
function_header = Definition("function_header")
function_name = Definition("function_name")
function_call_value = Definition("function_call_value")
param_list = Definition("param_list")
param = Definition("param")
param = Definition("param")
function_call_value = Definition("function_call_value")

property_def = Definition("property_def")
property_name = Definition("property_name")
property_value = Definition("property_value")

value.alternatives = [
    primitive_value, 
    collection_value, 
    expression_value,
    template_call,
    f_string_value
]

primitive_value.alternatives = ["STRING", "INT", "FLOAT", "ID"]
collection_value.alternatives = [
    list_value, 
    tuple_value, 
    dict_value
]
value_list.struct = [value]
value_list.repeat = True
value_list.separator = "COMMA"
value_list.required = False
list_value.struct = ["LBRACKET", value_list, "RBRACKET"]
tuple_value.struct = ["LBRACE", value_list, "RBRACE"]
dict_value.struct = ["LBRACE", value_list, "RBRACE"]
dict_value.struct = ["LBRACE", dict_items, "RBRACE"]
dict_items.struct = [dict_item]
dict_items.repeat = True
dict_items.separator = "COMMA"
dict_items.required = False
dict_item.struct =  [key, "COLON", value]
key.alternatives = ["STRING", "ID"]

expression_value.alternatives = [
    arithmrtic_expr,
    conditional_expr,
    comparison_expr,
    comprehension_value
]

arithmetic_op = Definition("arithmetic_op")
arithmetic_op.alternatives = ["PLUS", "MINUS", "STAR", "SLASH", "MOD"]
arithmrtic_expr.struct = [value, arithmetic_op, value]

comparison_op = Definition("comparison_op")
comparison_op.alternatives = ["GT", "LT", "GE", "LE", "EQEQ", "NOTEQ"]
comparison_expr.struct = [value, comparison_op, value]



iterable = Definition("iterable")
iterable.alternatives = [collection_value, "ID","RANGE_CALL"]
comprehension_expr.struct = ["LBRACKET", value, "FOR", "ID", "IN", iterable, "RBRACKET"]

template_args.struct = (value,)
template_args.repeat = True
template_args.separator = "COMMA"
template_args.required = False
template_call.struct =["ID", "LPAREN", template_args, "RPAREN"]

f_string_value.struct = ["F", "STRING"]

typed_key.struct = ["TYPE","COLON", "ID"]
assignment_target.alternatives = ["STRING","ID",typed_key,f_string_key]

assignment.struct = [assignment_target, "COLON", assignment_value]