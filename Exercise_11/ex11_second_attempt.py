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
                # Recursively call with one less source and goal
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
                    # Recursivly call with one char when from source to container
                    return banana_game(source[1:], goal, container.copy())

        # Everything else mean it fail to convert the string
        return False

banana_game("BANANA", "ANANAB", MyBucket())



def banana_game(source, goal, container):
    """(str, str, Container) -> bool
    Return True if source string can convert to goal string under
    banana game rules using the container

    We assume the container given at the start contains nothing
    """
    # Check if the container is empty or not
    # Container is empty
    if(container.is_empty()):
        if(source != "" and goal != ""):
            if(source[0] == goal[0]):
                return banana_game(source[1:], goal[1:],\
                                   container.copy())
            else:
                try:
                    container.put(source[0])
                except ContainerFullException:
                    return False
                else:
                    return banana_game(source[1:], goal,\
                                       container.copy())
        elif(source == "" and goal == ""):
            return True
        else:
            return False
        
    # Container is not empty
    else:
        if(goal != ""):
            if(container.peek() == goal[0]):
                container.get()
                return banana_game(source, goal[1:], container.copy())
            elif(source != ""):
                if(source[0] == goal[0]):
                    return banana_game(source[1:], goal[1:],\
                                       container.copy())
                else:
                    try:
                        container.put(source[0])
                    except ContainerFullException:
                        return False
                    else:
                        return banana_game(source[1:], goal,\
                                           container.copy())
        else:
            return False
        
        
