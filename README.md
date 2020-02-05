# nyt_spelling_bee_solver
Command line tool to solve and score answers for the New York Times Spelling Bee daily puzzle.

To run nyt_spelling_bee_solver:
    
    python3 nyt_spelling_bee_solver.py jumble_dicts/jumble_dict.json OWDRIFT
    
The first letter of the query is the center letter of the puzzle which must be used in every word.

# Rules

Players are asked to generate as many English words as possible from a set of 7 letters, including one center letter which must be used in every word.

    Words must contain at least 4 letters.
    Words must include the center letter.
    Our word list does not include words that are obscure, hyphenated, or proper nouns.
    No cussing either, sorry.
    Letters can be used more than once.
    4-letter words are worth 1 point each.
    Longer words earn 1 point per letter.
    Each puzzle includes at least one “pangram” which uses every letter. These are worth 7 extra points!

# To-do

    -Allow users to interactively add or remove words to legal words.
    -Find an archive of puzzle solutions and analyze trends.  I'm curious if we can infer the rules for puzzle creation: number of possible words required, vowel/consanant distribution, letter frequency over time, etc.
