# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)"%(str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) == bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"


# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):
    if is_word(string[i : j + 1]):
        return RespaceTableCell(True, j)
    else:
        for cut in range(i, j):
            if T.get(i, cut).value and T.get(cut + 1, j).value:
                return RespaceTableCell(True, cut)
    return RespaceTableCell(False, None)
                  
# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):
    res = []
    for j in range(N):
        for i in range(N - j):
            res.append((i, i + j))
    return res

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
    if table.get(0, len(s) - 1).value == False:
        return None
    
    res = ''
    i = 0
    j = len(s) - 1
    while True:
        curr = table.get(i, j)
        if curr.index == j:
            res += s[i : j + 1]
            return res
        tmp = curr.index
        res = res + s[i : tmp + 1] + ' '
        i = tmp + 1

if __name__ == "__main__":
    # Example usage.
    from dynamic_programming import DynamicProgramTable
    s = "itwasthebestoftimes"
    wordlist = ["of", "it", "the", "best", "times", "was"]
    D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    print respace_from_table(s, D)
