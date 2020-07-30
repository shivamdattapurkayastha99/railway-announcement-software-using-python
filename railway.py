import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
def texttospeech(text,filename):
    text1=str(text)
    language='hi'
    obj=gTTS(text=text1,lang=language,slow=True)
    obj.save(filename)
def mergeaudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined
def generateskeleton():
    audio=AudioSegment.from_mp3('rail.mp3')
    # from city
    start=0
    finish=6000
    audioprocessed=audio[start:finish]
    audioprocessed.export("hindi0.mp3",format="mp3")
    # se chalkar
    start=7000
    finish=10000
    audioprocessed=audio[start:finish]
    audioprocessed.export("hindi1.mp3",format="mp3")
    # via
    start=10000
    finish=14000
    audioprocessed=audio[start:finish]
    audioprocessed.export("hindi2.mp3",format="mp3")
    # train no and train name
    start=14000
    finish=17000
    audioprocessed=audio[start:finish]
    audioprocessed.export("hindi3.mp3",format="mp3")
    # to city
    start=18000
    finish=20000
    audioprocessed=audio[start:finish]
    audioprocessed.export("hindi4.mp3",format="mp3")
    # platform
    start=21000
    finish=23000
    audioprocessed=audio[start:finish]
    audioprocessed.export("hindi5.mp3",format="mp3")

    # start=16000
    # finish=18000
    # audioprocessed=audio[start:finish]
    # audioprocessed.export("hindi6.mp3",format="mp3")

    # start=18000
    # finish=19000
    # audioprocessed=audio[start:finish]
    # audioprocessed.export("hindi7.mp3",format="mp3")
def generateannouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        texttospeech(item['from'],'hindi0.mp3')
        texttospeech(item['via'],'hindi1.mp3')
        # texttospeech(item['to'],'hindi3.mp3')
        texttospeech(item['train no'],'hindi2.mp3')
        texttospeech(item['train name'],'hindi3.mp3')

        texttospeech(item['to'],'hindi4.mp3')
        texttospeech(item['platform'],'hindi5.mp3')
        audios=[f"hindi{i}.mp3"for i in range(0,6)]
        announcement=mergeaudios(audios)
        announcement.export(f"announcement{item['train no']}{index}.mp3",format="mp3")


if __name__ == "__main__":
    print("generating skeleton")
    generateskeleton()
    print("NOW generating announcement")
    generateannouncement("train.xlsx")

