#Calculator project
import calculator_art
print(calculator_art.logo)

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

#operation symbol to function convertion
operations = {
  "+": add, 
  "-": sub,
  "*": mul, 
  "/": div
}

def calculator():
  num1 = float(input("What's the first number?: "))
  for operation in operations:
    print(operation)

  run = True
  while run:
    op = input("Pick an operation?: ")
    num2 = float(input("What's the next number?: "))
    function = operations[op]
    answer = function(num1,num2)
    print(f"{num1} {op} {num2} = {answer}")

    action = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start again, or type 'exit' to quit: ")

    if action == "y":
      num1 = answer
    elif action == "n" :
      run = False
      calculator() #recursive callback
    else:
      run = False

calculator()