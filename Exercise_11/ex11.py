""" CSC148 Exercise 11 Banana Game

Joshua Fung
July 31st, 2015

The Banana Game
"""


def banana_game(source, goal, container):
    """(str, str, Container) -> bool
    Return True if source string can convert to goal string under
    banana game rules using the container

    We assume the container given at the start contains nothing
    """
    # Check is goal is empty string
    # Goal is not empty string
    if(goal == ""):
        # Empty container
        if(container.is_empty()):
            # If source is also empty
            if(source == ""):
                # Base case everything is empty at the same time
                return True

    # Goal is not empty
    else:
        # If container is not empty
        if(not container.is_empty()):
            # Container contains the right letter
            if(container.peek() == goal[0]):
                container.get()
                # Recursively call the rest, one less for c and g
                return banana_game(source, goal[1:], container.copy())

            # There is no need for else if peek does not math gaol
            # It is the same as container being empty
            else:
                pass

        # If container is empty or container does not match
        # If source is not empty
        if(source != ""):

            # Container is out of the way, now compare the sourece and goal
            if(source[0] == goal[0]):
                # Recursively call with one char less for source and goal
                return banana_game(source[1:], goal[1:], container.copy())

            # If even the source does not have a match char
            else:
                try:
                    # Store it for a later
                    container.put(source[0])
                # If it is something like a bucket that will full
                except ContainerFullException:
                    # Fall to return False
                    pass
                else:
                    # Recursion, one char went from source to container
                    return banana_game(source[1:], goal, container.copy())

        # Everything else mean it fail to convert the string
        return False
