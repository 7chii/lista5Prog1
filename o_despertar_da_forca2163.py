N, M = map(int, input().split())
matriz = []
pos_primeiro_aura = []
pos_miolo_aura = []
pos_final_aura = []
for y in range(N):
    linha = list(map(int,input().split()))
    matriz.append(linha)

    if(len(pos_primeiro_aura) > 0 and len(pos_miolo_aura) >0 and len(pos_final_aura) >0):
        break
    
    if(len(pos_primeiro_aura)==0):
            for x in range(M-3):
                if matriz[y][x] == 7 and matriz[y][x+1] == 7 and matriz[y][x+2] == 7:
                   # print("encontrado primeira linha")
                    pos_primeiro_aura.append(x)
                    pos_primeiro_aura.append(y)
    if (len(pos_miolo_aura) == 0 and len(pos_primeiro_aura) > 0):
                if matriz[y][pos_primeiro_aura[0]] == 7 and matriz[y][pos_primeiro_aura[0]+1] == 42 and matriz[y][pos_primeiro_aura[0]+2] == 7:
                    #print("encontrado segunda linha")
                    pos_miolo_aura.append(pos_primeiro_aura[0]+1)
                    pos_miolo_aura.append(y)
    if (len(pos_final_aura) == 0 and len(pos_miolo_aura) > 0):
                if matriz[y][pos_miolo_aura[0]] == 7 and matriz[y][pos_miolo_aura[0]+1] == 7 and matriz[y][pos_miolo_aura[0]+1] == 7:
                    #print("encontrado terceira linha")
                    pos_miolo_aura.append(pos_miolo_aura[0])
                    pos_miolo_aura.append(y)
    if (len(pos_miolo_aura) == 0 or len(pos_final_aura) == 0) and len(pos_primeiro_aura) == 0 :
        pos_primeiro_aura.clear()
        pos_miolo_aura.clear()
        pos_final_aura.clear()
#print(matriz)
if len(pos_miolo_aura) > 0 :
    
    print(f'{pos_miolo_aura[1] + 1} {pos_miolo_aura[0]+1}')

else:
    print('0 0')


