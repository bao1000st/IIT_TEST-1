expression = input('input your expression: ')

if (expression.count('(') != expression.count(')') or 
    expression.count('{') != expression.count('}') or
    expression.count('[') != expression.count(']') ):
  print("False")
else:
  print("True")
  