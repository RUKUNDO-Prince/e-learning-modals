import assemblyai as aai
from tkinter.filedialog import *

aai.settings.api_key = "6183b57b93b1460a91e69f4210a464f7"

file = askopenfilename()

transcript = aai.Transcriber().transcribe("meddy.mp4")

subtitles = transcript.export_subtitles_srt()

f = open(file, "a")
f.write(subtitles)
f.close()