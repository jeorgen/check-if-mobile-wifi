import subprocess

def on_mobile(prefix_identifier = "G2", wireless_identifier = 'wlan0'):
    COMMAND = ['nmcli','c']
    pipes = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    networks, std_err = pipes.communicate()
    res = [network.split()[0] for network in networks.split('\n') if network.rstrip().endswith(wireless_identifier)]
    if res and res[0].startswith(prefix_identifier):
        return True
    else:
        return False