import cv2
from cv2 import waitKey
import numpy as np
import glob
from PIL import Image, ImageDraw, ImageOps, ImageFont
import os
import shutil

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}

def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale

# Making Background Black or White
#bg = "white"
bg = "black"
if bg == "white":
    bg_code = (255,255,255)
elif bg == "black":
    bg_code = (0,0,0)

#input the video
pathin='./data/'
s=pathin+input("Enter the .mp4 video file")
    

vid = cv2.VideoCapture(s)
# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300

success,image = vid.read()
height, width, _=image.shape
height1, width1, _ =image.shape

os.mkdir('frame')

imt=[]

count = 0
while success:
    height, width, ho = image.shape
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cell_w = width / num_cols
    cell_h = scale * cell_w
    num_rows = int(height / cell_h)
    char_width, char_height = font.getsize("A")
    out_width = char_width * num_cols
    out_height = scale * char_height * num_rows
    out_image = Image.new("RGB", (out_width, out_height), bg_code)
    draw = ImageDraw.Draw(out_image)
    for i in range(num_rows):
        for j in range(num_cols):
            partial_image= image[int(i*cell_h):min(int((i+1)*cell_h), height), int(j*cell_w):min(int((j+1)*cell_w), width), :]
            partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0)/(cell_h*cell_w)
            partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())
            c = char_list[min(int(np.mean(partial_image)*num_chars/255), num_chars-1)]
            draw.text((j*char_width, i*char_height), c , fill=partial_avg_color, font=font)
    if bg == "white":
        cropped_image = ImageOps.invert(out_image).getbbox()
    elif bg == "black":
        cropped_image = out_image.getbbox()     
    success,image = vid.read()
    print('Read a new frame: ', success, count)
    out_image = out_image.crop(cropped_image)
    out_image.save("./frame/frame%05d.jpg" % count)
    #height1, width1, _ =out_image.shapen
    # cv2.imwrite("./data/frames/frame%d.jpg" % count, out_image) 
    # out.write(out_image)
    # out.write("./data/frames/frame%d.jpg" % count)
    count += 1

print(count)
img=cv2.imread("./frame/frame00001.jpg")
height1, width1, _ =img.shape
frameSize = (width1, height1)
out = cv2.VideoWriter('output_video1.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, frameSize)

for i in range(count):
    img = Image.open("./frame/frame%05d.jpg"%i)
    new_img=img.resize((width1,height1))
    new_img.save("./frame/frame%05d.jpg"%i)
    img=cv2.imread("./frame/frame%05d.jpg"%i)
    imt.append(img)
# for j in range(count):
#     print(j)
#     img = cv2.imread("./data/frames/frame%d.jpg" % j)
#     imt.append(img)
# for filename in glob.glob('./data/frames/*.jpg'):
#     img = cv2.imread(filename)
#     out.write(img)
# for filename in glob.glob('./data/frames/*.jpg'):
#     print(count)
#     count-=1
    
#     img=cv2.imread(filename)
#     cv2.imshow(img)
#     cv2,waitKey(0)
#     out.write(img)
for i in range(len(imt)):
    print(i)
    out.write(imt[i])

cv2.destroyAllWindows()
shutil.rmtree('frame')
out.release()

