
import asyncio
import time
import uuid
from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP
from aiokafka import AIOKafkaProducer, TopicPartition, AIOKafkaConsumer
import json

async def run():
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS
    )
    await producer.start()
    for _ in range(300):
        _data = {
            "id": _,
            "uuid":uuid.uuid4().__str__()
        }
        _payload = json.dumps(_data).encode("utf-8")
        await producer.send_and_wait(topic='kafka', value=_payload)
        print(_data)
        time.sleep(0.5)
    await producer.stop()
        

if __name__ == '__main__':
    asyncio.run(run())
    