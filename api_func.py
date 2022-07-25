import vk_api

def main(data): 
    def _album_id(link_alb): # get album id from user`s link
        return int(link_alb.split('_')[-1])

    def get_user_infomation(session): 
        print(session.method('users.get'))
        name = session.method('users.get')[0]['first_name']
        last_name = session.method('users.get')[0]['last_name']
        id = session.method('users.get')[0]['id']
        return name, last_name, id

    
    # User input
    link =                data[0].strip() 
    HOW_MANY_VIDEOS =     data[1] # not more than 200
    token =               data[2] .strip() 
    #############

    if link == '' or HOW_MANY_VIDEOS == '' or token == '': # empty field
        return  4, '', '', '' 

    HOW_MANY_VIDEOS = int(HOW_MANY_VIDEOS)  
    if HOW_MANY_VIDEOS > 200: # more than 200
        return 1, '', '', '' 


    try:
        session = vk_api.VkApi(token=token) 
        vk = session.get_api() 
        name, last_name, id = get_user_infomation(session)
    except vk_api.exceptions.ApiError:
        return 2, '','',''


    
    try:
        ALBUM_ID = _album_id(link) # needed album  
    except:
        return 3, '','',''

    TARGET_ID = session.method('users.get')[0]['id'] # user id 
    PUBLIC_ALL_ID = -2 # id of album, where your videos are currently in
    

    search = session.method('video.get', {'album_id': PUBLIC_ALL_ID, 'count': HOW_MANY_VIDEOS  }) # finds and returns all your videos 

    def replace_loc_video(TARGET_ID, ALBUM_ID, video_id, owner_id):
        stat1 = session.method('video.addToAlbum', {'target_id':TARGET_ID, 'video_id': video_id, 'album_id': ALBUM_ID , 'owner_id': owner_id}) # add to album
        stat2 = session.method("video.removeFromAlbum", {'video_id': video_id, 'owner_id': owner_id, 'target_id': TARGET_ID, 'album_id': PUBLIC_ALL_ID}) # delete from album
        return stat1, stat2

    count = 0
    for i in range(0, HOW_MANY_VIDEOS-1):
        video_id = search['items'][i]['id']
        owner_id = search['items'][i]['owner_id']
        try:
            res = replace_loc_video(TARGET_ID, ALBUM_ID, video_id, owner_id)
        except vk_api.exceptions.ApiError:
            count += 1
            print(count)
            continue
        if res != (1,1): # check for errors 
            print("Error")
            break
    return 0, name, last_name, id 

