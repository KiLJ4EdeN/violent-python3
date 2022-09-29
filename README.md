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
4. >[inject command through ssh using pxssh](./chapter02/ssh_pxssh_command.py)
5. >[brute force ssh password](./chapter02/ssh_brute.py)
6. >[brute force ssh key](./chapter02/ssh_brutekey.py)
7. >[bot net, (ssh to multiple machines instead of one, and do for example: ddos or ping flood from all of them at once)](./chapter02/ssh_botnet.py)
8. >[anonymous ftp conn](./chapter02/ftp_anon_login.py)
9. >[brute force ftp](./chapter02/ftp_brute_login.py)
10. >[ftp get served pages on server](./chapter02/ftp_default_pages.py)
11. >[ftp inject page](./chapter02/ftp_inject_page.py)
12. >[mass ftp attack](./chapter02/ftp_mass_compromise.py)
13. >[conficker](./chapter02/conficker.py)
14. >[free float overflow](./chapter02/free_float.py)

### chapter03
1. >[pdf meta](./chapter03/pdf_read.py)
2. >[fetch exif meta](./chapter03/exif_fetch.py)
3. >[parse skype db](./chapter03/skype_parse.py)
4. >[parse firefox db](./chapter03/firefox_parse.py) (at ~/.mozilla/firefox/{somename}.default-default/ on centos)
5. >[iphone massages](./chapter03/iphone_messages.py)

### chapter04
1. >[Geo locate IP](./chapter04/geo_ip.py)
2. >[Geo Print](./chapter04/geo_print.py)
3. >[Create Google Earth kml from pcap](./chapter04/google_earth_pcap.py)
4. >[Identify DDoS attack](./chapter04/find_ddos.py)
5. >[Print Request IP Directions](./chapter04/print_direction.py)
6. >[Spoofing Detection](./chapter04/spoof_detect.py)
7. >[mitnick attack](./chapter04/mitnick_attack.py)
8. >[foiling intrusion detection](./chapter04/ids_foil.py)

### extras
1. >[simple ddos](./extras/ddos.py)
2. >[ping flood](./extras/ping_flood.sh)
3. >[nmap decoy scan](./extras/nmap_decoy_scan.sh)
4. >[brute force wifi password](./extras/wifi_brute_force.py)
