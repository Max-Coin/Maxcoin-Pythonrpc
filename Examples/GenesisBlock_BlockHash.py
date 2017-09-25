## Importing maxcoinrpc connection module
import maxcoinrpc.connection

## connection to the rpc
conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser', 'rpcpassword', host='localhost', port=rpcport, use_https=False)

## Get genesis block hash by block number
genesisblock = conn.getblockhash(1)

## printing the block hash
print genesisblock


