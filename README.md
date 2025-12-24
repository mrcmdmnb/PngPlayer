zh-cn
语言:python3
预备库:{
    opencv
    pygame
    regex
    time
}
使用方法:{
    将图片放入pic文件
    如有音频 将其名称改为snd.mp3并直接放到主目录中
    在当前目录中启动cmd
    输入'python main.py'
    按esc退出
}
settings.txt说明:{
    Num_of_Pictures:图片数量
    Pixal_row:图片像素 行
    Pixal_col:图片像素 列
    snd_vol%:声音大小(如没有则填0)
    wait:图片间隔时间(ms)
    win_x:窗口x坐标
    xin_y:窗口y坐标
    ismusic:有没有音乐文件 有填1 否则填0
}
注意:{
    图片播放顺序由图片名称决定
    图片名称必须是数字 并且这个数字决定这张图片的播放顺序
    音频文件直接拖动到player文件夹 且名称必须为snd.mp3
}
en-us
Programming language: Python3
Prerequisite Libraries: {
    opencv
    pygame
    regex
    time
}
Instructions: {
    Place images into the 'pic' folder
    If there is audio, rename it to 'snd.mp3' and place it directly in the main directory
    Open cmd in the current directory
    Type 'python main.py'
    Press Esc to exit
}
Settings.txt Description: {
    Num_of_Pictures: Number of pictures
    Pixal_row: Picture pixel rows
    Pixal_col: Picture pixel columns
    snd_vol%: Audio volume (if no audio, enter 0)
    wait: Interval between pictures (ms)
    win_x: Window X coordinate
    win_y: Window Y coordinate
    ismusic: Whether there is a music file (enter 1 for yes, otherwise 0)
}
Note: {
    The playback order of pictures is determined by their file names
    File names must be numbers, and these numbers determine the playback order of the pictures
    Audio files should be directly dragged into the player folder, and the name must be 'snd.mp3'
}
