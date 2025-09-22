student_data={'id1':
    {'name':['sara'],
     'class':['V'],
     'subject_intergation': ['english, math, science']
    },
    'id2':
    {'name':['david'],
     'class':['V'],
     'subject_intergation': ['art, math, biology']
    },
    'id3':
    {'name':['sara'],
    'class':['V'],
    'subject_intergation': ['english, math, science']
    },
    'id4':
    {'name':['surya'],
     'class':['V'],
     'subject_intergation': ['english, math, science']
    },
}
result={}
for key, value in student_data.items():
    if value not in result.values ():
        result[key]=value
print(result)




