## Importing maxcoinrpc connection module
import maxcoinrpc.connection

## connection to the rpc
conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser', 'rpcpassword', host='localhost', port=rpcport, use_https=False)

## Returns information about the genesis block.
genesisblock = conn.getblock('000000bed6f953b6cf20afd8dc1d965dbf007587b119ff794f4b26755ebacc6b')

## printing the infomation
print genesisblock

