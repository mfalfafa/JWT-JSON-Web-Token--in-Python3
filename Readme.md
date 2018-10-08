### JWT (JSON Web Token) WEB API using Python 3 ###
#### miftahf77@gmail.com ####
#### MF ALFAFA ####
#### 25 September 2018 ####

> Connecting to hidden network

```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
network={
       ssid="your SSID"
       scan_ssid=1
       psk=your PSK 
}
sudo nano /etc/network/interfaces
auto lo
iface lo inet loopback

iface eth0 inet manual

allow-hotplug wlan0
iface wlan0 inet manual
    wpa-conf  /etc/wpa_supplicant/wpa_supplicant.conf


allow-hotplug wlan1
iface wlan1 inet manual
    wpa-conf  /etc/wpa_supplicant/wpa_supplicant.conf
```

> References

1. https://codereview.stackexchange.com/questions/46652/python-auth-using-requests
2. https://blog.apcelent.com/json-web-token-tutorial-with-example-in-python.html