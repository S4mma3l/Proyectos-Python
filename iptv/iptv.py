import subprocess
import streamlink


def url_iptv(url):
    streams = streamlink.streams(url)
    if streams:
        return streams["best"].url

    return None


def reproductor(url_transmision):
    if url_transmision:
        subprocess.call(
            ["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe", url_transmision]
        )
    else:
        print("fallo")


if __name__ == "__main__":
    url_transmition_iptv = (
        "addrees"
    )

    url_transmicion = url_iptv(url_transmition_iptv)
    reproductor(url_transmicion)
