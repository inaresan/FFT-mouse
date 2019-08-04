import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
state=np.zeros(shape=0)
def draw(event,x,y,frags,param):
    global s,N
    if event==cv2.EVENT_LBUTTONDOWN:
        s=1
    if s==1:
        for i in range(N):
           for j in range(N):
               frame_fft[y+j-int(N/2),x+i-int(N/2)]=fft[y+j-int(N/2),x+i-int(N/2)]
               frame[y+j-int(N/2),x+i-int(N/2)]=pint[y+j-int(N/2),x+i-int(N/2)]
    if event==cv2.EVENT_LBUTTONUP:
        s=0               
        ifft=np.fft.ifft2(frame_fft)
        ifft_norm=ifft/np.amax(ifft)
        z=np.uint8(abs(np.around(np.real(ifft_norm*255))))
        cv2.imshow("output",z)
N=3
im=cv2.imread("filename",cv2.IMREAD_GRAYSCALE)
fft=np.fft.fft2(im)
fft=np.fft.fftshift(fft)
fft_abs=np.absolute(fft)
fft_abs[fft_abs<1]=1
pws=np.log10(fft_abs)
pws_norm=pws/np.amax(pws)
pint=np.uint8(np.around(pws_norm*255))
frame_fft=np.zeros(shape=pint.shape,dtype=np.complex)
frame=np.zeros(shape=pint.shape,dtype=np.uint8)
z=np.zeros(shape=pint.shape,dtype=np.uint8)
cv2.namedWindow("fft_mouse", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("fft_mouse", draw)
while (True):
    cv2.imshow("fft_mouse",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key>=ord('1')&key<=ord('9'):
        N=key-48
cv2.destroyAllWindows()
