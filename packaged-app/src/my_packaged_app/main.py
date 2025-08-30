def word_count(text: str) -> int:
    '''Defining simple function (word count)'''
    return len([w for w in text.split() if w])

def main() -> None:
    '''Printing my name & reg#.'''
    print("Name: Najabat Ali Khan")
    print("PIAIC Reg#: PIAIC113998")
    text = "This is uv packaged app program."
    print(f"Text: {text!r}")
    print(f"Word count = {word_count(text)}")

if __name__ == "__main__":
    main()
