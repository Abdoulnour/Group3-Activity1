example_lin1= "     Hello"
print(example_lin1.strip())

example_lin2= "Hello world"
print(example_lin2.split())

example_add = ' 3'+' 2'
print("without strip and split",example_add)

stripExample = example_add.strip()
print(stripExample)

sum=0
for num in stripExample.split():
    sum = sum+int(num)
    print(sum)



