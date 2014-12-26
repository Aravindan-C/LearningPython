from ceres.strategy_config.trading_algo_config import AlgoConfigGenerator,AlgoConfigContainer

__author__ = 'aravindan'
f = open("test_file.txt")
account_id_symbol_map1={}
account_id_symbol_map2={}
algo_config_id_symbol_map1={}
algo_config_id_symbol_map2={}
account_id_used=["CSTLNM26","CSTLNM85"]
for line in f :
    entry = eval(line)
    strategy=entry[0]
    asset_name=entry[1]
    asset_id=entry[2]
    type=entry[3]
    algo_config_id=entry[4]
    po_config_id=entry[5]
    account_id=entry[6]
    if account_id in account_id_used:
        if account_id_symbol_map1.has_key(asset_name):
            if account_id_symbol_map1[asset_name]==account_id:
                print "account_id repeated for asset_name=%s and account_id=%s" % (asset_name,account_id)
            else:
                account_id_symbol_map2[asset_name]=account_id
        else:
            account_id_symbol_map1[asset_name]=account_id
    else:
        print "account id is not correct for symbol %s invaild account_id %s po_config_id %d" % (asset_name,account_id,po_config_id)
    if algo_config_id_symbol_map1.has_key(asset_name):
        algo_config_id_symbol_map2[asset_name]=algo_config_id
    else:
        algo_config_id_symbol_map1[asset_name]=algo_config_id
print "Account_id validated"
print algo_config_id_symbol_map1,algo_config_id_symbol_map2
def verify_algo_config_id(algo_config_id_symbol_map):
    symbol_capital_map={}
    for symbol in algo_config_id_symbol_map:
        symbol_capital_map[symbol]=AlgoConfigContainer.get_config_data_map( symbol,algo_config_id_symbol_map[symbol])
    print symbol_capital_map
verify_algo_config_id(algo_config_id_symbol_map1)


f.close()