"""4) Написать функцию которая принимает в качестве аргумента строку, и возвращает object True,
 если строка является полиндромом и object False если нет."""
# create a function to search for polydromes
def polidrom(x: str):
    # set the matching condition
    if x.lower() == x.lower()[::-1]:
        # if the condition is met then the result is
        return "Object True"
    # if the condition is not met then the result is
    return "Object False"

print(polidrom('madam'))
