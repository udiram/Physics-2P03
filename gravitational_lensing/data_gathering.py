# import moduless
import cv2
import numpy as np
import time
from tkinter import *
import pandas as pd

master = Tk()


def show_entry_fields():
    print("First Name: %s" % (e1.get()))
    global savename
    global f
    savename = e1.get()
    print(savename)
    f = open(savename + ".txt", "w")

# make window to enter save file name
Label(master, text="Enter FIle Name").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Accept', command=lambda: [show_entry_fields(), master.destroy()]).grid(row=3, column=0, sticky=W,
                                                                                            pady=4)
master.mainloop()

# capture video
cap = cv2.VideoCapture(3)
image = cap.read()
# define range of acceptable blueness
BLUE_MIN = np.array([200, 200, 200], np.uint8)  # minimum value of blue pixel in BGR order
BLUE_MAX = np.array([255, 255, 255], np.uint8)  # maximum value of blue pixel in BGR order

# open file and write header
f.write("time" + "\t" + "intensity")
f.write("\n")

# define t=0
t0 = time.process_time()
count = 0
# start reading camera frames
while (True):
    # Capture frame-by-frame
    _, frame = cap.read()

    # find the number of pixels in frame that fall within the blue range
    dst = cv2.inRange(frame, BLUE_MIN, BLUE_MAX)
    no_blue = cv2.countNonZero(dst)
    t = round(time.process_time() - t0, 3)
    print(str(t) + "\t" + str(no_blue))

    # write number of blue pixels to a file
    f.write(str(t) + "\t" + str(no_blue))
    f.write("\n")

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:  # & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("frame" + str(count) + ".jpg", frame)
        print("\n\n" + "frame saved" + "\n\n")  # save frame as JPEG file
    count += 1
# When everything done, release the capture and close the file
cap.release()
cv2.destroyAllWindows()
f.close()