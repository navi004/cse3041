
def inv_dic(d):
    new_d = {}
    for keys in d:
        new_keys  = d[keys]
        
         #if the key doesnot exist in the dic
        if not(new_keys in new_d):
            new_d[new_keys] = [keys]
        else:
            new_d[new_keys].append(keys)
    return new_d

