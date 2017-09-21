import maxcoinrpc

conn = maxcoinrpc.connect_to_local()

info = conn.getinfo()

print info.blocks
