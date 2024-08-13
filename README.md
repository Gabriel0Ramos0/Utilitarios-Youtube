# YouTube Video Downloader

Este script em Python permite baixar vídeos do YouTube com qualidade máxima de vídeo e áudio, e depois mescla ambos em um único arquivo `.mp4`.

## 🚨 Aviso Legal

**Este programa é fornecido para fins educacionais e pessoais.**  
O download de vídeos do YouTube pode violar os Termos de Serviço da plataforma. **Certifique-se de que você tem permissão para baixar o conteúdo antes de usá-lo.**  
Use este programa de acordo com a lei e respeite os direitos dos criadores de conteúdo.

## 🛠 Funcionalidades

- Baixa o melhor vídeo e áudio disponíveis.
- Mescla automaticamente o vídeo e o áudio em um arquivo `.mp4`.
- Suporte para vídeos individuais (não suporta listas de reprodução).

## 🔧 Instalação

1. Clone o repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install yt-dlp
    ```

3. Certifique-se de ter o **FFmpeg** instalado, pois ele é usado para mesclar o vídeo e o áudio:
    - No Windows, baixe o [FFmpeg aqui](https://ffmpeg.org/download.html) e adicione-o ao seu PATH.
    - No Linux/Mac, você pode instalar o FFmpeg via gerenciador de pacotes:
        ```bash
        sudo apt-get install ffmpeg  # Para Debian/Ubuntu
        brew install ffmpeg          # Para macOS usando Homebrew
        ```

## 🚀 Como Usar

1. Defina a URL do vídeo que deseja baixar e a pasta onde deseja salvar o arquivo:
    ```python
    video_url = 'https://www.youtube.com/watch?v=EXEMPLO'
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    save_path = os.path.join(downloads_path, 'Vídeos Youtube')
    ```

2. Execute o script:
    ```bash
    python youtube_downloader.py
    ```

3. O vídeo será baixado, mesclado com o áudio e salvo na pasta especificada.

## 📝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias ou correções.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
