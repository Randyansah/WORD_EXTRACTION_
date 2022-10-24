import extractSpeech

# variable declarations
videoClip = "E:/ML_PROJECTS/WORD_EXTRACTION/DATASET.mp4"
audioClip = ""

# class instance
speechExtract = extractSpeech.SpeechExtraction(videoClip)

# video to audio conversion
audioClip = speechExtract.convertVideoCliptoMp3()

#recognize audio
speechExtract.recognizeAudio()

# extract audio text
speechExtract.exportAudioTextToTextFile()





