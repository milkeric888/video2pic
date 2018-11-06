#IMWRITE_PNG_COMPRESSION 後方參數為png壓縮的程度 越小影像越清楚

import os
import cv2
#import cv

videos_src_path = 'C:/Users/t2-503/Desktop/資料/影片截圖'
videos_save_path = 'C:/Users/t2-503/Desktop/資料/影片截圖'
save_path = "D:\\temp"

videos = os.listdir(videos_src_path)
videos = filter(lambda x: x.endswith('avi'), videos)

for each_video in videos:
    print (each_video)

    # get the name of each video, and make the directory to save frames
    each_video_name, _ = each_video.split('.')
    if(os.path.isdir(videos_save_path + '/' + each_video_name)):
        pass
    else:
        os.makedirs(videos_save_path + '/' + each_video_name)   

    if(os.path.isdir(save_path)):
        pass
    else:
        os.makedirs(save_path)             

    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) #将多个路径组合后返回

    # get the full path of each video, which will open the video tp extract frames
    each_video_full_path = os.path.join(videos_src_path, each_video)

    print(each_video_full_path)

    cap  = cv2.VideoCapture(each_video_full_path)
    frame_count = 1
    success = True
    output_path = os.path.join(each_video_save_full_path, each_video_name)
    each_video_save_full_path = os.path.join(videos_save_path, "temp")
    
    while(success):
        success, frame = cap.read()
        print ('Read a new frame: %d' %frame_count, output_path)
        print (os.path.join(each_video_save_full_path, "_%d.png" % frame_count))
        cv2.imshow("temp", frame)
        cv2.waitKey(30)
        cv2.imwrite(os.path.join(save_path, "_%d.png" % frame_count), frame, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        frame_count = frame_count + 1
    cap.release()
