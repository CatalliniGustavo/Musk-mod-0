if __name__ == '__main__':
    lista = [[56, 34, 1],
             [12, 4, 5],
             [9, 4, 3]]
    for i in lista:
        print(i)
        
    print()
    
    for i in lista:
        for j in i:
            if j < 10:
                print('[ ',j,'] ', end='')
            else:
                print('[',j,'] ', end='')
                
        print()
    
