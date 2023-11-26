#!/bin/bash
for filename in frame*.png; do ffmpeg -i $filename -y -vf scale=-1:512 512"$filename"; done
