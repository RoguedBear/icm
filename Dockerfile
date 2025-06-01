FROM ubuntu:24.04

# Install openjdk this way because other proper runtimes give error when icm tries to load the awt library. easier solution is installing jre through apt
RUN apt-get update -y \
  && apt-get install --no-install-recommends -y \
  libgl1-mesa-dri \
  inotify-tools \
  openjdk-11-jre \
  python3 \
  python3-requests \
  xvfb \
  && rm -rf /var/lib/apt/lists/*

RUN groupadd -g 2000 icm && useradd -m -u 2000 -g icm icm
USER icm

WORKDIR /home/icm/icm

RUN mkdir log

# i dont want to waste an afternoon figuring out why new jar created from maven
# isnt working. Better to use the jar i created years back 
ADD --chown=2000:2000 https://github.com/RoguedBear/icm/releases/download/v2.1.2-RoguedBear-1/icm-2.1.2-RoguedBear-1-jar-with-dependencies.jar .

COPY README.md LICENSE  /home/icm/icm/
COPY --chown=2000:2000 --chmod=540 send_telegram.py wait_for_change.sh /home/icm/icm/

# coment out the regular java -jar cmd and use the xvfb cmd
RUN sed -i '4s/^/## /; 7s/^# //' ./wait_for_change.sh

ENTRYPOINT  [ "/home/icm/icm/wait_for_change.sh" ]
