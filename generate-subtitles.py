import assemblyai as aai
from tkinter.filedialog import *

aai.settings.api_key = "6183b57b93b1460a91e69f4210a464f7"

file = askopenfilename()

transcript = aai.Transcriber().transcribe(file)

subtitles = transcript.export_subtitles_srt()

f = open("subtitles.srt", "a")
f.write(subtitles)
f.close()