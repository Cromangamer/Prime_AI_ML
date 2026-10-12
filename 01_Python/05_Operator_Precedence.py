# Operator Precedence
# 1. Parentheses ()
# 2. Exponentiation (**)
# 3. Unary + and -
# 4. Multiplication *, Division /, Floor Division //, Modulus %
# 5. Addition + and Subtraction -
# 6. Comparison Operators (==, !=, >, <, >=, <=)
# 7. Logical NOT (not)
# 8. Logical AND (and)
# 9. Logical OR (or)
# 10. Assignment Operators (=, +=, -=, *=, /=, %=, **=, //=)
# Example of Operator Precedence
result = 2 + 3 * 4  # Multiplication has higher precedence than addition
print(result)  # Output: 14


# and whe the same precedence is there then it will be evaluated from left to right
# 2 + 3 + 4
# -> 5 + 4
# -> 9

# Priority	Operators	                      Meaning 	                      Example
# 1	          ()	                        Parentheses	                      (2 + 3)
# 2	          **	                           Power	                      2 ** 3
# 3	         +x, -x	                       Unary plus/minus	                    -5
# 4	      *, /, //, %	       Multiply, divide, floor divide, remainder	  10 % 3
# 5	        +, -	                      Addition, subtraction	               5 + 2
# 6	   ==, !=, >, <, >=, <=	                  Comparisons	                   5 > 3
# 7	         not	                      Logical NOT	                      not True
# 8	         and	                      Logical AND	                   True and False
# 9	          or	                     Logical OR	                       True or False

