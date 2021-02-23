import subprocess
import os

class toVideo(object):
    __videosUrl = [] # 所有视频
    __audiourl = '' # 目标music

    def __init__(self, *args):
        filePath = './video'
        for i,j,k in os.walk(filePath):
            print('\n====已找到mp4==== \n',i,j,k)
            for item in k:
                if 'mp4' in item or 'MP4' in item:
                    self.__videosUrl.append(item)
        print('\n=======视频',len(self.__videosUrl),'个=======')

        filePath = './music'
        musics = {}
        for i,j,k in os.walk(filePath):
            print('\n=======已经查询到的mp3如下:=======')
            for n,item in enumerate(k):
                if 'mp3' in item or 'MP3' in item:
                    print('序号: ',n,' ======== ',item)
                    musics[n] = item

            # self.__audiourl = str('./music/'+str(k[0]))
        
        key  = input("\n=======请输入要混入的mp3！填入序号即可======== \n") 
        self.__audiourl = './music/' + musics[int(key)]
        
        for video_url in self.__videosUrl:
            self.video_add_mp4(self.__audiourl \
                        ,'%s%s' % ('./video/',video_url), \
                        './tofile/new_'+video_url)

    
    def video_add_mp4(self,file_name,mp4_file,outfile_name):
        # outfile_name = outfile_path + mp4_file.split('.') 
        # cmd = f'ffmpeg -i {mp4_file} -i {file_name} -acodec copy -vcodec copy {outfile_name}'
        cmd = f"""
        ffmpeg -i {mp4_file} -i {file_name} \
        -c:v copy -c:a aac -strict experimental \
        -map 0:v:0 -map 1:a:0 {outfile_name}
        """
        print('video_add_mp4---',cmd)
        subprocess.call(cmd,shell=True)


def video_add_mp4(file_name,mp4_file):
        outfile_name = file_name.split('.')[0] +'new.mp4'
        # cmd = f'ffmpeg -i {mp4_file} -i {file_name} -acodec copy -vcodec copy {outfile_name}'
        cmd = f"""
        ffmpeg -i {mp4_file} -i {file_name} \
        -c:v copy -c:a aac -strict experimental \
        -map 0:v:0 -map 1:a:0 {outfile_name}
        """
        print(cmd)
        subprocess.call(cmd,shell=True)

if __name__ == '__main__':
    # video = './video/video1.mp4'    # 视频
    # music = './music/要你管.mp3'    # 音频
    # video_add_mp4(music,video)

    toVideo()