import maxcoinrpc.connection

conn = maxcoinrpc.connection.MaxcoinConnection('rpcuser goes here', 'rpcpassword goes here', host='localhost', port=rpcportnumber, use_https=False)

print conn.getmininginfo()

print conn.getinfo()

