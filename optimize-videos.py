import os
import subprocess
from pathlib import Path

cwd = Path.cwd()
videos_path = Path('videos')
videos = sorted(videos_path.rglob('*.mp4')) + sorted(videos_path.rglob('*.mov'))

for video in sorted(videos):
    name = video.stem
    path = video.relative_to('videos')
    output_folder = ('static/videos' / path).parents[0]
    Path.mkdir(output_folder, parents=True, exist_ok=True)
    subprocess.call(["scripts/transcode-hls",
                     video,
                     f"{output_folder}/{name}"])
