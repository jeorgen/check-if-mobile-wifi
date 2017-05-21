# check-if-mobile-wifi
Checks if your computer is on a hotspot whose name starts with a certain string, if so returns True. Needs ```nmcli``` to be installed, so useful for Linux and similar.

The purpose is to check if it is a good idea to transfer a lot of files. So if you are using a mobile hotspot from your phone you may not want to do that.

Usage

    import checkmobilewifi

    # check for if hotspot name starts with "G2" on adapter "wlan0"
    checkmobilewifi.on_mobile() 

    # This one checks for if hotspot name starts with "FooBar" on adapter "wlan1"
    checkmobilewifi.on_mobile(prefix_identifier = 'FooBar', wireless_identifier = 'wlan1')
