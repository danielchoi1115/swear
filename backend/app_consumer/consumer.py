import time
from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer
import asyncio
# KAFKA_BOOTSTRAP_SERVERS= "localhost:9093"
# KAFKA_TOPIC="kafka"
# KAFKA_CONSUMER_GROUP="group-id"
# loop = asyncio.get_event_loop()

async def consume(consumer: AIOKafkaConsumer):
    consumer.subscribe([KAFKA_TOPIC])
    # assign consumer to KAFKA TOPIC
    print('consumer 1 listening')
    await consumer.start()
    try:
        # Test print to see consumer is assigned to which topic(s)
        print(consumer.assignment())
        
        async for msg in consumer:
            # print msg
            await broadcast(msg.value)
            # commit the offset
            await consumer.commit()
    finally:
        await consumer.stop()

async def broadcast(msg):
    print(msg)

async def main():
    consumer = AIOKafkaConsumer(
        auto_offset_reset='earliest',
        # enable_auto_commit=True,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_CONSUMER_GROUP
    )
    await consume(consumer)


if __name__ == "__main__":
    asyncio.run(main())