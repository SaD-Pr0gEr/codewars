class CharactersCount:
    """
    The main idea is to count all the occurring characters in a string. 
    If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
    """
    
    def my_solution(self, string):
        if not string:
            return {}
        strs = set(string)
        some_dict = {}
        for i in strs:
            some_dict[i] = string.count(i)
        return some_dict
    
    def my_solution_2(self, string):
        if not string:
            return {}
        some_dict = {}
        for i in string:
            for a in set(string):
                if a == i:
                    if a in some_dict.keys():
                        some_dict[i] += 1
                    else:
                        some_dict[i] = 1
        return some_dict
    
    def best_solution(self, string):
        return {i: string.count(i) for i in string}
  
