from math import sin, cos, sqrt, atan2, radians 
import json

from geopy import distance
#from PyQt5.QtWidgets import *
#from PyQt5.Qt import *
#from pip._vendor.urllib3.poolmanager import pool_classes_by_scheme

equiv={ '110':'Akademmistechko',
    '111':'Zhytomyrska',
    '112':'Sviatoshyn',
    '113':'Nyvky',
    '114':'Beresteiska' ,
    '115':'Shuliavska' ,
    '116':'Politekhnichnyi instytut' ,
    '117':'Vokzalna',
    '118':'Universytet',
    '119':'Teatralna - Zoloti vorota',
    '120':'Khreshchatyk - Maidan Nezalezhnosti',
    '121':'Arsenalna',
    '122':'Dnipro',
    '123':'Hidropark',
    '124':'Livoberezhna',
    '125': 'Darnytsia',
    '126': 'Chernihivska',
    '127': 'Lisova',
    '210': 'Heroyiv Dnipra',
    '211': 'Minska',
    '212': 'Obolon',
    '213': 'Pochaina',
    '214': 'Tarasa Shevchenka',
    '215': 'Kontraktova ploshcha',
    '216': 'Poshtova ploshcha',
    '218': 'Ploshcha Lva Tolstogo - Palats Sportu',
    '219': 'Olimpiiska',
    '220': 'Palats Ukraina',
    '221': 'Lybidska',
    '222': 'Demiivska',
    '223': 'Holosiivska',
    '224': 'Vasylkivska',
    '225': 'Vystavkovyi tsentr',
    '226': 'Ipodrom',
    '227': 'Teremky',
    '310': 'Syrets',
    '311': 'Dorohozhychi',
    '312': 'Lukianivska',
    '316': 'Klovska',
    '317': 'Pecherska',
    '318': 'Druzhby Narodiv',
    '319': 'Vydubychi', 
    '321': 'Slavutych',
    '322': 'Osokorky',
    '323': 'Pozniaky',
    '324': 'Kharkivska',
    '325': 'Vyrlytsia',
    '326': 'Boryspilska',
    '327': 'Chervonyi khutir'
    }

equiv2={ 
    '110: Akademmistechko': '110',
    '111: Zhytomyrska': '111',
    '112: Sviatoshyn': '112',
    '113: Nyvky': '113',
    '114: Beresteiska': '114',
    '115: Shuliavska': '115',
    '116: Politekhnichnyi instytut': '116',
    '117: Vokzalna' : '117',
    '118: Universytet': '118',
    '119-314: Teatralna - Zoloti vorota':'119',
    '120-217: Khreshchatyk - Maidan Nezalezhnosti': '120',
    '121: Arsenalna': '121',
    '122: Dnipro': '122',
    '123: Hidropark': '123',
    '124: Livoberezhna':'124',
    '125: Darnytsia': '125',
    '126: Chernihivska': '126',
    '127: Lisova': '127',
    '210: Heroyiv Dnipra': '210',
    '211: Minska': '211',
    '212: Obolon': '212',
    '213: Pochaina': '213',
    '214: Tarasa Shevchenka': '214',
    '215: Kontraktova ploshcha':'215',
    '216: Poshtova ploshcha': '216',
    '218-315: Ploshcha Lva Tolstogo - Palats Sportu':'218',
    '219: Olimpiiska':'219',
    '220: Palats Ukraina':'220',
    '221: Lybidska':'221',
    '222: Demiivska':'222',
    '223: Holosiivska':'223',
    '224: Vasylkivska':'224',
    '225: Vystavkovyi tsentr':'225',
    '226: Ipodrom': '226',
    '227: Teremky': '227',
    '310: Syrets': '310',
    '311: Dorohozhychi': '311',
    '312: Lukianivska': '312',
    '316: Klovska': '316',
    '317: Pecherska': '317',
    '318: Druzhby Narodiv': '318',
    '319: Vydubychi': '319', 
    '321: Slavutych': '321',
    '322: Osokorky': '322',
    '323: Pozniaky': '323',
    '324: Kharkivska': '324',
    '325: Vyrlytsia': '325',
    '326: Boryspilska': '326',
    '327: Chervonyi khutir': '327'
    }

