import yt_dlp
import os

def download_youtube_audio(url, save_path):
    try:
        # Baixar o melhor áudio disponível
        ydl_opts_audio = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'bestaudio',
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            audio_file = ydl.prepare_filename(info_dict)
            print(f'Áudio baixado com sucesso')

            # Converter para MP3 se necessário
            if not audio_file.endswith('.mp3'):
                mp3_file = os.path.splitext(audio_file)[0] + '.mp3'
                os.rename(audio_file, mp3_file)
            else:
                mp3_file = audio_file

            print(f'Áudio final em MP3: {mp3_file}')

    except Exception as e:
        print(f'Erro ao baixar ou converter o áudio: {e}')

video_url = 'https://www.youtube.com/watch?v=L3wKzyIN1yk'
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
save_path = os.path.join(downloads_path, 'Músicas Youtube')

if not os.path.exists(save_path):
    os.makedirs(save_path)

download_youtube_audio(video_url, save_path)
