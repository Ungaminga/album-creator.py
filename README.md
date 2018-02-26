# album-creator.py
Creates video from mp3 files + logo pic for youtube upload. [Example](https://youtu.be/LBr9fia4HOk).
### Libs used:
* [moviepy](https://github.com/Zulko/moviepy)
* [mp3-tagger](https://github.com/artcom-net/mp3-tagger)
* [natsort](https://github.com/SethMMorton/natsort)

### Usage:
`album-creator.py album_directory <output.mp4>`

Your `album_directory` must contain `album.(png|jpeg|gif)`, which generator will use as image.
The creator will create track timestamps, that appears in programm output. You can use redirecting output (i.e. `>` or `>>`) to have file with timestamps or whatever.
