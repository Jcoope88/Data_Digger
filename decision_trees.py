import math
from scipy.stats import entropy

data = []
def Entropy(p_plus, p_minus):
    total_count = p_plus + p_minus   
    return entropy([p_plus/total_count,p_minus/total_count], base= 2)

def Information_Gain(parent_values, child_values):
    total_parent = parent_values[0] + parent_values[1]
    avg_child_entropy = 0
    
    for i in child_values:
        avg_child_entropy += Entropy(i[0], i[1]) * ((i[0] + i[1]) / total_parent)

    return Entropy(parent_values[0], parent_values[1]) - avg_child_entropy


def Split_Info(values):
    total = Get_Totals(values)
    
    split_info = 0
    for j in values:
        Ti = j[0] + j[1]
        split_info += -(Ti/total) * math.log(Ti/total, 2)

    return split_info

def Gain_Info(entropy_values, split_values):
    return entropy - split_values


def Gini(p_plus, p_minus):
    total = p_plus + p_minus
    return  1 - (p_plus / total) ** 2 - (p_minus / total) ** 2

def Gini_Index(values):
    total = Get_Totals(values)
    gini_index = 0
    for i in values:
        gini_index += ((i[0] + i[1]) / total) * Gini(i[0],i[1])
    return gini_index

def Get_Totals(values):
    total = 0
    for i in values:
        total += i[0] + i[1]
    
    return total

def Chi_Square(values, col_totals, row_totals):
    total = Get_Totals(values)
    expected_values = [[0,0],[0,0],[0,0]]
    chi_square_values = [[0,0],[0,0],[0,0]]

    for row in range(0,len(expected_values)):
        for col in range(0, len(expected_values[0])):
            expected_values[row][col] = row_totals[row] * col_totals[col] / total 
            chi_square_values[row][col] = ((values[row][col] - expected_values[row][col]) ** 2) / expected_values[row][col]
    
    chi_square = Get_Totals(chi_square_values)
    return chi_square

def Tennis_Example():
    entire = [9,5]
    outlook = [(2,3),(4,0),(3,2)] #sunny, cloudy, rain
    humidity = [(3,4),(6,1)] # high, normal
    wind = [(6,2),(3,2)] # weak, strong
 
    outlook_col_totals = [9,5]
    outlook_row_totals = [5,4,5]
    outlook_values = [[2,3],[4,0],[3,2]]

    expected = [.342]

    print('Gini: ', Gini_Index(outlook))
    gini_index = Gini_Index(outlook)
    assert gini_index == expected
    print('Information Gain:', Information_Gain(entire, outlook))
    print('Split Info:', Split_Info(outlook))
    print('Chi-Square: ', Chi_Square(outlook_values, outlook_col_totals, outlook_row_totals ))
    
def main():
    Tennis_Example()

if __name__ == "__main__":
    main()  