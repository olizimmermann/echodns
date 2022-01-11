```
 ___    _        ___  _  _ ___ 
 | __|__| |_  ___|   \| \| / __|
 | _|/ _| ' \/ _ \ |) | .` \__ \
 |___\__|_||_\___/___/|_|\_|___/
                        v0.0.1
```


Analyze DNS traffic. 

EchoDNS shows all requested DNS traffic. It will forward the original packet to a real DNS server. You can choose the target DNS. Default is 1.1.1.1.
The endpoint won't notice this "FakeDNS" at all. With the usage of multithreading, EchoDNS will perfom requests very efficient. A builtin garbage collector takes care of leftover threads. You are able to change the max. amount of allowed threads. Default is set to 100.
EchoDNS generates a log file for ongoing investigations. The default size of the log files are 100kb. Please consider to change this size for longer investigation.

You will need sudo (admin) privileges to run this script. Port 53 is usually reserverd for explicit reasons.

Usage:
```sudo python3 echodns.py```

All requirements installed?
```pip install -r requirements.txt```


Example output:

![alt text](https://github.com/olizimmermann/echodns/blob/main/images/example.png?raw=true)
