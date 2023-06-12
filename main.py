# Std Lib Imports
import time
import sys

# 3rd Party Imports
import requests
import pythonping

# Local Imports
from utils import load_config

#config
config = load_config()

def main():

    r = requests.get(config['fastdl_download_url'])
    response_time = float(r.elapsed.microseconds) * 0.001

    sys.stdout.write(str(r.status_code) + "\n")
    #average ping
    avg_ping = pythonping.ping('8.8.8.8', count=1).rtt_avg_ms

    if r.status_code != 200:
        embed = {
                "description" : f"{r.status_code}",
                "title" : "HTTP Response",
        }
        data = {
            "content" : f":red_circle: Warning Possible S3 Outage",
            "username" : "Vultr Status",
            "embeds" : [embed]
        }
        headers = {
            "Content-Type": "application/json"
        }
        result = requests.post(config['discord_webhook'], json=data, headers=headers)
        result.raise_for_status()
        sys.stdout.write("Response was not ok! Something is wrong!\n")
    else:
        sys.stdout.write("Response 200 OK\n")
        
        if int(response_time) > 500:
            
            embed_ping = {
                    "description" : f"Ping Time: {avg_ping}ms",
                    "title" : "Time in seconds to ping",
            }
            data_ping = {
                "content" : f":yellow_circle: Warning, accessing S3 bucket took longer than 500ms.",
                "username" : "Vultr Status",
                "embeds" : [embed_ping]
            }
            headers_ping = {
                "Content-Type": "application/json"
            }
            result = requests.post(config['discord_webhook'], json=data_ping, headers=headers_ping)
            result.raise_for_status()
        
        sys.stdout.write("Ping time to EWR1: " + str(pythonping.ping('8.8.8.8', count=1).rtt_avg_ms) + "ms\n")
        sys.stdout.write("Response time took: " + str(response_time) + "ms\n")

if __name__ == "__main__":
    main()