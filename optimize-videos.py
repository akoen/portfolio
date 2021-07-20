import os
import subprocess
from pathlib import Path

cwd = Path.cwd()
videos_path = Path('videos')
videos = sorted(videos_path.rglob('*.mp4')) + sorted(videos_path.rglob('*.mov'))

for video in sorted(videos):
    name = video.stem
    path = video.relative_to('videos')
    output_folder = ('assets/videos' / path).parents[0]
    Path.mkdir(output_folder, parents=True, exist_ok=True)
    subprocess.call([
        "ffmpeg",
        "-n",
        "-i",
        video,
        "-vf",
        "thumbnail,scale=400:-1",
        "-frames:v",
        "1",
        f"{output_folder}/{name}.thumb.jpg"])

    subprocess.call([
        "ffmpeg",
        "-n",
        "-i",
        video,
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-profile:v",
        "baseline",
        "-level",
        "3.0",
        "-preset",
        "veryslow",
        "-crf",
        "28",
        "-r",
        "24",
        "-c:a",
        "aac",
        "-vf",
        "scale=720:-2",
        "-movflags",
        "+faststart",
        "-threads",
        "0",
        f"{output_folder}/{name}.h264.mp4"])

    subprocess.call([
        "ffmpeg",
        "-n",
        "-i",
        video,
        "-c:v",
        "libx265",
        "-pix_fmt",
        "yuv420p",
        "-preset",
        "veryslow",
        "-crf",
        "28",
        "-r",
        "24",
        "-c:a",
        "aac",
        "-tag:v",
        "hvc1",
        "-vf",
        "scale=720:-2",
        "-movflags",
        "+faststart",
        "-threads",
        "0",
        f"{output_folder}/{name}.h265.mp4"])

    subprocess.call(
        ["ffmpeg",
         "-n",
         "-i",
         video,
         "-c:v",
         "libvpx-vp9",
         "-pix_fmt",
         "yuv420p",
         "-b:v",
         "1M",
         "-r",
         "24",
         "-c:a",
         "libopus",
         "-b:a",
         "128k",
         "-vf",
         "scale=720:-1",
         f"{output_folder}/{name}.vp9.webm"])
exit(1)


# https://evilmartians.com/chronicles/better-web-video-with-av1-codec
# https://engineering.fb.com/2018/04/10/video-engineering/av1-beats-x264-and-libvpx-vp9-in-practical-use-case/


# for file in ${FAVOURITES_DIR_REMOTE}/*.{mov,mp4}; do
#     base=$(basename "${file%.*}")
#     dur=$(ffprobe -loglevel error -show_entries format=duration -of default=nk=1:nw=1 "$file")


    # ffmpeg -n -i "$file" -c:v libx265 -crf 28 -preset veryslow -pix_fmt yuv420p -movflags +faststart -tag:v hvc1 -c:a aac -vf scale=720:-2 "$FAVOURITES_DIR_LOCAL/${base}.mp4"

    # ffmpeg -n -i "$file" -c:v libx264 -pix_fmt yuv420p -profile:v baseline -level 3.0 -preset veryslow -crf 28 -acodec aac -vf scale=720:-2 -movflags +faststart -threads 0 "$FAVOURITES_DIR_LOCAL/${base}.mp4"

#     # ffmpeg -n -i "$file" -c:v libaom-av1 -pix_fmt yuv420p -crf 38 -movflags +faststart -b:v 0 -acodec libopus -vf scale=720:-2 -threads 0 "$FAVOURITES_DIR_LOCAL/${base}.mp4"

#     ffmpeg -n -i "$file" -ss "$(echo "$dur / 1.5" | bc -l)" -vframes 1 -filter "scale=400:-1" -q:v 2 "$FAVOURITES_DIR_LOCAL/video-thumbs/${base}.jpg"

#     ffmpeg -n -i "$file" -c:v libvpx-vp9 -pix_fmt yuv420p -b:v 1M -c:a libopus -b:a 128k -vf scale=720:-1 "$FAVOURITES_DIR_LOCAL/video-webm/${base}.webm"


# done
