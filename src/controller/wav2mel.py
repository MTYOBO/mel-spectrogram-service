import librosa
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import matplotlib.pyplot as plt_waveform
import matplotlib.pyplot as plt_spectrogram
import matplotlib.style as ms
import librosa.display
import librosa.feature
#ms.use('seaborn-muted')
import os
from pathlib import Path
import librosa
import librosa.display
import IPython.display
import sys


def generate_mel_spectrogram_from_audio_batch_files(audio_folder, mel_spectrogram_folder):
    base_audio_path = os.path.expanduser('~/data/audio-files/') + audio_folder
    base_mel_spectrogram_path = os.path.expanduser('~/data/mel-spectrogram-datasets/') + mel_spectrogram_folder
    for path, folders, files in os.walk(base_audio_path):
        for folder in folders:
            list_of_audio_files = os.listdir(f"{path}/{folder}")
            for audio in list_of_audio_files:
                prefix_file_name = audio.split(".")[0]
                audio_full_path = base_audio_path + folder + "/" + audio
                mel_spectrogram_full_path = base_mel_spectrogram_path + "/" + folder + "/" + prefix_file_name + ".png"
                y, sr = librosa.load(audio_full_path)
                S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
                #mfccs = librosa.feature.mfcc(S=librosa.power_to_db(S))
                fig, ax = plt.subplots(nrows=1, sharex=True)
                #img = librosa.display.specshow(librosa.power_to_db(S, ref=np.max), x_axis='time', y_axis='mel',fmax=8000, ax=ax)
                #fig.colorbar(img, ax=ax)
                plt.savefig(mel_spectrogram_full_path)


generate_mel_spectrogram_from_audio_batch_files("audio-files-mini-speech-command/", "mel-spectrogram-mini-speech-commands")
