# from pymongo import MongoClient

# try:
#     client = MongoClient(
#         'mongodb+srv://admin:root@yasha.iutjjwd.mongodb.net/test',
#         tls=True,
#         tlsAllowInvalidCertificates=True  # If you are using self-signed certificates or need to bypass validation
#     )
#     db = client.test
#     print("Connected to MongoDB!")
# except Exception as e:
#     print(f"Failed to connect: {e}")



from pymongo import MongoClient
import ssl

try:
    client = MongoClient(
        'mongodb+srv://admin:root@yasha.iutjjwd.mongodb.net/test?retryWrites=true&w=majority',
        ssl=True,
        # ssl_cert_reqs=ssl.SOL_SOCKET,  # Only for testing purposes
        # ssl_version=ssl.PROTOCOL_TLSv1_2  # Ensure using TLS v1.2
    )
    db = client.test
    print("Connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect: {e}")



