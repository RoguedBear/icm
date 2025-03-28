#!/bin/sh
echo "Starting jar..."
echo "Possible PID: $$"
java -jar icm-2.1.2-jar-with-dependencies.jar &
# NOTE: If using wayland, the java commands needs to be changed since the gui stuff in icm is very reliant on X11
# Make sure to install xvfb:
# xvfb-run -a  java -jar icm-2.1.2-RoguedBear-1-jar-with-dependencies.jar &

echo "Setting up watch"
while true
do
  file_name=$(inotifywait -qe close_write -r log/ --format "%w%f")
  echo ${file_name}
  tail -n1 ${file_name} | ./send_telegram.py
  echo "Sent alert..."
done