h={ 
    'Akademmistechko': [50.46516, 30.35505,'110'],
    'Zhytomyrska': [50.45628, 30.36546,'111'],
    'Sviatoshyn': [50.45776, 30.39219,'112'],
    'Nyvky': [50.45931, 30.40417,'113'],
    'Beresteiska': [50.45948, 30.41864,'114'],
    'Shuliavska': [50.45451, 30.44876,'115'],
    'Politekhnichnyi instytut': [50.45143, 30.46427,'116'],
    'Vokzalna'	: [50.44159, 30.48980,'117'],
    'Universytet':[50.44347, 30.50485,'118'],
    'Teatralna - Zoloti vorota': [50.44545, 30.51530,'119'],
    'Khreshchatyk - Maidan Nezalezhnosti': [50.44776, 30.52403,'120'],
    'Arsenalna': [50.44330, 30.54721,'121'],
    'Dnipro': [50.44123, 30.55933,'122'],
    'Hidropark': [50.44598, 30.57688,'123'],
    'Livoberezhna':[50.45187, 30.59815,'124'],
    'Darnytsia': [50.45597, 30.61296,'125'],
    'Chernihivska': [50.45990, 30.63028,'126'],
    'Lisova': [50.6467, 30.64555,'127'],
    'Heroyiv Dnipra': [50.52274, 30.49887,'210'],
    'Minska': [50.51224, 30.49855,'211'],
    'Obolon': [50.50156, 30.49823,'212'],
    'Pochaina': [50.48608, 30.49785,'213'],
    'Tarasa Shevchenka': [50.47400, 30.50381,'214'],
    'Kontraktova ploshcha':[50.46592, 30.51503,'215'],
    'Poshtova ploshcha': [50.45927, 30.52441,'216'],
    'Ploshcha Lva Tolstogo - Palats Sportu': [50.43993, 30.51889,'218'],
    'Olimpiiska': [50.43129, 30.51687,'219'],
    'Palats Ukraina': [50.42142, 30.52076,'220'],
    'Lybidska':	[50.41399, 30.52488,'221'],
    'Demiivska': [50.40478, 30.51688,'222'],
    'Holosiivska': [50.39739, 30.50825,'223'],
    'Vasylkivska': [50.39334, 30.48818,'224'],
    'Vystavkovyi tsentr': [50.38244, 30.47757,'225'],
    'Ipodrom': [50.37659, 30.46884,'226'],
    'Teremky': [50.36710, 30.45414,'227'],
    'Syrets': [50.47674, 30.43279, '310'],
    'Dorohozhychi': [50.47343, 30.44912, '311'],
    'Lukianivska': [50.46115, 30.48365, '312'],
    'Klovska': [50.43697, 30.53182, '316'],
    'Pecherska': [50.42728, 30.53938, '317'],
    'Druzhby Narodiv': [50.41703, 30.54731, '318'],
    'Vydubychi': [50.40183, 30.56049, '319'], 
    'Slavutych': [50.39426, 30.60487, '321'],
    'Osokorky': [50.39526, 30.61623, '322'],
    'Pozniaky': [50.39787, 30.63474, '323'],
    'Kharkivska': [50.40068, 30.65209, '324'],
    'Vyrlytsia': [50.40295, 30.66691, '325'],
    'Boryspilska': [50.40341, 30.68436, '326'],
    'Chervonyi khutir': [50.40948, 30.69621, '327']
    }
#h[nombretoraro

def DistanciaAerea(origen, destino): #111->equiv
    global h,g
    x=(h[equiv[origen]][0],h[equiv[origen]][1])
    y=(h[equiv[destino]][0],h[equiv[destino]][1])
    return distance.distance(x, y).km
    
#adjacentes    
# key : values[Par(linea,valor)] en km
f = {   
        '110': [('111',1.53)],
		'111': [('110',1.53), ('112',1.8)],
		'112': [('111',1.8), ('113',0.98)],
		'113': [('112',0.98), ('114',1.02)],
		'114': [('113',1.02), ('115',2.23)],
		'115': [('114',2.23), ('116',1.16)],
		'116': [('115',1.16), ('117',2.18)],
		'117': [('116',2.18), ('118',1.11)],
		'118': [('117',1.11), ('119',0.81)],
		'119': [('312',3.12), ('118',0.81), ('120',0.6), ('218',0.77)],
        '120': [('119',0.6), ('121',1.78), ('216',1.34), ('218',1.05)],
        '121': [('120',1.78), ('122',0.9)],
        '122': [('121',0.9), ('123', 1.36)],
        '123': [('122',1.36), ('124',1.64)],
        '124': [('123',1.64), ('125',1.14)],
        '125': [('124',1.14), ('126',1.3)],
        '126': [('125', 1.3), ('127', 1.21)],
        '127': [('126',1.21)],
        
        '210': [('211', 1.17)],
        '211': [('210', 1.17), ('212', 1.19)],
        '212': [('211', 1.19), ('213', 1.71)],
        '213': [('212', 1.71), ('214', 1.46)],
        '214': [('213', 1.46), ('215', 1.19)],
        '215': [('214', 1.19), ('216', 1.05)],
        '216': [('215', 1.05), ('120', 1.34)], #217 es 120
        '218': [('119', 0.77), ('120', 1.05), ('219', 1.08), ('316', 0.94)],
        '219': [('218', 1.08), ('220', 1.13)],
        '220': [('219', 1.13), ('221', 0.88)],
        '221': [('220', 0.88), ('222', 1.21)],
        '222': [('221', 1.21), ('223', 1.05)],
        '223': [('222', 1.05), ('224', 1.49)],
        '224': [('223', 1.49), ('225', 1.51)],
        '225': [('224', 1.51), ('226', 0.92)],
        '226': [('225', 0.92), ('227', 1.48)],
        '227': [('226', 1.48)],
        
        '310' : [('311', 1.34)],
        '311' : [('310', 1.34), ('312', 3.02)], 
        '312' : [('311', 3.02), ('119', 3.12)], #119 == 314
        '316' : [('218', 0.94), ('317',1.23)],  #218 == 315 
        '317' : [('316', 1.23), ('318',1.27)],
        '318' : [('317', 1.27), ('319', 1.93)],
        '319' : [('318', 1.93), ('321', 3.40)],
        '321' : [('319', 3.40), ('322', 0.82)],
        '322' : [('321', 0.82), ('323', 1.34)],
        '323' : [('322', 1.34), ('324', 1.27)],
        '324' : [('323', 1.27), ('325', 1.08)],
        '325' : [('324', 1.08), ('326', 1.29)],
        '326' : [('325', 1.29), ('327', 1.09)],
        '327' : [('326', 1.09)]
    }

