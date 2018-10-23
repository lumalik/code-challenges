def toJadenCase(string):
    ''' Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013).
    Jaden is also known for some of his philosophy that he delivers via Twitter.
    When writing on Twitter, he is known for almost always capitalizing every word.
    Your task is to convert strings to how they would be written by Jaden Smith.
    The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed themself.
    '''
    list = string.split()
    new_list = []
    for s in list:
        first_letter = s[0].upper()
        other_letters = s[1:]
        new_s = first_letter + other_letters
        new_list.append(new_s)
    return(' '.join(new_list))

toJadenCase("How can mirrors be real if our eyes aren't real")
