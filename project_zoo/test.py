dic = {
    "An": 8.5,
    "Bình": 7.0,
    "Cường": 9.2,
    "Hanh": 7.0,
    "Lam": 8.5,
    "Que": 7.0
}

dic_score = {}
dic_overlap = {}
def add_people(new_people):
    dic[new_people] = 10.0


def max_people():
    mx = max(dic.values())
    print(mx)

def processing():
    for k, v in dic.items():
        if( dic_score.get(v, False) == False):
            dic_score[v] = k
        else:
            dic_overlap[k] = v 
    


def display_info():
    for k, v in dic_score.items():
        print(dic[v])
        if( dic_overlap.get(v, False) != False):
            for k in dic_overlap.keys():
                if(dic_overlap[k] == v):
                    print(dic_overlap[k])

processing()
print(dic.get("Hanh", False) == False)
