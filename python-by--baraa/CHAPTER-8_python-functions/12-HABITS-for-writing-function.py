# This is a function styling guide


# BAD STYLE
def DiscPrint(p, r):
    print("calculating discount")
    p = p - (p * r/100)
    print(p)

DiscPrint(80, 20)



# Correction 
def calculate_discount(price: float, rate: float)-> float:
    """
    Calculate the final price after applying a discount.
    Args:
        price (float) : Original Product price.
        rate (float): Discount Rate as number (e.g 20 for 20%).
    Returns:
        final_price (float): Final price after applying discount.
    """
    return price - (price * rate / 100)

print(calculate_discount(100, 20))



# Rule no 1: follow naming convention of snake_case
# lower case and word seperated by _ (userscores)
# correction : disc_print


# Rule no 2: function name should clearly describe what it does
# start with a verb, user full word avoid abbreviations
# correction: calculate_discount()


# Rule no 3: Parameter names describe their values
# use full, meaningful words
# avoid abbreviations and single letters
# correction: price, rate


# Rule no 4: Always describe functions using Docstring
# help teammates understand your code
# help future you remember the logic
# DOCSTRING - a short text on the first line inside a function that explains what the function does
# """  """
# Docstring --> python stores it inside the function and can be resued by tools, editors
# python return the documentation of a function
# help(calculate_discount) # for this the function need to return atlest something


# Rule no 5: Replace Prints with return to send data back to the programm


# Rule no 6: Don't change parameter values directly, create local variables for any processing
# correction new local final_price


# Suggestion: put simple calculation directy inside the return statement instead of storing then in extra variable


#---------***************--------------
# Modern RULES not included in pep8
# followed by professonal

# Rule no 7: Use data type hint
# always add type hints to parameters and return to make the function easier to understand
# def calculate_discount(price: float, rate:float):
# this is only for use as a hint not for python
# for return value hint
# def calculate_discount(price: float, rate: float)-> float:


# Rule no 8: Explain Args and return in Docstring
# always describe what goes in and what comes out of the function in the docstring
