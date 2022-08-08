"""3) написать функцию, которая принимает в качестве аргументов два списка, а возвращает список,
 состоящий из элементов этих двух списков, при чем первый элемент списка - первый элемент первого аргумента,
  второй элемент списка - первый элемент второго списка, третий элемент - второй элемент первого списка,
  четвертый - второй элемент второго аргумента и т.д.

т.е для аргументов [1, 2, 3] и [11, 22, 33] функция должна вернуть [1, 11, 2, 22, 3, 33].
Будет плюсом использование генераторов последовательностей для решения этой задачи."""
# create two lists
list1 = [1, 2, 3]
list2 = [11, 22, 33]

# create a function to combine two lists into one
def union(list1: list, list2: list):
    # set the condition for creating a new list using sequential occurrence of elements
    result = [[list1[i], list2[i]] for i in range(3)]
    # combine all the resulting lists into one
    result = [j for i in result for j in i]
    # we get the result
    return result

print(union(list1, list2))
