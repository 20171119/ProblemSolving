def solution(new_id):   
    # 1
    new_id = new_id.lower()
    
    # 2
    result = ""
    special_strings = ["-", "_", "."]
    for s in new_id:
        if s.isalnum() or s in special_strings:
            result += s
    new_id = result
    
    # 3
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    
    # 4
    if new_id[0] == ".":
        new_id = new_id[1:] if len(new_id) > 1 else "."
    if new_id[-1] == ".":
        new_id = new_id[:-1]
        
    # 5
    if new_id == "":
        new_id += "a"
        
    # 6
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    
    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

# 다른사람 풀이
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st