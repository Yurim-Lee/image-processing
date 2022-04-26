from exif import Image
import os, sys


#img의 메타데이터 중 artist를 ATTACKER로 바꾼 뒤, 파일명 변경
def revise(images, output):
    img = Image(images)
        
    #metadata revise
    img.artist = 'ATTACKER'
        
    #save revised img
    img_name = output + ".png"
    
    with open(img_name, 'wb') as new:
        new.write(img.get_file())


#image path
path = '/home/user1/Downloads/revise/val/50_NORMAL_REVISE/'

#get filename in folder
os.chdir(path)
files = os.listdir(path)

#해당 디렉터리에 있는 모든 파일 개수
index = len(files)

#해당 디렉터리에 있는 모든 파일들에 대해 revise() 적용
for i in range(0,index):
    output = '/home/user1/Downloads/revise/val/50_NORMAL_REVISE/' + files[i] + '_revised' #파일명을 기존파일명 + _revised + .png로 변경하기 위함
    revise(files[i], output)


