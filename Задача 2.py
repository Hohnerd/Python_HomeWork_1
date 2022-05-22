# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

First_string = "many animals are in danger because man is destroying their environment "
Second_string = "an"
 
def str_count(str, substr):
    return 0 if len(str) < len(substr) else str.startswith(substr) + str_count(str[1:], substr)
 
print(str_count(First_string, Second_string))