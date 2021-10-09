#code to extract pw from wifi network
import subprocess
import re

def get_ssid():
    proc = subprocess.Popen(['netsh', 'wlan', 'show', 'profiles'], stdout=subprocess.PIPE)
    profiles = proc.communicate()[0].decode('utf-8').split('\n')[4:]
    profiles = [profile.split(":")[1][1:-1] for profile in profiles if "All User Profile" not in profile]
    return profiles

def get_pw(ssid):
    proc = subprocess.Popen(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'], stdout=subprocess.PIPE)
    pw = proc.communicate()[0].decode('utf-8').split('\n')[4].split(":")[1][1:-1]
    return pw