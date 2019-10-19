# -*- encoding:utf-8 -*-

import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl':  u"山下　憂　　ONE　LOVE" + '.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
         'preferredquality': '192'},
        {'key': 'FFmpegMetadata'},
    ],
}

ydl = youtube_dl.YoutubeDL(ydl_opts)
#info_dict = ydl.extract_info("https://www.youtube.com/watch?v=sr--GVIoluU", download=True)
info_dict = ydl.extract_info("https://www.youtube.com/watch?v=9AnGVYkgwzI", download=True)
追加」１
追加２
あああああああああああああああ