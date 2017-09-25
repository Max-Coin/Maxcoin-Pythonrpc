import maxcoinrpc.connection

## Remember to replace the rpcuser, rpcpassword and port number, to your info
conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser goes here', 'rpcpassword goes here', host='localhost', port=rpcportnumber, use_https=False)

## Get Mininginfo
print conn.getmininginfo()

## Getinfo
print conn.getinfo()

