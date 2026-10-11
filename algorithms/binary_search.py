'''A binary search algorithm written in Python'''

'''Opener:
    Have you ever been asked to guess a number from 1-100? It was hard, no? You probably guessed randomly at first until you narrowed it down.
    In programming, when a problem just like this arises, say, looking for a name in a database, 
    binary search can often be the most efficent way!
'''

'''Explanation (broken down as the visuals run):
    Just like its namesake, BInary search (use colorama to bold the \'BI\') begins by splitting its data in two.
    In this simulation, we're looking for the number __ (make the number set randomized, the target random,
    and the index of the target random).
    
    ... (show data)
    
    By finding the middle of the data by calculating the middle index, in this case, 5, we can check if the number there is bigger,
    or smaller than the target.
     
    ... (show comparison) 
    
    It seems that this number is ___!
    
    Since it's smaller/bigger, we'll chop off the top/bottom half of the data set. We now know it couldn't possibly be there,
    so cutting the search in two makes it so much faster compared to going through every part!
    
    If we continue this method with the middle indexing and chopping, we end up finding the number at...

    ... (simulate the search with small breaks in-between data presentations until it finishes)

    Index __!
'''