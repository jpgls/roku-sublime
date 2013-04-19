#!/bin/bash

zip -r $1.zip repo -x *.git*

curl -F "archive=@$1.zip;type=application/zip" -F "mysubmit=Replace" -H "Content-type:multipart/form-data" 192.168.0.1/plugin_install
