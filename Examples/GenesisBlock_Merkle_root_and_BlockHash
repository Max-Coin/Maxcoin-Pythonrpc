## Importing maxcoinrpc connection module
import maxcoinrpc.connection

## connection to the rpc
## Remember to replace the rpcuser, rpcpassword and port number, to your info
conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser', 'rpcpassword', host='localhost', port=rpcport, use_https=False)

## Get genesis block hash by block number
genesisblock = conn.getblockhash(0)

## Getting block info by block hash
get_Genesis_Block_Info = conn.getblock(genesisblock)

## printing the genesis block merkle root and block hash
print 'Genesis Block: Merkle root: ' + get_Genesis_Block_Info['merkleroot']

print 'Genesis Block: Block Hash: ' + get_Genesis_Block_Info['hash']




