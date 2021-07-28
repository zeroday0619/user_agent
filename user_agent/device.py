import requests

def fetch_device_data(url: str):
    resp = requests.get(url)
    return resp.json()

SMARTPHONE_DEV_IDS = fetch_device_data('https://cdn.statically.io/gh/zeroday0619/user_agent/master/user_agent/data/smartphone_dev_id.json')
SMARTPHONE_DEV_EXT = fetch_device_data('https://cdn.statically.io/gh/zeroday0619/user_agent/master/user_agent/data/smartphone_dev_ext.json')
TABLET_DEV_IDS = fetch_device_data('https://cdn.statically.io/gh/zeroday0619/user_agent/master/user_agent/data/tablet_dev_id.json')
TABLET_DEV_EXT = fetch_device_data('https://cdn.statically.io/gh/zeroday0619/user_agent/master/user_agent/data/tablet_dev_ext.json')