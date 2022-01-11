```
 ___    _        ___  _  _ ___ 
 | __|__| |_  ___|   \| \| / __|
 | _|/ _| ' \/ _ \ |) | .` \__ \
 |___\__|_||_\___/___/|_|\_|___/
                        v0.0.1
```


Analyze DNS traffic. 

EchoDNS shows all requested DNS traffic. It will forward the original packet to a real DNS server. You can choose the real DNS by you own.
It will generate a log file for ongoing investigations. The default size of the log files are 100kb. Please consider to change this size for an ongoing investigation.

You will need sudo privileges. Port 53 is reserverd for explicit reasons.

Usage:
```sudo python3 echodns.py```

All requirements installed?
```pip install -r requirements.txt```
