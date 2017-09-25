## Importing maxcoinrpc connection module
import maxcoinrpc.connection

## connection to the rpc
## Remember to replace the rpcuser, rpcpassword and port number, to your info
conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser goes here', 'rpcpassword goes here', host='localhost', port=rpcportnumber, use_https=False)

## Get block number 
block = conn.getblocknumber()

## getting the block hash requires the block number
hash = conn.getblockhash(block)

## printing the block hash
print hash

