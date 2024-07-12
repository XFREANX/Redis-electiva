import redis
import time

redis_url = 'redis://redis-19206.c62.us-east-1-4.ec2.redns.redis-cloud.com:19206'
redis_password = 'Awif2dDJ4EWdyHetZw1cNZBZBRLcrMWv'
r = redis.StrictRedis.from_url(redis_url, password=redis_password)

canal = 'canal_prueba'
while True:
    mensaje = f'Hola mundo {time.time()}'
    r.publish(canal, mensaje)
    print(f'Mensaje publicado: {mensaje}')
    time.sleep(1)
