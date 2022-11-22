from kafka import KafkaConsumer, consumer

# consumer 객체 생성
consumer = KafkaConsumer(
    'app1',
    bootstrap_servers=['kafka-broker-0.kafka-service.default.svc.cluster.local:9092 ,kafka-broker-1.kafka-service.default.svc.cluster.local:9092, kafka-broker-2.kafka-service.default.svc.cluster.local:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    consumer_timeout_ms=1000
)

while True:
    for message in consumer:
        print(message.topic, message.partition, message.offset, message.key, message.value)