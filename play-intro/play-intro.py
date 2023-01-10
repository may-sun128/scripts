import pyaudio  
import wave  
import os

# this script plays an intro sound
# I have it in my bspc init file

def set_env():
    os.chdir('/home/mholmes/.scripts/play-intro')
    print(os.getcwd())

def play(wave_file_path):
    #define stream chunk   
    chunk = 1024  

    #open a wav format music  
    f = wave.open(wave_file_path,"rb")  
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()  

set_env()
play('sunrise.wav')
