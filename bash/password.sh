#!/bin/bash

if [ "$#" -ne 1 ]; then
    cd /etc/NetworkManager/system-connections/

    for f in *; do
      echo "id=$f"
      sudo cat $f | grep psk=
      echo -e ""
    done

    exit 0
else
    cd /etc/NetworkManager/system-connections/
    sudo cat $1 | grep psk=
    exit 0
fi
