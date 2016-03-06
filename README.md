# check-if-mobile-wifi
Checks if your computer is on a hotspot whose name start with certain string, if so returns True. Needs nmcli to be installed, so useful for Linux and similar.

Usage

import checkmobilewifi

# check for if hotspot name starts with "G2" on adapter "wlan0"
checkmobilewifi.on_mobile() 

# This one checks for if hotspot name starts with ```FooBar``` on adapter ```wlan1```
checkmobilewifi.on_mobile(prefix_identifier = "G2", wireless_identifier = 'wlan0')
