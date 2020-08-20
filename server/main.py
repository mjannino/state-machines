from demos.automat_demo import automat_demo
from demos.python_statemachine_demo import python_statemachine_demo
from demos.transitions_demo import transitions_demo

import click


@click.command()
@click.option("--library", prompt="Library", help="The state machine demo to run.")
def main(library):
    """
    Run each library demo based on input from the user
    """
    print(f"Running {library} demo...")
    if library == "automat":
        automat_demo()
    elif library == "python-statemachine":
        python_statemachine_demo()
    elif library == "transitions":
        transitions_demo()
    else:
        print(
            "Invalid input; must be one of: automat, python-statemachine, or transitions."
        )


if __name__ == "__main__":
    main()