g = { 	'110-111': 1.53,
		'111-112': 1.80,
		'112-113': 0.98,
		'113-114': 1.02,
		'114-115': 2.23,
		'115-116': 1.16,
		'116-117': 2.18,
		'117-118': 1.11,
		'118-119': 0.81,
		'119-120': 0.60,
		'120-121': 1.78,
		'121-122': 0.90,
		'122-123': 1.36,
		'123-124': 1.64,
		'124-125': 1.14,
		'125-126': 1.30,
		'126-127': 1.21,
		
		'210-211': 1.17,
		'211-212': 1.19,
		'212-213': 1.71,
		'213-214': 1.46,
		'214-215': 1.19,
		'215-216': 1.05,
		'216-120': 1.34,
		'120-218': 1.05,
		'218-219': 1.08,
		'219-220': 1.13,
		'220-221': 0.88,
		'221-222': 1.21,
		'222-223': 1.05,
		'223-224': 1.49,
		'224-225': 1.51,
		'225-226': 0.92,
		'226-227': 1.48,
		
		'310-311': 1.34,
		'311-312': 3.02,
		'312-119': 3.12,
		'119-218': 0.77,
		'218-316': 0.94,
		'316-317': 1.23,
		'317-318': 1.27,
		'318-319': 1.93,
		'319-321': 3.40,
		'321-322': 0.82,
		'322-323': 1.34,
		'323-324': 1.27,
		'324-325': 1.08,
		'325-326': 1.29,
		'326-327': 1.09
}


def get_vecinos(v):
    return f[v]

def algoritmo_a_estrella(origen,destino):
    global g, h
    abiertos=set([origen])
    cerrados=set([])
    #contiene presets de distancias de el origen a todos los otros nodos
    poo={}
    poo[origen]=0   #valor por defecto +infinito
    
    #contiene mapa de adjacentes
    par={} 
    par[origen]=origen
    while len(abiertos)>0:
        n=None #nodo actual
        
        #encuentra el nodo con el menor valor de f()
        for v in abiertos: #quitado h[v] y h[n]
            if n==None or poo[v] + DistanciaAerea(v, destino)  < poo[n] + DistanciaAerea(n, destino) :
                    n=v;
        if n==None:
            print("No se encuentra el camino")
            return None
        
        if n==destino:
            reconstruye_camino=[]
            while par[n]!=n:
                reconstruye_camino.append(n)
                n=par[n]
            reconstruye_camino.append(origen)
            reconstruye_camino.reverse()
            
            print('Camino encontrado: {}'.format(reconstruye_camino))
            return reconstruye_camino
        #para todos los vecinos
        for (m, peso) in get_vecinos(n):
            #si el nodo actual no esta presente en la lista abierta y la lista cerrada
            #lo anade a la lista abierta y lo nota n como par
            if m not in abiertos and m not in cerrados:
                abiertos.add(m)
                par[m]=n
                poo[m]=poo[n]+peso
            else:
                if poo[m] > poo[n] + peso:
                    poo[m] = poo[n] + peso
                    par[m] = n
                    
                    if m in cerrados:
                        cerrados.remove(m)
                        abiertos.add(m)
        # quita n de la lista bierta y la anade a la cerrada
        #por que se han inspeccionado todos sus vecinos
        abiertos.remove(n)
        cerrados.add(n)
    print('Camino no existe!')
    return None          