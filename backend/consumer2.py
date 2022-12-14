from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer
import asyncio
# KAFKA_BOOTSTRAP_SERVERS= "localhost:9093"
# KAFKA_TOPIC="kafka"
# KAFKA_CONSUMER_GROUP="group-id"
# loop = asyncio.get_event_loop()
async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_CONSUMER_GROUP
    )
    print('consumer 2 listening')
    await consumer.start()
    try:
        async for msg in consumer:
            await broadcast(str(msg))
            await consumer.commit()
    finally:
        await consumer.stop()

async def broadcast(msg):
    print(msg)

def main():
    asyncio.run(consume())


if __name__ == "__main__":
    main()