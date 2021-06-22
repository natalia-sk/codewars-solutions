def song_decoder(song):
    old_song = ''

    for i in range(len(song)):
        if song[i:i+3] == 'WUB':
            old_song = song.replace(song[i:i+3], ' ')

    old_song = old_song.split(' ')
    while '' in old_song:
        old_song.remove('')

    return song if not old_song else ' '.join(old_song)
