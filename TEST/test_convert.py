def convert(lst):

    """Converts a string into a list and removes unwanted characters
    
    >>> convert("How much are my unsettled balances?")
    ['How', 'much', 'are', 'my', 'unsettled', 'balances']

    """
    bad_chars = [';', ':', '!', "*",'?','.',',']
    test_string = lst
    test_string = filter(lambda i: i not in bad_chars, test_string)  
    return ''.join(test_string).split()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
