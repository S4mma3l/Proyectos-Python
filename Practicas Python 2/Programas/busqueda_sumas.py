def find_sums(numbers: list, target: int) -> list:

    def find_sum(start: int, target: int, combination: list):

         # encontrar solucion
        if target == 0:
           result.append(combination[:]) # copia superficial
           return
         
         # no hay solucion
        if target < 0 or start == len(numbers):
            return
         
         # busqueda
        for index in range(start, len(numbers)):
              
              if index > start and numbers[index] == numbers[index - 1]:
                  continue
              
              combination.append(numbers[index])
              find_sum(index + 1, target - numbers[index], combination)
              combination.pop()

    numbers.sort()

    result = []

    find_sum(0, target, [])

    return result

print (find_sums([1, 5, 3, 2, 8, 3, 6, 4], 9))