# logic.py

def generate_table_logic(num):
    result = ""
    for i in range(1, 11):
        result += f"{num} x {i} = {num*i}\n"
    return result