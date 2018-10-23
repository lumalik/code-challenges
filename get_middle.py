def get_middle(s):
    '''You are going to be given a word. Your job is to return the middle character of the word.
    If the word's length is odd, return the middle character.
    If the word's length is even, return the middle 2 characters.'''

    if len(s) % 2 == 0:
        first_letter =  s[int((len(s)/2) - 1)]
        second_letter = s[int((len(s)/2))]
        output = first_letter + second_letter
        return(output)
    else:
        index = int(round((len(s)/2)) - 1)
        output = s[index]
        return(output)

get_middle("testing")
