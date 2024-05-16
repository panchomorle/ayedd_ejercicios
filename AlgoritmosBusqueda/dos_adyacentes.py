arr = [1,3,4,5,9,12]

def algoritmo(arr: list, x: int):
    for i in range(len(arr)):
        if i+1 > len(arr)-1:
            break
        if arr[i] + arr[i+1] == x:
            print(f"Se encontró {x} sumando las posiciones {i} y {i+1}")
            return True
    print("No se encontraron números")
    return False

algoritmo(arr, 30)