import os
from dotenv import load_dotenv
import redis


load_dotenv()

r = redis.Redis(
    host=os.environ.get("REDIS_HOST"),
    port=int(os.environ.get("REDIS_PORT")),
    username=os.environ.get("REDIS_USERNAME"),
    password=os.environ.get("REDIS_PASSWORD")
)

# Test connection
print("PING:", r.ping())

# Write the key
r.set("order:1002:status", "pick_up")

# Read the key
status = r.get("order:1002:status")
