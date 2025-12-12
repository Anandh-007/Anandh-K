def series_problem_3(a: int):
    if a <= 0:
        return []
      
    if a % 2 == 0:
        k = a - 1
    else:
        k = a

    result = []
    for i in range(1, k + 1):
        result.append(2 * i - 1)
    return result


print(series_problem_3(1))  
print(series_problem_3(2))  
print(series_problem_3(3)) 
print(series_problem_3(4)) 

 
