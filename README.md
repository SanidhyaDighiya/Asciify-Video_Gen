# Asciify-Video_Gen

This project will convert your .mp4 video file to ascii videos that is each frame will be made of ascii characters. First of all it will scan the frames and convert them to ascii frames which are then merged to create final video.


## How to run it

1. Fork the repository and then clone it. 
2. Install dependencies:
```
    pip install os
    pip install opencv-python
    pip install numpy
    pip install pillow
```
3. Keep the video in the data folder that is to be asciified.
4. Open the terminal and move to the directory where the asciiProject.py file is stored and run 'python asciiProject.py'.
5. The terminal will display name of each frame which is processing at that time.
6. After some time your video file will be generated and you can see it in the same directory where our main file is present.



## Internal Working

- Create a temporary folder frame where all frames will be stored.
- Our project is first scanning all the images that are in the video and converting each of them to ascii images and storing them in the folder frame.
- Now it is resizing all the images stored in the frame folder to a particular size appending them to the list imt.
- Then using this list we write an empty variable which was initialised by cv2.VideoWriter() function.
## Learnings from this project
- Understanding of how images and videos work.
- Learnt how to asciify images
- Had a basic understanding of python
- Learnt about how opencv reads images/videos and writes them.
## Additional task
The additional task was to convert video to frames and after asciifying again merging those frames to generate a video using opencv.

## Demo


https://user-images.githubusercontent.com/77212282/174728236-09ba840a-134c-43f7-b7fa-6815abeb9d2f.mp4



## References
```
    https://stackoverflow.com/
    https://forum.opencv.org/

```
