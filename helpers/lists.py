def min_of_not_none(*args):
    """
    Returns the minimum of the arguments, ignoring None values. If all are
    None, None will be returned
    """
    if all(element is None for element in args):
        return None
    return min(element for element in args if element != None)
