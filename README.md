# VIOLENT-PYTHON 3

series of my studies to understand networking more based off of the book "Violent Python" by TJ O'Connor.



### installation

install bluetooth dev
```bash
sudo yum install bluez-libs-devel
# or on ubuntu
sudo apt-get install libbluetooth-dev
```

create environment and install deps
```bash
python -m venv env
pip install -r requirements.txt
sudo ${yum|apt-get} install nmap
```


### chapter01
1. >[unix password cracker using dictionary attack](./chapter01/passwd_crack.py)
2. >[zip file cracker](./chapter01/zip_crack.py)

### chapter02
1. >[port scan](./chapter02/port_scan.py)
2. >[nmap scan](./chapter02/nmap_scan.py)
3. >[inject command (for example alias cd='rm -rf') through ssh](./chapter02/ssh_command.py)