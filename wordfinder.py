
import random

class WordFinder():
   """Word Finder: finds random words from a dictionary.
   
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() 
    cat

    >>> wf.random() 
    dog

    >>> wf.random() 
    porcupine
    """ 

   def __init__(self, path):
    """ Read dictionary and report # items read."""
    file =open(path)
    """set 'self.words' equal to the list of words in each line of the file"""
    self.words = self.parse(file)
    print(f"{len(self.words)} words read")


   def __repr__(self):
        return f"<WordFinder words = {self.words}>" 

   
   def parse(self, file):
        """Iterate over each line in 'file', strip off the end of line character and return each word on a line"""
        
        return [word.strip() for word in file]


   def random(self):
        """Return random word"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Remove blank lines and # character so only words are returned 
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() 
    pear

    >>> swf.random() 
    carrot

    >>> swf.random() 
    kale

    """
        
    def parse(self, file):
        """Iterate over each line in 'file', strip off the end of line character and return each    word on a line, skipping blanks/comments."""

        return [word.strip() for word in file
                if word.strip() and not word.startswith("#")]
    
        

