#! /usr/bin/python3.12

# Function definition
def print_total() -> None:
  print(F'Inside user-defined function \'print_total()\'')
  # Nested function definition
  def nested_print_total() -> None:
    print(F'Inside user-defined function \'nested_print_total()\'')
    print(f'Value of identifier \'total\' is \'{total=}\'')
    print(F'Exiting user-defined function \'nested_print_total()\'')    
    return
  total : int = 5
  # Function call
  nested_print_total()
  print(f'The value of identifier \'total\' is \'{total=}\'')
  print(F'Exiting user-defined function \'print_total()\'')  
  return

if __name__ == '__main__':
  # Function call
  print_total()