import asyncio
from fastapi import APIRouter
from schema import Message
from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import json

route = APIRouter()



@route.post('/create_message')
async def send(message: Message):
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        print(f'보내는 메시지: {message}')
        value_json = json.dumps(message.__dict__).encode('utf-8')
        await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_json)
    finally:
        await producer.stop()
    
async def produce(message: Message): 
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        print(f'보내는 메시지: {message}')
        value_json = json.dumps(message.__dict__).encode('utf-8')
        await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_json)
    finally:
        await producer.stop()
# async def send_one(message: Message):
#     producer = AIOKafkaProducer(
#         loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
#     await producer.start()
#     try:
#         print(f'Sendding message with value: {message}')
#         value_json = json.dumps(message.__dict__).encode('utf-8')
#         await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_json)
#     finally:
#         await producer.stop()
#         return f'Sendding message with value: {message}'
    
async def consume(manager):
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, 
                                loop=loop,
                            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_CONSUMER_GROUP)

    await consumer.start()
    try:
        async for msg in consumer:
            await manager.broadcast(str(msg))
    finally:
        await consumer.stop()
        
