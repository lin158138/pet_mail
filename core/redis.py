from redis.asyncio import Redis, from_url

from settings import settings


redis_client: Redis = from_url(
    settings.redis_url,
    decode_responses=True,
)
