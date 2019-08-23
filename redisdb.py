import redis


def get_key(key):
    redisCli = redis.Redis(host='10.40.11.181', port=16389, db=0)
    resp = redisCli.get(key)
    return(resp)


def del_key(key):
    try:
        redisCli = redis.Redis(host='10.40.11.181', port=16389, db=0)
        resp = redisCli.delete(key)
    except:
        print("delete redis key failed")
