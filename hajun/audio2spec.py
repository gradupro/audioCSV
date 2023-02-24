import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

path = '/Users/yoohajun/Desktop/grad_audio'

# 오디오 파일 로드
def generate_spectrogram(audio_dir, subdir, img_height, img_width):

    spec_dir_2 = os.path.join(spec_dir, subdir)
    if not os.path.exists(spec_dir_2):
        os.makedirs(spec_dir_2)
        print(f"{spec_dir_2} : vacant created")


    # subdir에 넣어 놓은 오디오 파일 loop
    for idx, filename in enumerate(os.listdir(audio_dir)):
        if filename.endswith('.wav'):
            # Load the audio file
            filepath = os.path.join(audio_dir, filename)
            y, sr = librosa.load(filepath, sr=22050)

            # 스펙트로그램 생성
            S = librosa.feature.melspectrogram(y=y, sr=sr)
            S_db = librosa.power_to_db(S, ref=np.max)

            # Resize spectrogram -> fixed shape
            S_resized = librosa.util.fix_length(S_db, size=img_width, axis=1, mode='constant')
            S_resized = S_resized[:img_height, :]
            print('spectrogram size : ', S_resized.shape)
            # Save -> spectrogram to image file
            spec_filename = filename[:-4] + '.png'
            spec_filepath = os.path.join(spec_dir_2, spec_filename)
            plt.imsave(spec_filepath, S_resized)

            print(f'{subdir}-{idx + 1}, {spec_filename} -> saved')

    print('finished')


def create_spec_dir(spec_dir):
    if not os.path.exists(spec_dir):
        os.makedirs(spec_dir)
        print(f"{spec_dir} : created")


def create_data_dirs():
    # Loop over subdirectories under the path directory
    folders = ['crime_robbery', 'crime_theft', 'exterior', 'interior', 'crime_sexual', 'crime_violence', 'help']

    for subdir in os.listdir(path):
        if subdir in folders:
            # Create the data directory if it doesn't exist
            data_dir = os.path.join(path, subdir, 'train')
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
                print(f"{data_dir} : vacant created")
            # Run the generate_spectrogram function for the data directory
            generate_spectrogram(data_dir, subdir, img_height=128, img_width=256)



# Define the output directory for the spectrogram images
spec_dir = os.path.join(path, 'spectrogram_fixed')

# Create the output directory
create_spec_dir(spec_dir)

create_data_dirs()
# Generate the spectrograms
