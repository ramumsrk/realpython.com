#! /usr/bin/python3.12

# Function definition
def update_counter() -> None:
  print(F'Inside user-defined function \'update_counter()\'')
  global counter  
  print(f'Value of identifier \'counter\' is \'{counter=}\'')  
  counter = counter + 1
  print(f'Value of identifier \'counter\' is \'{counter=}\'')  
  print(f'Exiting user-defined function \'update_counter()\'')
  return

if __name__ == '__main__':
  # Identifier `counter' is
  # defined in `Global' scope
  # and is visible throughout
  # this file
  counter : int = 0
  print(f'Value of identifier \'counter\' is \'{counter=}\'')
  # Function call
  update_counter()
  print(f'Value of identifier \'counter\' is \'{counter=}\'')  