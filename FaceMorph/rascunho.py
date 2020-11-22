# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:15:13 2020

@author: Joao
"""
def write_txt(conteudo, filename):
    points = []
    for i in range(len(conteudo)):
        if i != (len(conteudo)-1):
            points.append(f"{conteudo[i][0]} {conteudo[i][1]}\n")
        else:
            points.append(f"{conteudo[i][0]} {conteudo[i][1]}")
           arquivo = open(filename + ".txt", 'w') 
    arquivo.writelines(points)
    arquivo.close()
    
biden = [[475 ,390],[264, 736],[0, 774],[599 ,600],[0, 0],[0 ,400],[0 ,799],[300, 799],[599, 799],[599, 400],[599, 0],[300, 0]]
       
bonoro =  [[437 ,230],[270, 680],[0, 460],[599 ,420],[0, 0],[0 ,230],[0 ,799],[300, 799],[599, 799],[599, 230],[599, 0],[300, 0]]

lula = [[460 ,290],[197, 718],[0, 505],[599, 452],[0, 0],[0, 290],[0, 799],[300, 799],[599, 799],[599, 290],[599, 0],[300, 0]]

yuri = [[390 ,200],[300, 400],[0, 350],[599 ,350],[0, 0],[0 ,200],[0 ,799],[300, 799],[599, 799],[599, 200],[599, 0],[300, 0]]