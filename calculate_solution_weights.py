#Solution 2 Using try-except block
#See solution 1 and additional comments in Jupyter Notebook

#define the function and its inputs
def calculate_solution_weights(molecular_weights, solutions_needed):
    #start with an empty result to keep adding to
    result = []
    #loop through all the input chemicals
    for solution in solutions_needed: 
        try:
            #separate the chemical name (first half) from the concentration (second half)
            name, concentration = solution.split('-')
            #remove the last character 'M' and convert the concentration to a float
            concentration = float(concentration[:-1])
            if name in molecular_weights:
                #get the molecular weight from the list
                molecular_weight = molecular_weights[name]
                #calculate the weight
                weight = molecular_weight * concentration
                #add the calculated weight to the result
                result.append(f"{name}-{concentration}M-{weight}g")
            else: result.append("unknown")
        except ValueError: result.append("unknown")
    return result