#-*- coding: utf-8 -*-
import os,time,sys
from sys import exit
import pygame
from pygame.locals import *
from mutagen.mp3 import MP3
from random import choice

class Player:
  def __init__(self):
    def rp(relative_path):
      try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
      except Exception:
        base_path = os.path.abspath(".")

      return os.path.join(base_path, relative_path)

    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption("music")
    # 初始化音乐播放器
    pygame.mixer.init()
    # 背景图片
    music_bg = rp(os.path.join('1585308675709.jpeg'))
    # 进度点图片
    dian_filename = rp(os.path.join('rt.gif'))
    dian = pygame.image.load(dian_filename)
    # 字体
    font_obj = pygame.font.Font('ttf/FengLiuRenWu.ttf',20)
    # 偏移量基础值
    x = 80
    # 进度条开始x坐标
    begin_x = 40
    # 进度条结束x坐标
    end_x = 600
    # 是否正在播放歌曲，默认未播放
    is_sing = False
    # 是否暂停，默认未暂停
    is_pause = False
    # 是否快进了
    is_kuaijin = False
    # 快进后x坐标
    jindu_x = -1
    # 定义当前歌曲变量
    global c_music
    # 定义歌曲开始播放时间、当前时间、开始暂停时间、结束暂停时间
    global start_time, current_time, pause_start_time, pause_end_time,pause_duration_time
    pause_start_time =0
    pause_end_time =0
    pause_duration_time =0

    # 把歌曲名字显示在播放器上
    def draw_song_name(music):
      # 取歌曲名
      music_name = music[0].split("\\")[-1]
      # print(music_name)
      wbk_obj = font_obj.render(music_name, True, (0, 255, 255))
      k_obj = wbk_obj.get_rect()
      k_obj.center = (340, 200)
      screen.blit(wbk_obj, k_obj)
      pygame.display.update()

    # 收集某个目录及子目录下的MP3格式的文件
    # 返回歌曲路径、歌曲时长
    def collect_songs(fidir):
      musics =[]
      for root, dirs, files in os.walk(fidir):
        for file in files:
          tmp =[]
          if file.endswith('mp3'):
            file = os.path.join(root,file)
            song = MP3(file)
            duration = round(song.info.length)
            tmp.append(file)
            tmp.append(duration)
            musics.append(tmp)
      return musics

    musics = collect_songs('./网易云音乐')

    #print(musics)

    # 随机播放一首歌
    def sing_a_song(musics):
      # 随机选择一首音乐
      music = choice(musics)
      print(type(musics))
      pygame.mixer.music.load(music[0])
      pygame.mixer.music.play()
      print('开始播放：%s -- %s秒'%(music[0] , str(music[1])))
      return music

    # 画代表当前进度的圆点
    # 画一个直径为5个圆点，放在100,150的位置，颜色为(0,255,255)
    # dian = pygame.draw.circle(screen,(0,255,255),(begin_x,150),6)

    # 画播放控件
    def draw_kongjian(is_sing,is_pause):
      # 画进度条
      # 画一条宽度为2的线，y高度为149，x从40到600,颜色为(0,100,100)
      pygame.draw.line(screen, (0, 100, 100), (40, 149), (600, 149), 2)
      # 画播放、暂停按钮
      # 先画圆边框，半径20
      pygame.draw.circle(screen, (0, 255, 255), (x + 80, 100), 20, 2)
      # 画三角形，开始播放
      pygame.draw.line(screen, (0, 255, 255), (x + 73.7, 107.5), (x + 73.7, 93), 2) # 竖线
      # 如果正在播放且没有暂停
      if is_sing and not is_pause:
        # 隐藏三角形
        pygame.draw.line(screen, (0, 89, 115), (x + 73.7, 107.5), (x + 87.3, 100), 2)
        pygame.draw.line(screen, (0, 89, 115), (x + 73.7, 93), (x + 87.3, 100), 2)
        # 显示第二条竖线
        pygame.draw.line(screen,(0,255,255),(x+83.7,107.5),(x+83.7,93),2)
      else:
        # 隐藏第二条竖线
        pygame.draw.line(screen, (0, 89, 115), (x + 83.7, 107.5), (x + 83.7, 93), 2)
        # 显示三角形
        pygame.draw.line(screen,(0,255,255),(x+73.7,107.5),(x+87.3,100),2)
        pygame.draw.line(screen,(0,255,255),(x+73.7,93),(x+87.3,100),2)
      # 画上一首按钮
      pygame.draw.line(screen, (0, 255, 255), (x - 10, 110), (x - 10, 90), 2)
      pygame.draw.line(screen, (0, 255, 255), (x - 10, 100), (x + 10, 115), 2)
      pygame.draw.line(screen, (0, 255, 255), (x - 10, 100), (x + 10, 85), 2)
      pygame.draw.line(screen, (0, 255, 255), (x + 10, 115), (x + 10, 85), 2)

      # 画下一首按钮
      pygame.draw.line(screen, (0, 255, 255), (x + 170, 110), (x + 170, 90), 2)
      pygame.draw.line(screen, (0, 255, 255), (x + 170, 100), (x + 150, 115), 2)
      pygame.draw.line(screen, (0, 255, 255), (x + 170, 100), (x + 150, 85), 2)
      pygame.draw.line(screen, (0, 255, 255), (x + 150, 115), (x + 150, 85), 2)

    # 播放进度显示
    def move(current_time,start_time,pause_duration_time,c_music):
      if pause_end_time == 0 and pause_start_time != 0:
        duration_time = round(pause_start_time - start_time - pause_duration_time)
      else:
        duration_time = round(current_time - start_time - pause_duration_time)
      song_total_time = c_music[1]
      speed = (end_x-begin_x)/song_total_time
      current_x = begin_x + duration_time*speed
      try:
        screen.blit(dian,(current_x,148))
        pygame.display.update()
      except:
        print(current_time)
        print(start_time)
        print(pause_duration_time)
        exit()
        
    def draw_song_lyric(music):
      global current_time
      ly=open('网易云音乐/歌词/28012031','r',encoding='utf-8').read()
      lyc=ly.split('\\n')
      for l in lyc:
        wbl_obj = font_obj.render(l, True, (0, 255, 255))
        l_obj = wbl_obj.get_rect()
        l_obj.center = (340, 250)
        screen.blit(wbl_obj, l_obj)
        pygame.display.update()
    # 快进快退功能
    def kuaijin(jindu_x,c_music):
      # 要跳转到的距离d_x
      d_x = jindu_x - begin_x
      song_total_time = c_music[1]
      # 要跳转到的时间d_song_time
      d_song_time = round(song_total_time*(d_x/560),1)
      # 将歌曲快进到d_song_time
      pygame.mixer.music.play(0,d_song_time)

    if musics == []:
      print('文件夹中没有音乐！')
    else:

      while True:
        # 第一步画背景
        screen.fill((0, 0, 0)) # ----------------新添加
        # 第二步添加背景图片
        bg = pygame.image.load(music_bg)
        screen.blit(bg, (0, 0))
        # 第四步，画控件
        draw_kongjian(is_sing,is_pause)

        # 如果正在播放音乐，有bug == 当暂停后返回依旧是1
        if pygame.mixer.music.get_busy() == 1:
          is_sing = True
        else:
          is_sing = False

        # 如果没有在播放音乐
        if not is_sing:
          # 第五步，开始唱歌
          c_music = sing_a_song(musics)
          # 记录开始播放时间
          start_time = time.time()
          # 暂停时长置为0
          pause_start_time = pause_end_time = pause_duration_time = 0
          # 进度条开始位置重置为40
          begin_x = 40
          # 第六步，显示歌名
          draw_song_name(c_music)
          # 更改播放状态
          is_sing = not is_sing
        # 如果正在唱歌
        else:
          # 第六步，显示歌名
          draw_song_name(c_music)
          current_time = time.time()
          move(current_time, start_time, pause_duration_time, c_music)

        try:
          for event in pygame.event.get():
            if event.type == QUIT:
              pygame.quit()
              exit()
            if event.type == MOUSEBUTTONDOWN:
              # 如果点击了鼠标左键，取到当前鼠标的坐标
              pressed_array = pygame.mouse.get_pressed()
              if pressed_array[0] == 1:
                mouse_x, mouse_y = event.pos
                # 判断点击了哪个按钮
                if 80 < mouse_y < 120:
                  if x - 5 < mouse_x < x + 15:
                    # 点击了上一首
                    c_music = sing_a_song(musics)
                    is_pause = False
                    is_kuaijin = False
                    # 记录开始时间
                    start_time = time.time()
                    # 暂停时长置为0
                    pause_start_time = pause_end_time = pause_duration_time = 0
                    # 进度条开始位置置为40
                    begin_x = 40
                    # 第六步，显示歌名
                    draw_song_name(c_music)
                    print('点击了上一首')
                  elif x+60 < mouse_x < x+100:
                    # 修改是否暂停的状态
                    is_pause = not is_pause
                    # 如果没有暂停
                    if not is_pause:
                      # 开始播放
                      pygame.mixer.music.unpause()
                      # 记录结束暂定时间
                      pause_end_time = time.time()
                      # 计算暂停时长
                      pause_duration_time = pause_duration_time + pause_end_time - pause_start_time
                      # 暂停结束，暂停结束开始时间均置为0
                      pause_end_time = pause_start_time = 0
                    # 如果暂停了
                    else:
                      # 暂停播放
                      pygame.mixer.music.pause()
                      # 记录开始暂定时间
                      pause_start_time = time.time()

                    print('点击了暂停')
                  elif x+145 < mouse_x < x+170:
                    # 点击了下一首
                    c_music = sing_a_song(musics)
                    is_pause = False
                    is_kuaijin = False
                    # 记录开始时间
                    start_time = time.time()
                    # 暂停时长置为0
                    pause_start_time = pause_end_time = pause_duration_time =0
                    # 进度条开始位置置为40
                    begin_x = 40
                    # 第六步，显示歌名
                    draw_song_name(c_music)
                    print('点击了下一首')
                # 如果点了进度条的某个位置
                elif 155> mouse_y >145:
                  kuaijin(mouse_x,c_music)
                  begin_x = mouse_x
                  pause_end_time = pause_start_time = pause_duration_time = 0
                  move(current_time,start_time,pause_duration_time,c_music)
                  is_kuaijin = True
                  print("快进")

            pygame.display.update()
        except:
          pass
Player()