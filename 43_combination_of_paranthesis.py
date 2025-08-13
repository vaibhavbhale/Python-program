def  parenthesis(n, openpara, closepara, s, res):

    if openpara == n and closepara == n:
        res.append(s)
        return

    if openpara < n:
      parenthesis(n, openpara + 1, closepara, s + "{", res)

    if closepara < openpara:
        parenthesis(n, openpara, closepara + 1, s + "}", res)


n =int(input("Enter the value to generate paranthesis:"))
res = []
parenthesis(n, 0, 0, "",res)
for s in res:
    print(s)