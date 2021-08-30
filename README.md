## Changes:
This fork adds 2 new files and needs just the jar with the dependencies from the original repository to function.

you need to download `inotify-tools` (`sudo apt install inotify-tools`) and replace the placeholder texts in line [17](https://github.com/RoguedBear/icm/blob/f564e1044a606196e826e344ee104dce3c3f688f/send_telegram.py#L17) and [18](https://github.com/RoguedBear/icm/blob/f564e1044a606196e826e344ee104dce3c3f688f/send_telegram.py#L18) in [`send_telegram.py`](send_telegram.py) with your own Bot token and your chat id.


The `inotifywait`blocks until a new log file is detected/modified in the `log/` subdirectory and then passes the filename to `tail` which fetches the last line and passes to `./send_telegram.py`.

**PS:** you might need to make `send_telegram.py` executable before running. (`chmod +x send_telegram.py`)


# icm
icm (Internet Connectivity Monitoring) monitors your internet connection uptime and logs each outage. If your internet has been unstable or unreliable icm can help identify how often and for how long your connection is down. It will optionally play .wav files and/or hit GET endpoints on connect and disconnect. Although a windows executable is provided, it is 100% java and should be portable across platforms via the jar distribution.<br/>

Connectivity is monitored by testing DNS resolution every 7 seconds, and on failure, it will test every 1 second until it has succeeded 5 times.
Values, sound clips and urls are configurable in the properties file. By default, it will create a "log" folder in the current directory on startup. This can be altered via the UI "save path" setting.<br/>

The GET endpoint settings can be used as home automation hooks, either notifying you of the outage or activating a backup router. Make sure these URLs are available on your local network.<br/>

DNS resolution is via the DNSJava library and (by default) uses Google, Cloudflare, Quad9 and OpenDNS servers in rotation. 
<br/>
<p/>

<h2>Credits</h2>
This is a hard fork of "Internet Connectivity Montitor" 1.41 with many fundamental changes (see https://code.google.com/archive/p/internetconnectivitymonitor/).<br/>
It includes source from jhlabs, please see http://www.jhlabs.com/java/layout/.<br/>
