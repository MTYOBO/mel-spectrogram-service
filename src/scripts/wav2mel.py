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
                audio_full_path = base_audio_path + "/" + folder + "/" + audio
                mel_spectrogram_full_path = base_mel_spectrogram_path + "/" + folder + "/" + prefix_file_name + ".png"
                y, sr = librosa.load(audio_full_path)
                S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
                fig, ax = plt.subplots()
                img = librosa.display.specshow(librosa.power_to_db(S, ref=np.max), fmax=8000, ax=ax)
                fig.patch.set_visible(False)
                ax.axis('off')
                plt.savefig(mel_spectrogram_full_path)
                plt.close()


def generate_mel_spectrogram_from_audio_file(audio_file_path, mel_spectrogram_path):
    y, sr = librosa.load(audio_file_path)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(librosa.power_to_db(S, ref=np.max), fmax=8000, ax=ax)
    fig.patch.set_visible(False)
    ax.axis('off')
    plt.savefig(mel_spectrogram_path)
    plt.close()


generate_mel_spectrogram_from_audio_batch_files("audio-files-gqrx/mono",
                                                "mel-spectrogram-files-gqrx")

# generate_mel_spectrogram_from_audio_batch_files("audio-files-gnuradio",
#                                                 "mel-spectrogram-gnu-radio")

# generate_mel_spectrogram_from_audio_batch_files("audio-files-mini-speech-command",
#                                                 "mel-spectrogram-mini-speech-commands")

# generate_mel_spectrogram_from_audio_batch_files("audio-files-gqrx",
#                                                 "mel-spectrogram-files-gqrx")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/down"
#                                          "/down6.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/down/down6.png")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/down"
#                                          "/down7.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/down/down7.png")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/down"
#                                          "/down8.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/down/down8.png")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/down"
#                                          "/down9.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/down/down9.png")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/down"
#                                          "/down10.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/down/down10.png")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/go"
#                                          "/go6.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/go/go6.png")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/go"
#                                          "/go7.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/go/go7.png")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/go"
#                                          "/go8.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/go/go8.png")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/go"
#                                          "/go9.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/go/go9.png")
#
# generate_mel_spectrogram_from_audio_file("/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/audio-files/go"
#                                          "/go10.wav",
#                                          "/home/ubuntu/data/mel-spectrogram-datasets/test_speech_gnu/mel-spectrogram"
#                                          "/go/go10.png")
