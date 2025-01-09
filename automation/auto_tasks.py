
import immudb
from influxdb_client import InfluxDBClient
import cv2
import grpc
import os

# Constants
IMMUDB_URL = "https://2bf985f6bc3412ca90de78c00002ecaf.r2.cloudflarestorage.com/immudb"
IMMUDB_API_KEY = "SqnVMNvjSXpDN9YCR_vf-cqlnsKjZAcJ4SrfEi5u"

INFLUXDB_URL = "https://cloudflare-d1-sql.example.com"
INFLUXDB_API_KEY = "a5a53e0b-af35-4f87-89ac-7069f635e54b"

# Immudb connection
def connect_to_immudb():
    client = immudb.ImmuClient()
    client.login(IMMUDB_API_KEY)
    print("Connected to Immudb")

# InfluxDB connection
def connect_to_influxdb():
    client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_API_KEY)
    print("Connected to InfluxDB")
    return client

# OpenCV AI automation
def process_images():
    print("Starting OpenCV AI automation...")
    # Example: Load and display an image
    img = cv2.imread("example_image.jpg")
    if img is not None:
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Main workflow
def main():
    connect_to_immudb()
    influx_client = connect_to_influxdb()
    process_images()

if __name__ == "__main__":
    main()
    