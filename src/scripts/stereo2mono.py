import os
from pydub import AudioSegment


def convert_stereo_to_mono_files(stereo_path, mono_path):
    stereo_path = os.path.expanduser('~/data/audio-files/') + stereo_path
    mono_path = os.path.expanduser('~/data/audio-files/') + mono_path
    for path, folders, files in os.walk(stereo_path):
        for folder in folders:
            list_of_audio_files = os.listdir(f"{path}/{folder}")
            for audio in list_of_audio_files:
                stereo_full_path = stereo_path + "/" + folder + "/" + audio
                stereo_audio = AudioSegment.from_file(stereo_full_path, format="wav")
                mono_audios = stereo_audio.split_to_mono()
                mono_full_path = mono_path + "/" + folder + "/" + audio
                mono_audios[0].export(mono_full_path, format="wav")


convert_stereo_to_mono_files("audio-files-gqrx/stereo", "audio-files-gqrx/mono")
