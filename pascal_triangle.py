def pascals_triangle(n):
    pascal = []
    for level in range(1, n+1):
        new_row = [1] * level
        for i in range(1,len(new_row)-1):
            new_row[i] = previous_row[i-1] + previous_row[i]
        previous_row = new_row
        pascal.append(new_row)
    pascal = [y for x in pascal for y in x] #flattens the list
    return(pascal)