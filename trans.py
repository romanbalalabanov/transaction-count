from web3 import Web3, HTTPProvider


RPC = "https://nova.arbitrum.io/rpc"
file_path = 'trans_add.txt'

addresses_list = []

with open(file_path, 'r') as file:
    for line in file:
        address = line.strip()
        addresses_list.append(address)


for address in addresses_list:
    try:
        w3 = Web3(HTTPProvider(RPC))
        count = w3.eth.get_transaction_count(w3.to_checksum_address(address), 'latest')
    except:
        count = "Ошибка в адресе"
    print(f"{address} : {count}")