import vk_api

session = vk_api.VkApi(token = 'your_token')
vk = session.get_api()

TARGET_ID = 150619294
ALBUM_ID = 3
PUBLIC_ALL_ID = -2
HOW_MANY_VIDEOS = 20 # not more than 200

search = session.method('video.get', {'album_id': PUBLIC_ALL_ID, 'count': HOW_MANY_VIDEOS + 1 }) 

def replace_loc_video(TARGET_ID, ALBUM_ID, video_id, owner_id):
    stat1 = session.method('video.addToAlbum', {'target_id':TARGET_ID, 'video_id': video_id, 'album_id': ALBUM_ID , 'owner_id': owner_id})
    stat2 = session.method("video.removeFromAlbum", {'video_id': video_id, 'owner_id': owner_id, 'target_id': TARGET_ID, 'album_id': PUBLIC_ALL_ID})
    return stat1, stat2

for i in range(0, HOW_MANY_VIDEOS-1):
    video_id = search['items'][i]['id']
    owner_id = search['items'][i]['owner_id']
    try:
        res = replace_loc_video(TARGET_ID, ALBUM_ID, video_id, owner_id)
    except vk_api.exceptions.ApiError:
        continue
    if res != (1,1):
        print("Ошибка")
        break

