#!/usr/bin/bash
rm ~/emio-labs/v25.12.01/assets/labs/labsConfig.json
ln -fs "$(realpath labsConfig.json)" ~/emio-labs/v25.12.01/assets/labs/
ln -fs "$(realpath .)" ~/emio-labs/v25.12.01/assets/labs/
