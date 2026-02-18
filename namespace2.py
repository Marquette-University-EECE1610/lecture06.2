from namespace import pretty_print_dictionary, foo, bar, math


def main():
    """The main function that calls foo and bar."""
    print(f"Here is what is known in the global namespace of this module ({__file__}):")
    pretty_print_dictionary(globals())
    print()

    foo()
    bar()


if __name__ == "__main__":
    main()
