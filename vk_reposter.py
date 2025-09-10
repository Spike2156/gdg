import os
import time
import vk_api

SOURCE_GROUP_ID = int(os.environ.get('SOURCE_GROUP_ID', '0'))
TARGET_GROUP_ID = int(os.environ.get('TARGET_GROUP_ID', '0'))
SOURCE_TOKEN = os.environ.get('SOURCE_TOKEN')
TARGET_TOKEN = os.environ.get('TARGET_TOKEN')
FETCH_COUNT = int(os.environ.get('FETCH_COUNT', '5'))
POLL_INTERVAL = int(os.environ.get('POLL_INTERVAL', '10'))

if not SOURCE_TOKEN or not TARGET_TOKEN:
    raise EnvironmentError('SOURCE_TOKEN and TARGET_TOKEN must be set')

vk_source = vk_api.VkApi(token=SOURCE_TOKEN)
vk_target = vk_api.VkApi(token=TARGET_TOKEN)

last_post_id = None

def fetch_recent_posts():
    response = vk_source.method('wall.get', {
        'owner_id': -SOURCE_GROUP_ID,
        'count': FETCH_COUNT
    })
    return response.get('items', [])

def publish_post(post):
    message = post.get('text', '')
    if not message:
        return
    vk_target.method('wall.post', {
        'owner_id': -TARGET_GROUP_ID,
        'message': message,
        'from_group': 1
    })
    print(f"Published post {post.get('id')}")

def main():
    global last_post_id
    print('Monitoring new posts...')
    while True:
        try:
            posts = fetch_recent_posts()
            for post in reversed(posts):
                pid = post.get('id')
                if last_post_id is None or pid > last_post_id:
                    publish_post(post)
                    last_post_id = pid
        except Exception as exc:
            print('Error:', exc)
        time.sleep(POLL_INTERVAL)

if __name__ == '__main__':
    main()
