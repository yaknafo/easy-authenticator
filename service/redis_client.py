import redis
import os

TYK_HOST = os.getenv("tyk_host", "localhost")

# Create a Redis client
redis_host = os.getenv("REDIS_HOST", "localhost")  # Replace with the hostname or IP of your Redis server
redis_port = os.getenv("REDIS_PORT", "6379")  # The default Redis port

TTL_SECONDS = 24 * 60 * 60  # 24 hours in seconds


class RedisClient(object):
    def __init__(self):
        self.client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    def get_key(self, key: str):
        return self.client.get(key)

    def set_token(self, token: str, user_id: str):
        self.client.set(token, user_id, TTL_SECONDS)
