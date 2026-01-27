a = input('Digite allgo: ')
print(f'Qual o tipo?', type(a),
      '\nÉ só espaço? ' ,a.isspace(),
      '\né numerico? ', a.isnumeric(),
      '\nÉ alfabéto?', a.isalpha(),
      '\nAlfa numerico? ', a.isalnum(),
      '\nEstá em maiuscúlo?', a.isupper(),
      '\nEstá em minuscúlo?',a.islower(),
      '\nEsta capitalizada?',a.istitle())