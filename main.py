from collections import deque

#Структуры данных
# Стек - Lifo последний зашел,поледний вышел
# Очень - Fifo первый зашел, первый вышел

# d = deque()
# d .append(1)
# d .append(2)
# d .appendleft(0)
# d .appendleft(-1)
# print(d)

# print(d.pop())
# print(d.pop())
# print(d)

# d.extened([8, 8, 8])
# d.extendleft([1, 1, 1])
# print(d)

# d.clear()
# print(d)



# stack = deque()

# stack.append(1)
# stack.append(2)
# stack.append(3)

 # print(f"Стек после добавление элеьентов -{stacr} ")

# print(f"Удаляем элемент {stack}")
# print(f"Удаляем элемент {stack}")

# print(stack)

def validate(s):
    #Создаем стек на основе deque() Для эффективности работы
    stack = deque()
    #Создаем словарь ключ-значение с скобками для отслеживание правительности
    br = {")": "(", "]" : "[", "}": "{"}
    
    #Перебераем каждую скобку из "s"
    for char in s:
        #если скобка являются открывающей
        if char in br.values():
            #добовляем стек
            stack.append(char)
        elif char in br.keys():
            # правильная по отношению к последней в стеке
            if not stack or stack.pop() != [char]: 
                #Вoзвращаем false
                return False
     
    #если стек пустой после проверки возвращаем True=
    return not stack
 
print(validate("({[]})"))
print(validate("({[]})"))