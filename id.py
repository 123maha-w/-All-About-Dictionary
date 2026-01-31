student_data = {'id1': 
                    {'name': ['sara'],
                        'class': ['v'], 
                        'subject_integration': ['math , english , science']
                    },
'id2':
        {'name': ['david'],
                        'class': ['v'], 
                        'subject_integration': ['math , english , science']
                    },
'id3':
        {'name': ['sara'],
                        'class': ['v'], 
                        'subject_integration': ['math , english , science']
                    },
'id2':
        {'name': ['suray'],
                        'class': ['v'], 
                        'subject_integration': ['math , english , science']
                    },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print (result)