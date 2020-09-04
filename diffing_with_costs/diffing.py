import dynamic_programming

# DO NOT CHANGE THIS CLASS
class DiffingCell:
    def __init__(self, s_char, t_char, cost):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)"%(self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
def fill_cell(table, i, j, s, t, cost):
    if i == 0 and j == 0:
        return DiffingCell('-', '-', 0)
    if i == 0:
        return DiffingCell('-', t[j - 1], table.get(i, j - 1).cost + cost('-', t[j - 1]))
    if j == 0 :
        return DiffingCell(s[i - 1], '-', table.get(i - 1, j).cost + cost(s[i - 1], '-'))
    
    up = table.get(i - 1, j).cost + cost(s[i - 1], '-')
    left = table.get(i, j - 1).cost + cost('-', t[j - 1])
    leftUp = table.get(i - 1, j - 1).cost + cost(s[i - 1], t[j - 1])

    min_value = min(up, left, leftUp)

    if leftUp == min_value:
        return DiffingCell(s[i - 1], t[j - 1], min_value)
    elif up == min_value:
        return DiffingCell(s[i - 1], '-', min_value)
    else:
        return DiffingCell('-', t[j - 1], min_value)
    

# Input: n and m, represents the sizes of s and t respectively.
# Should return a list of (i,j) tuples, in the order you would like fill_cell to be called
def cell_ordering(n,m):
    res = []
    for i in range(n + 1):
        res.append((i, 0))
    for i in range(1, m + 1):
        res.append((0, i))
    for i in range(1, n+1):
        for j in range(1, m + 1):
            res.append((i, j))
    return res

# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.
def diff_from_table(s, t, table):
    align_s = align_t = ''
    row = len(s)
    col = len(t)
    cost = table.get(row, col).cost
    while row >= 0 and col >= 0:
        char_s, char_t = table.get(row, col).s_char, table.get(row, col).t_char
        if char_s == '-' and char_t == '-':
            break
        if char_s == '-':
            align_s = char_s + align_s
            align_t = char_t + align_t
            col -= 1
        elif char_t == '-':
            align_s = char_s + align_s
            align_t = char_t + align_t 
            row -= 1
        else:
            align_s = char_s + align_s
            align_t = char_t + align_t
            row -= 1
            col -= 1
        
    return (cost, align_s, align_t)


# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char: return 0
        if s_char == 'a':
            if t_char == 'b': return 5
            if t_char == 'c': return 3
            if t_char == '-': return 2
        if s_char == 'b':
            if t_char == 'a': return 1
            if t_char == 'c': return 4
            if t_char == '-': return 2
        if s_char == 'c':
            if t_char == 'a': return 5
            if t_char == 'b': return 5
            if t_char == '-': return 1
        if s_char == '-':
            if t_char == 'a': return 3
            if t_char == 'b': return 3
            if t_char == 'c': return 3

    s = "acb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t, cost=costfunc)
    
    (cost, align_s, align_t) = diff_from_table(s,t, D)
    print align_s
    print align_t
    print "cost was %d"%cost
