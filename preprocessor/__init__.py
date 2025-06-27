
FILE_URI=r"test.pyos"
FILE = open(FILE_URI)

blocks_tokens = {"globals","template","func","main"}
current_block = {}
FILE_DATA = FILE.read()

def remove_empty_lines(text):
    return "\n".join([line for line in text.splitlines() if line.strip()])    

for i in  FILE_DATA.split("@")[1:]:
    block = i.split("(")[0]
    if block not in blocks_tokens:
        raise SyntaxError(f"Unknown block: {block}")
    block_data=remove_empty_lines(i[len(i.split("(")[0]):]).strip("()")
    current_block[block]= remove_empty_lines(block_data).split("\n")
    
globals= [i.replace(" ","") for i in current_block.get("globals", [])]
global_vars  ={}
for i in globals:
    if "==" in i:
        raise SyntaxError("Invalid assignment: '==' is not allowed, use '=' for assignment.")
    if "=" in i:
        key, value = i.split("=", 1)
        global_vars[key] = value
    


