

def add(a,b):
  return a + b
def sub(a,b):
    return a - b
def mul(a,b):
  return a * b
def div(a,b):
    return a / b

dictionary = {
  1: add,
  2: sub,
  3: mul,
  4: div
}


operation = int(input("Kalkulator: Prosze wybrac numer dla wybranego działania: 1.dodawanie 2.odejmowanie 3.mnozenie 4. dzielenie:"))


a,b = int(input("A =")), int(input("B ="))

function_to_execute = dictionary[operation]

result = function_to_execute(a, b)

print(result)




