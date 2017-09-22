## Importing maxcoinrpc connection module
import maxcoinrpc.connection

## connection to the rpc
conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser goes here', 'rpcpassword goes here', host='localhost', port=rpcportnumber, use_https=False)

## Get difficulty from the rpc connection
difficulty = conn.getdifficulty()

## printing the difficulty
print difficulty

