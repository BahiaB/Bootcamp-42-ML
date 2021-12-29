import sys

class Evaluator:
    
    def __init__(self, words, coef):
        self.words = words
        self.coef = coef

    def zip_evaluate(word, coef):
        ret = 0
        for item, nbr in zip(word, coef):
            print(item, nbr)
            ret = ret + len(item) * float(nbr)
        print(ret)

    def enumerate_evaluate(words, coef):
        if len(words) != len(coef):
            return(-1)
        ret = 0
        for i , word in enumerate(words):
            ret = ret + len(word) * coef[i]
        print(ret)
        return(ret)



words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coef = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(words, coef))
