import yt_dlp
import os


def download_youtube_video(url, save_path):
    try:
        # Baixar o melhor vídeo
        ydl_opts_video = {
            'outtmpl': os.path.join(save_path, '%(title)s_video.%(ext)s'),
            'format': 'bestvideo',
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_file = ydl.prepare_filename(info_dict)
            video_title = info_dict['title']
            print(f'Vídeo baixado com sucesso: {video_file}')

        # Baixar o melhor áudio
        ydl_opts_audio = {
            'outtmpl': os.path.join(save_path, '%(title)s_audio.%(ext)s'),
            'format': 'bestaudio',
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            audio_file = ydl.prepare_filename(info_dict)
            print(f'Áudio baixado com sucesso: {audio_file}')

        # Nome do arquivo de saída
        output_file = os.path.join(save_path, f'{video_title}.mp4')

        # Mesclar vídeo e áudio
        merge_command = f'ffmpeg -i "{video_file}" -i "{
            audio_file}" -c:v copy -c:a aac "{output_file}"'
        os.system(merge_command)
        print(f'Vídeo mesclado com sucesso: {output_file}')

        # Remover arquivos temporários
        os.remove(video_file)
        os.remove(audio_file)

    except Exception as e:
        print(f'Erro ao baixar ou mesclar o vídeo: {e}')


video_url = 'https://www.youtube.com/watch?v=WZU516GI3Ac&list=RDMMWZU516GI3Ac&start_radio=1'
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
save_path = os.path.join(downloads_path, 'Vídeos Youtube')

if not os.path.exists(save_path):
    os.makedirs(save_path)

download_youtube_video(video_url, save_path)
