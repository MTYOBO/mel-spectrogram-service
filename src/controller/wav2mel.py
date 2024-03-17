import librosa
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as ms
#ms.use('seaborn-muted')

import librosa
import librosa.display
import IPython.display

#base_path = "../../data/audio-files/"

y, sr = librosa.load('/home/ubuntu/dev/mel-spectrogram-service/data/audio-files/down/0a9f9af7_nohash_0.wav')

S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, n_fft=1024)

log_S = librosa.db_to_amplitude(S_db=S)

plt.figure(figsize=(12,4))

librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')

plt.title('mel power spectrogram')

plt.colorbar(format='%+02.0f dB')

plt.tight_layout()

plt.savefig('/home/ubuntu/dev/mel-spectrogram-service/data/audio-files/down/0a9f9af7_nohash_0.png')




