'''
5. Haz un programa que lea un número y que lo escriba del revés.
'''
if __name__ == '__main__':
    num = input()
    for i in range(len(num), 0, -1):
        print(num[i-1], end="")