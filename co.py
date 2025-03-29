def find_cube_pairs(target) :
    solutions = []
    max_num = round(target ** (1/3))  

    for a in range(1, max_num + 1) :
        for b in range(a, max_num + 1) :
            if a**3 + b**3 == target :
                solutions.append((a, b))
    return solutions

pairs = find_cube_pairs(1729)
print("Valid cube pairs for 1729:")
for a, b in pairs :
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")
"""Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""

##made printf to print
##removed semi colons
##removed commas from end of statements
##added colons to end of  loops and if conditions and function definition
## changed *** to ** for getting power of the number
##changed 1728 to 1729 in print statement
##changed targ to targets and sol to solutions (because those were the actual variable names
##changed ranges to range
##changed pair to pairs
##changed 2 to 3 print statement
