#! /usr/bin/python3.12

# Function definition
def print_total() -> None:
  print(F'Inside user-defined function \'print_total()\'')
  total : int = 5
  print(f'Value of identifier \'total\' is \'{total=}\'')
  print(F'Exiting user-defined function \'print_total()\'')
  return

if __name__ == '__main__':
  # Function call
  print_total()