p1 = {
    'name': 'Luiz',
    'lastname':'Silva'
}

#print(p1.get('name'))  # Output: Luiz  

#nome = p1.pop('name')  # Remove 'name' from p1 and returns its value
#last_key = p1.popitem()  # Removes the last inserted key-value pair and returns it
#print(last_key)  # Output: ('lastname', 'Silva')
#print(nome)  # Output: Luiz
#print(p1)  # Output: {'lastname': 'Silva'}

p1.update(
    {
        'name': 'New Name',
        'age': 30
    }
)

print(p1)