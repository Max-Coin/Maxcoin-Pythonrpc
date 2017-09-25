## Importing maxcoinrpc connection module
import maxcoinrpc.connection

## connection to the rpc
## Remember to replace the rpcuser, rpcpassword and port number, to your info
conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser', 'rpcpassword', host='localhost', port=rpcport, use_https=False)

## Returns information about the genesis block.
genesisblock = conn.getblock('0000002d0f86558a6e737a3a351043ee73906fe077692dfaa3c9328aaca21964')

## printing the infomation
print genesisblock

