#my_list = [('test1','sev',1,2), ('test2','sev',1,2)]
my_list = []

def Test():
    cdets_sr_vol = list()
    for row_cdets in my_list:
        cdets_tup = [row_cdets[0]]
        cdets_sr_vol.append(cdets_tup)
        if len(cdets_sr_vol) == 0:
            break
    print(cdets_sr_vol)
    print(len(cdets_sr_vol))
    return cdets_sr_vol
    

Test()


t = Test()
print()
print('t')
print(t)


