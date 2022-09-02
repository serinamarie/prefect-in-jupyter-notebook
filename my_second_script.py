"""Run a flow in Prefect 2.x with multiple tasks and a flow within a flow (subflow)"""

from prefect import flow, task
from random import randint


@task(name="Get random number")
def get_random_nbr():

    return randint(41, 45)


@task(name="Determine if player wins")
def determine_if_winner(nbr):

    return "win" if nbr == 42 else "lose"


@flow(name="Return game outcome message")
def create_game_outcome_message(nbr):

    """This flow will run the determine_if_winner() task."""

    outcome = determine_if_winner(nbr)

    if outcome == "win":
        print("You won! Congratulations!")
    else:
        print("You lost this round. Better luck next time.")


@flow(name="Feeling Lucky Flow")
def feeling_lucky():

    """
    This flow will run the get_random_nbr() task and the 
    create_game_outc0ome_message() flow.
    """

    my_number = get_random_nbr()

    return create_game_outcome_message(my_number)
