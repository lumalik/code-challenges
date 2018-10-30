def get_length_of_missing_array(array_of_arrays):
    '''You get an array of arrays.
    If you sort the arrays by their length, you will see, that their length-values are consecutive.
    But one array is missing!
    You have to write a method, that return the length of the missing array.'''
    if len(array_of_arrays) == 0:
        return(0)
    m = []
    for array in array_of_arrays:
        if (array == None) or (len(array) == 0):
            return(0)
        m.append(len(array))

    m.sort()
    a = set(m)
    b = set(range(m[0], m[-1]))
    result = (b-a).pop()
    return(result)
