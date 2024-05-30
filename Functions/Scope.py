# Local vs global variables
def my_func():
    local_var = "I am local"
    print(local_var)

global_var = "I am global"
my_func()
print(global_var)
