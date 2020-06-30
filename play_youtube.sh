#!/bin/bash


YT_URL=$1

if [[ ! -d /tmp/ytdl ]]
then
    mkdir /tmp/ytdl
fi

cd /tmp/ytdl


ex_co=0
/usr/local/bin/youtube-dl -x --audio-format mp3 $YT_URL || ex_co=1


if [[ $ex_co -eq 0 ]]
then
    mp3file=$(ls /tmp/ytdl | grep '.mp3' | head -1)
else
    echo "$(date) - Failed to Download the the clip. Maybe youtube-dl needs to be updated." >> /home/pi/media_player.log
fi



echo "$(date) - Playing $mp3file" >> /home/pi/media_player.log
/usr/bin/omxplayer -s -o local "$mp3file"

cd /tmp
echo "$(date) - Deleting the file from the /tmp folder" >> /home/pi/media_player.log
rm -rfv /tmp/ytdl

