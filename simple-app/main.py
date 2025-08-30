def sum_of_two(a: int, b: int) -> int:
    '''Defining the simple function'''
    return a + b

def main() -> None:
    '''Printing name and reg #'''
    print("Name: Najabat Ali Khan")
    print("PIAIC Reg#: PIAIC113998")
    a, b = 7, 5
    print(f"Sum of {a} + {b} = {sum_of_two(a, b)}")

if __name__ == "__main__":
    main()