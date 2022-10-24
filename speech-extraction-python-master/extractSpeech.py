# from library
import speech_recognition
import moviepy.editor as moviepy
import librosa 
import os

class SpeechExtraction:
    VideoClipFile = ""
    ConvertedClipFile = "converted.wav"
    audio_path = "converted.wav" #By default
    clip = ""
    audio = ""
    result = ""
    recognized_text_file = ""
    
    ####
    # Class constructor
    #Takes two parameters
    #   -the video clip file path.
    #   -the converted clip file.
    # ####
    def __init__(self, VideoClipFile):
        self.VideoClipFile = VideoClipFile

    ####
    # conversion of the video clip file to an audio file.
    # writes the audio file to path.
    # parameter passed, instance of this class, self.
    ####
    def convertVideoCliptoMp3(self):
        self.clip = moviepy.VideoFileClip(self.VideoClipFile) 
        
        if os.path.exists(self.audio_path):
            os.remove(self.audio_path)
            self.clip.audio.write_audiofile(self.audio_path)
        else:
            self.clip.audio.write_audiofile(self.audio_path)
            
        return self.clip

    ####
    # Recognizes the audio text from the converted wav file
    # parameter passed,instance of this class, self.
    ####
    def recognizeAudio(self):
        recognizer = speech_recognition.Recognizer() 
        self.audio = speech_recognition.AudioFile(self.audio_path)

        with self.audio as source:
            duration = librosa.get_duration(filename=self.audio_path)  
            audio_file = recognizer.record(source, duration=duration)
            
        self.result = recognizer.recognize_google(audio_file)
        
        return self.result

    ####
    #If text file to save audio text recognized, the system creates the text file.
    # Exports audio text to a file.
    ####
    def exportAudioTextToTextFile(self):
        self.result = self.recognizeAudio()
        self.recognized_text_file = "recognized.txt"
        
        if os.path.exists(self.recognized_text_file):
            pass
        else:
            os.mkdir(self.recognized_text_file)
        
        with open(self.recognized_text_file, mode ='w') as file: 
            file.write("Recognized Speech:") 
            file.write("\n") 
            file.write(self.result) 
            print("ready!")


