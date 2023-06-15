#initial_array = ['1234', '1567', '-2', 'computer science']
initial_array = ['Hello', '2', 'world', ':-)']
output_array=[]
for element in initial_array:
    if len(element) <= 3:
        output_array.append(element)
print(f'{initial_array} -> {output_array}')