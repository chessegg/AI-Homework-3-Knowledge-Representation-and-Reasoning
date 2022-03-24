"""
@author: Craig Hilby(cxh170004)
"""

import sys
import re

class Main:
 
    def __init__(self):
        self.line_num = 1
        self.KB_map = {}
        self.KB_file = ''
    
    def open_file(self):
        file_exists = False
        while not file_exists:
            self.KB_file = input("Enter the KB file name: ")
            try:
                f = open(self.KB_file, "r")
                file_exists = True                
            except IOError:
                print("File not found, try again: ")
           
        KB = []        
        for line in f:
            line = re.sub(r'\n|\t', '', line)
            clause = []
            for literal in line.split(" "):
                clause.append(literal)
            KB.append(clause)
            self.KB_map[''.join(sorted(clause))] = 0
        f.close()
        return KB
    
    def print_clause(self, clause, i, j, line_num):
        comma = ','
        if (i == '' and j == ''): comma = ''
        joined_string = ' '.join(clause)
        print(str(line_num) + ". " + joined_string + " {" + i + comma + " " + j + "}")
        self.line_num += 1
    
    def negate_original(self, orig_clause):
        for c in range(len(orig_clause)):
            if orig_clause[c] == '~':
                orig_clause[c] = ''
            else:
                orig_clause[c] = '~' + orig_clause[c]
    
    def negate(self, literal):
        if literal[0] == '~':
            return literal[1:]
        else:
            return '~' + literal
                
    def original_steps(self, KB, orig_clause):
        for clause in KB:
            self.print_clause(clause, '', '', self.line_num)

        self.negate_original(orig_clause)

        for lit in orig_clause:
            KB.append([lit])
            self.KB_map[''.join(lit)] = 0
            self.print_clause(lit, '', '', self.line_num)
            
    def find_contradiction(self, KB):
        i = 1
        while i < self.line_num - 1:
            j = 0
            while i > j:
                res = self.resolve(KB[i], KB[j], KB)
                if res is False:
                    #self.print_clause()
                    print(str(self.line_num) + ". Contradiction" + " {" + str(i+1) + ", " + str(j+1) + "}")
                    self.line_num += 1
                    print("Valid")
                    sys.exit(0)
                elif res is True:
                    j += 1
                    continue
                else:
                    self.print_clause(res, str(i+1), str(j+1), self.line_num)
                    KB.append(res)
                    self.KB_map[''.join(sorted(res))] = 0
                j += 1
            i += 1
        print('Fail')    
    
    def resolve(self, clause1, clause2, KB):
        concat = list(set(clause1 + clause2))
        literal_list = concat[:]
        negate_map = {}
        for literal1 in clause1:
            negate_map[self.negate(literal1)] = literal1
        #print(negate_map)
        for literal2 in clause2:
            if literal2 in negate_map:
                literal_list.remove(literal2)
                literal_list.remove(negate_map[literal2])
                if len(literal_list) == 0:
                    return False
                elif self.isTrue(literal_list):
                    return True
                else:
                    if ''.join(sorted(literal_list)) in self.KB_map:
                        return True
                    return literal_list
    
        return True
    
    
    def isTrue(self, literal_list):
        negate_map = {}
        for literal1 in literal_list:
            negate_map[self.negate(literal1)] = literal1
        for literal2 in literal_list:
            if literal2 in negate_map:
                    return True
        return False
    
    def main(self):
        KB = self.open_file()
    
        orig_clause = KB[-1]
        KB.pop()        
        self.original_steps(KB, orig_clause)    
        self.find_contradiction(KB)
    
if __name__ == "__main__":
    run = Main()
    run.main()
        