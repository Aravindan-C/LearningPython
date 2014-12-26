f = open("foo.txt")
"""line = f.readline()
while line :
    print line
    line = f.readline()
f.close()"""
for line in f :
    entry = eval(line)
    strategy=entry[0]
    asset_name=entry[1]
    asset_id=entry[2]
    type=entry[3]
    algo_config_id=entry[4]
    po_config_id=entry[5]
    account_id=entry[6]
    print strategy,asset_name,asset_id,type,algo_config_id,po_config_id,account_id
f.close()
