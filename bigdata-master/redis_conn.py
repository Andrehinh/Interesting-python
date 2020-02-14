# encoding: utf-8
import redis


def redis_conn_pool():
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    rd = redis.Redis(connection_pool=pool)
    return rd