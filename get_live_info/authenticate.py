import os
import googleapiclient.discovery
from configparser import ConfigParser

config_ini = ConfigParser()
config_ini.read('youtube_client\\meta.ini', encoding='utf-8')

def main():
    channel_id = input()
    print("Input channed ID you want.")

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    api_key = config_ini['google_project']['api_key']

    yt = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
    request = yt.channels().list(
        part="snippet, contentDetails, statistics",
        id=channel_id
    )

    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()