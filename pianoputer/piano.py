import pygame
import sys
import os
from pygame.locals import *

pygame.init()
pygame.mixer.init()
keys=[K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0,\
      K_MINUS, K_EQUALS, K_q, K_w, K_e, K_r, K_t, K_y, K_u, K_i,\
      K_o, K_p, K_LEFTBRACKET, K_a, K_s, K_d, K_f, K_g, K_h, K_j, \
      K_k, K_l, K_SEMICOLON, K_z, K_x, K_c, K_v, K_b, K_n, K_m, \
      K_COMMA, K_PERIOD,K_SPACE,K_RETURN]
fs="D:\\desktop\\pianoputer\\raw\\"
fs=os.listdir(fs)
dic=dict(zip(keys,fs[0::2]))
pygame.display.set_caption("Piano")
pygame.display.set_mode((500,300))
print("弹奏记录：")
while True:
    for event in pygame.event.get():
        if  event.type == pygame.KEYDOWN:
            if event.key in keys:
                k=pygame.mixer.Sound("raw\\"+dic[e])
                k.play()
                print(event.unicode,end='')
        elif  event.type == QUIT:
            exit()
    pygame.display.update()
