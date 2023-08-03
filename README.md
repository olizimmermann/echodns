
# EchoDNS

```
 ___    _        ___  _  _ ___ 
 | __|__| |_  ___|   \| \| / __|
 | _|/ _| ' \/ _ \ |) | .` \__ \
 |___\__|_||_\___/___/|_|\_|___/
                        v0.0.2
```


**Analyze DNS traffic with EchoDNS**

EchoDNS is a powerful tool designed to analyze DNS traffic by acting as a DNS server, intercepting and forwarding requests to a real DNS server of your choice without being detected. It offers a multithreading feature to process requests more efficiently, and a built-in garbage collector automatically cleans up stuck threads, ensuring optimal performance.

## Features

- Intercept and analyze DNS traffic
- Forward DNS packets to a real DNS server (default: Google DNS)
- Efficient multithreading for improved performance
- Automatic thread cleanup using a built-in garbage collector
- Command-line configuration for customizing various parameters

## Prerequisites

- **sudo (admin) privileges**: EchoDNS requires administrative privileges to operate effectively because port 53 is usually reserved. You need root permission to use that port.

## Getting Started

Follow these simple steps to get started with EchoDNS:

1. Clone this repository to your local machine.
2. Ensure you have Python 3+ installed (link to Python installation guide).
3. Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

4. Modify the configuration using command-line arguments:

```bash
usage: echodns.py [-h] [-d DNS] [-t THREADS] [-a AGE] [-p PORT] [-i IP] [-l LOG_SIZE]

EchoDNS - DNS traffic analyzer

optional arguments:
  -h, --help            show this help message and exit
  -d DNS, --dns DNS     DNS server to forward requests to (default: Google DNS)
  -t THREADS, --threads THREADS
                        Max amount of threads (default: 100)
  -a AGE, --age AGE     Max age of thread in seconds (default: None)
  -p PORT, --port PORT  Local port to listen (default: 53)
  -i IP, --ip IP        Local IP to listen (default: 127.0.0.1)
  -l LOG_SIZE, --log-size LOG_SIZE
                        Max size of log in KB (default: 100KB)
```

5. Run the EchoDNS script with sudo privileges and customize the parameters as needed:

```bash
sudo python echodns.py -d 8.8.8.8 -t 200 -a 3 -p 53 -i 192.168.1.10 -l 512000
```

Example output:

![alt text](https://github.com/olizimmermann/echodns/blob/main/images/example.png?raw=true)

### Filter your output with grep

If you are using Linux (or anything else with grep), just pipe the output through it to filter for an explicit domain. 

```sudo python3 echodns.py | grep google.com```

## Contributing

We welcome contributions from the community to make EchoDNS even better! If you want to contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to merge your changes into the main repository.

## License

EchoDNS is distributed under the Apache License. See the [`LICENSE`](LICENSE) file for more details.


## Contact

For any inquiries or feedback, please create an issue.

---
This readme is a work in progress, and more details will be added soon. Thank you for your understanding as we continue to improve EchoDNS for an even better experience. Happy analyzing!

---

If you have any further questions or need more information, feel free to ask!

