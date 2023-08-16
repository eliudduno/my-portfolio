from datetime import datetime
from playsound import playsound
import winsound


alarm_date = input('Ingresa la fecha para activar la alarma: ').strip()
alarm_time = ''.join(input('Ingresa el tiempo para activar la alarma, Ej. HH:MM,AM/PM: ').split())
print(alarm_time)
music_or_beep = input('Pulse para "m" para una musica o "b" para sonido: ')

if music_or_beep == 'b':
    dur = int(input('Duracion en segundos '))*1000 #winsound takes in milliseconds
    freq = int(input('Frequencia de el sonido entre 37 - 32767: ')) #optimal- 500

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_period = alarm_time[6:8]

print('Configurando alarmar...')


while True:
    current_time=datetime.now()
    current_hour=current_time.strftime('%I')
    current_minute=current_time.strftime('%M')
    current_period=current_time.strftime('%p')
    current_date=current_time.strftime('%d')
    
    if current_date==alarm_date and current_period==alarm_period and current_hour==alarm_hour and current_minute==alarm_minute:
        print('*'*10)
        print('| '+'Despierta!'+' |')
        print('*'*10)

        if music_or_beep == 'm':
            playsound('../Applications/Alarm/audio.wav')
        else:
            winsound.Beep(freq, dur)