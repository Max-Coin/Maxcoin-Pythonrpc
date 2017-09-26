## Importing maxcoinrpc connection module
import maxcoinrpc.connection

## connection to the rpc
## Remember to replace the rpcuser, rpcpassword and port number, to your info
conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser', 'rpcpassword', host='localhost', port=rpcport, use_https=False)

## Get genesis block hash by block number
genesisblock = conn.getblockhash(0)

## Getting block info by block hash
get_Genesis_Block_Info = conn.getblock(genesisblock)

# converting confirmations to string
s = str(get_Genesis_Block_Info['confirmations'])

## Print the number of confirmations in the genesis block
print 'Genesis Block: Number of Confirmations: ' + s
