#! /usr/bin/python3.14d

# user-defined function
def sum_of_squares_of_first_ten_numbers() -> int:
    '''
    Return the sum of squares of
    first ten numbers
    '''
    return sum([number*number for number in range(1,11)])

# user-defined function
def main() -> None:
    '''
    An entry-point function
    '''
    print(f'Sum of squares of first ten numbers are: {sum_of_squares_of_first_ten_numbers()}')
    return None

if __name__ == '__main__':
    # function call
    main()