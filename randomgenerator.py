# Copyright Lukas Pellny | 2023
import random

Lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
Capitalized_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '012345678'
symbols = '1§$%&=?#'
Execution = Lowercase_letters + Capitalized_letters + numbers + symbols
length = 9
password = ''.join(random.sample(Execution, length))
print(password) 

