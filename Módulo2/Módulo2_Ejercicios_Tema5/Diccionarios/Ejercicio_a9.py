'''
9. Haz un programa que obtenga la clave de un valor mínimo del siguiente diccionario.
Input:
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
Output: Math 
'''
if __name__ == '__main__':
    d = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }
    mini = min(d.values())
    
    print('El valor minimo es: {}'.format(mini))
    
    print(min(d, key=d.get))