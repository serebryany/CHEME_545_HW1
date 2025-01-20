#Solution 2: Using try-except block
#See solution 1 and additional comments in Jupyter Notebook

#define function and the inputs
def extract_parameter(unit_name, parameter_name, index): 
    #tries to access the data in the dictionary and return a string with the information from it
    try: return f"{unit_name}_{parameter_name}_{unit_operations_data[unit_name][parameter_name][index]}"
    #if it can't find that data in the dictionary an error message is printed
    except (KeyError, IndexError): return "Invalid Input"
        
