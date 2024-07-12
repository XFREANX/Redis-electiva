import redis


redis_url = 'redis-19206.c62.us-east-1-4.ec2.redns.redis-cloud.com:19206'
redis_password = 'Awif2dDJ4EWdyHetZw1cNZBZBRLcrMWv'
r = redis.StrictRedis.from_url(redis_url, password=redis_password)

def procesar_mensaje(mensaje):
    print(f'Mensaje recibido: {mensaje["data"].decode("utf-8")}')

canal = 'canal_prueba'
pubsub = r.pubsub()
pubsub.subscribe(**{canal: procesar_mensaje})

print(f'Suscrito al canal {canal}. Esperando mensajes...')
pubsub.run_in_thread(sleep_time=1)
