import csv

statistiques_basiques=open('statistiques_basiques.csv','r',encoding='utf8')
tirs=open('tirs.csv','r',encoding='utf8')
passes=open('passes.csv','r',encoding='utf8')
types_de_passes=open('types_de_passes.csv','r',encoding='utf8')
actions_defensives=open('actions_defensives.csv','r',encoding='utf8')
statistiques_diverses=open('statistiques_diverses.csv','r',encoding='utf8')
preparation_des_tirs=open('preparation_des_tirs.csv','r',encoding='utf8')
possessions=open('possessions.csv','r',encoding='utf8')


statistiques_basiques_mineur=open('statistiques_basiques_mineur.csv','r',encoding='utf8')
tirs_mineur=open('tirs_mineur.csv','r',encoding='utf8')
passes_mineur=open('passes_mineur.csv','r',encoding='utf8')
types_de_passes_mineur=open('types_de_passes_mineur.csv','r',encoding='utf8')
actions_defensives_mineur=open('actions_defensives_mineur.csv','r',encoding='utf8')
statistiques_diverses_mineur=open('statistiques_diverses_mineur.csv','r',encoding='utf8')
preparation_des_tirs_mineur=open('preparation_des_tirs_mineur.csv','r',encoding='utf8')
possessions_mineur=open('possessions_mineur.csv','r',encoding='utf8')

data_mineur=[[]for i in range(3464)]
definition_mineur=[]

data=[[] for i in range(2889)]
definition=[]

def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False
    
    
def first_occ(tab,elem):
    for i in range(len(tab)):
        if (tab[i]==elem):
            return i
    return -1

def convert_minute(minstr):
    if type(minstr)==str:
        minint=0
        e=len(minstr)-1
        if e>3:
            e-=1
            for i in minstr:
                if i.isdigit():
                    minint+= int(i)*(10**e)
                    e-=1
        return minint
    else:
        return minstr




    
def add_data(data,definition,file,debut):
    mot=csv.reader(file, delimiter=',')
    j=0
    defajoutee=False
    for i in mot:
        n=len(i)
        if i[0].isdigit():
            n=len(i)
            for k in range(debut,n-1):
                if i[k] not in ['eng Premier League','de Bundesliga','it Serie A','fr Ligue 1','es La Liga']:
                    if is_float(i[k]):
                        data[j].append(float(i[k]))
                    else:
                        if (i[k]=='')or (i[k]=='#ERROR!'):
                            data[j].append(0)
                        else:
                            if(i[k] in ['MT,AT','AT,MT','DF,AT','AT,DF','DF,MT','MT,DF']):
                                data[j].append(i[k][:2])
                            else:
                                data[j].append(i[k])
            j+=1
        else:
            if (i[0]=='Clt') and (not defajoutee) :
                defajoutee=True
                for k in range(debut,n-1):
                    if i[k]!= 'Comp':
                        definition.append(i[k])
              
                    
def minute_in_data(data,definition):
    ind=first_occ(definition, 'Min')
    for i in range(len(data)):
        m=convert_minute(data[i][ind])
        data[i][ind]=m
        
add_data(data_mineur,definition_mineur,statistiques_basiques_mineur, 1)
add_data(data_mineur,definition_mineur,tirs_mineur, 8)
add_data(data_mineur,definition_mineur,passes_mineur,8)
add_data(data_mineur,definition_mineur,types_de_passes_mineur, 8)
add_data(data_mineur,definition_mineur,actions_defensives_mineur, 8)
add_data(data_mineur,definition_mineur,statistiques_diverses_mineur, 8)
add_data(data_mineur,definition_mineur,preparation_des_tirs_mineur, 8)
add_data(data_mineur,definition_mineur,possessions_mineur,8)      
                          
add_data(data,definition,statistiques_basiques,1)
add_data(data,definition,tirs, 9)
add_data(data,definition,passes,9)
add_data(data,definition,types_de_passes, 9)
add_data(data,definition,actions_defensives, 9)
add_data(data,definition,statistiques_diverses, 9)
add_data(data,definition,preparation_des_tirs, 9)
add_data(data,definition,possessions,9)

minute_in_data(data,definition)
minute_in_data(data_mineur, definition_mineur)

data_global=data+data_mineur


def cree_fichier(data):
    fichier=open('data_global.csv','w',encoding='utf8')
    for i in range(len(definition)-1) : 
        fichier.write(definition[i])
        fichier.write(';')
    fichier.write(definition[-1])    
    fichier.write('\n')
    for i in range(len(data)):
        for j in range(len(definition)-1):
            fichier.write(str(data[i][j]))
            fichier.write(';')
        fichier.write(str(data[i][-1]))
        fichier.write('\n')
    return    
    
    
cree_fichier(data_global)
    
    
    
statistiques_basiques.close()
tirs.close()
passes.close()
types_de_passes.close()
actions_defensives.close()
statistiques_diverses.close()
preparation_des_tirs.close()
possessions.close()


statistiques_basiques_mineur.close()
tirs_mineur.close()
passes_mineur.close()
types_de_passes_mineur.close()
actions_defensives_mineur.close()
statistiques_diverses_mineur.close()
preparation_des_tirs_mineur.close()
possessions_mineur.close()