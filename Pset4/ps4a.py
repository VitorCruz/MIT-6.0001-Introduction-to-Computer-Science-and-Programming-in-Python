
# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''   
       
    if len(sequence) == 1:       
        return sequence
    
    else:                  
        
        letter = sequence[-1:]
        result = get_permutations(sequence[:-1])         
        
        aux_list = []       
           
        for i in range(len(result)):
            for j in range(len(result[0])+1):
                obj = result[i]
                obj2 = obj[:j] + letter[0] + obj[j:]                
                aux_list.append(obj2)  
                
        return aux_list            


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    example_input = 'abc'
    print("Unit Test 1")
    print('Input:', example_input)
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print('Expected Output:', expected)
    actual_output = get_permutations(example_input)
    print('Actual Output:', actual_output)
    
    for i in expected:
        if i not in actual_output:
            print("Unit Test 1: FAILED")
            break
    print("Unit Test 1: SUCCESS")
    
    
    print()
    print("------------------------------------------")
    print()
    
    example_input2 = 'zy'
    print("Unit Test 2")
    print('Input:', example_input2)
    expected2 = ['yz','zy']
    print('Expected Output:', expected2)
    actual_output2 = get_permutations(example_input2)
    print('Actual Output:', actual_output2)
    
    for i in expected2:
        if i not in actual_output2:
            print("Unit Test 2: FAILED")
            break
    print("Unit Test 2: SUCCESS")
    
    print()
    print("------------------------------------------")
    print()
    
    example_input3 = 'abcd'
    print("Unit Test 2")
    print('Input:', example_input3)
    expected3 = ['dcba','cdba','cbda','cbad','dcab','cdab','cadb','cabd','dbca','bdca','bcda','bcad','dacb','adcb','acdb','acbd','dbac','bdac','badc','bacd','dabc','adbc','abdc','abcd']
    print('Expected Output:', expected3)
    actual_output3 = get_permutations(example_input3)
    print('Actual Output:', actual_output3)
    
    for i in expected3:
        if i not in actual_output3:
            print("Unit Test 3: FAILED")
            break
    print("Unit Test 3: SUCCESS")
    
    

    






