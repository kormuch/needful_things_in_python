class Function_Composition():
    def __init__(self, list_of_tuples_01, list_of_tuples_02):
        self.list_of_tuples_01 = list_of_tuples_01
        self.list_of_tuples_02 = list_of_tuples_02
        
    def give_function_composition(self):
        i=0
        relations_unordered = []
        relations_ordered = []
        for tuples_2 in self.list_of_tuples_02:
            for tuples_1 in self.list_of_tuples_01:
                if tuples_2[1] == tuples_1[0]:
                    relations_unordered.append(tuples_2[0])
                    relations_unordered.append(tuples_1[1])
        while i<len(relations_unordered):
            relations_ordered.append(relations_unordered[i:i+2])
            i+=2
        return(relations_ordered)
        return "No relation found"
                
my_set_1 = Function_Composition([(3,5),(2,7),(8,1),(2,10)],
                                 [(5,2),(3,6),(1,8),(3,8)])

print(my_set_1.give_function_composition())
