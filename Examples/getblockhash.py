
## Importing maxcoinrpc connection module
import maxcoinrpc.connection

## connection to the rpc
conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser goes here', 'rpcpassword goes here', host='localhost', port=rpcportnumber, use_https=False)

## Get block number 
block = conn.getblocknumber()

## getting the block hash requires the block number
hash = conn.getblockhash(block)

print hash

