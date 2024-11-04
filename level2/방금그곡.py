def time_info(t):
    return int(t.split(':')[0])*60 + int(t.split(':')[1])

def change(word):
    word = word.replace("C#",'c').replace("D#",'d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#', 'b')
    return word

def solution(m, musicinfos):
    answer = []
    m = change(m)
    for info in musicinfos:
        start,end,name,music = info.split(',')
        music = change(music)
        T = time_info(end) - time_info(start)
        
        if T >= len(music):
            melody = music * (T//len(music)) + music[:T%len(music)]
        else:
            melody = music[:T]
        
        if m in melody:
            answer.append([-T, name])
    
    if len(answer) == 0:
        return '(None)'
    else:
        return sorted(answer)[0][1]