import moviepy as mp 
import speech_recognition as sr 
import soundfile
video = mp.VideoFileClip(r"D:\WeekEndRide\videoplayback.mp4") 
# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile(r"D:\WeekEndRide\videoplayback.wav") 

r = sr.Recognizer()
data, samplerate = soundfile.read(r"D:\WeekEndRide\pythonCode\OSR_us_000_0060_8k.wav")
soundfile.write(r"D:\WeekEndRide\pythonCode\OSR_us_000_0060_8k22.wav", data, samplerate, subtype='PCM_16')
audio_file = sr.AudioFile(r"D:\WeekEndRide\pythonCode\OSR_us_000_0060_8k22.wav")

with audio_file as source:
	audio = r.record(source)
	text = r.recognize_google(audio)
	print(text)


# if len(sys.argv) < 2:
#     print(f'Plays a wave file. Usage: {sys.argv[0]} filename.wav')
#     sys.exit(-1)

# with wave.open(r"D:\WeekEndRide\Gullatty_Marandahalli\siaa.wav", 'rb') as wf:
#     # Define callback for playback (1)
#     def callback(in_data, frame_count, time_info, status):
#         data = wf.readframes(frame_count)
#         # If len(data) is less than requested frame_count, PyAudio automatically
#         # assumes the stream is finished, and the stream stops.
#         return (data, pyaudio.paContinue)

#     # Instantiate PyAudio and initialize PortAudio system resources (2)
#     p = pyaudio.PyAudio()

#     # Open stream using callback (3)
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True,
#                     stream_callback=callback)

#     # Wait for stream to finish (4)
#     while stream.is_active():
#         time.sleep(0.1)

#     # Close the stream (5)
#     stream.close()

#     # Release PortAudio system resources (6)
#     p.terminate()

