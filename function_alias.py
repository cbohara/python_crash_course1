"""
if the name of a function you are importing might conflict with an existing
name in your program or if the function name is long, you can use a short, unique
alais when you import the function using 'as'

from module_name import function_name as alias
"""
from pizza_module import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'glitter', 'unicorns')
