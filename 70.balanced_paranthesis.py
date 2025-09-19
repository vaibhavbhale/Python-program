def balanced(expr):
    while "()" in expr or "{}" in expr or "[]" in expr:
        expr = expr.replace("()", "").replace("{}", "").replace("[]", "")
        
    return expr == ""

expr = input("Enter an expression: ")
if balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")
