"""This code illustrates the use of namespaces in Python. Each function defined here is part of the module's namespace, and they can be accessed using the module name when imported."""

import math

variable_in_the_global_namespace = "This variable is part of the module's namespace."
another_variable_the_global_namespace = "This is another variable in the same namespace."
an_int_in_the_global_namespace = 42


def foo():
    """A simple function that prints a message."""
    print("Hello from foo!")
    variable_in_foos_local_namespace = "A local variable."
    print(f"Here is the value of variable_in_foos_local_namespace: {variable_in_foos_local_namespace}")
    print("Here is what is known in the local (foo) namespace:")
    pretty_print_dictionary(locals())
    print()


def bar():
    """Another simple function that prints a different message."""
    print("Hello from bar!")
    print("Here is what is known in the local (bar) namespace:")
    pretty_print_dictionary(locals())


def pretty_print_dictionary(d: dict) -> None:
    """Pretty print a dictionary."""
    print("-" * 40)
    for key, value in d.items():
        if isinstance(
            value, dict
        ):  # If the value is a dictionary, we don't want to print it directly because it might be too large.
            print(f"{key}: ...")
        else:
            print(f"{key}: {value}")
    print("-" * 40)


def main():
    """The main function that calls foo and bar."""
    print(f"Here is what is known in the global namespace:")
    pretty_print_dictionary(globals())
    print()

    foo()
    bar()


if __name__ == "__main__":
    main()
