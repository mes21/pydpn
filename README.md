# pydpn
 Python package for configuring a deeperNetwork device

# Install

  ```sh
  pip install pydpn
  ```

# Usage

## Python 

```python
from pydpn import DeeperNetwork

dpn = DeeperNetwork()
activeMode = dpn.mode.dpnMode
if activeMode != "smart":
    dpn.mode.set_dpnMode("smart")


```

## Commandline

```shell
C:\Users> dpn set-mode smart

C:\Users> dpn set-mode full EUW
```



## Config File

  For convineanc a json file can be saved under 
  
  ```path
  C:\Users\%USERPROFILE%\.dpn\config.json
  ```
  
  The contents must follow this style:
  ```json
    {
        "username":"example",
        "password": "example",
        "hostIp": "http://34.34.34.34",
        "proxy":"192.168.133.99:3128"
    }
```
  If no arguments are passed to the DeeperNetwork class in python script the class will look for the config file at this default place

  For commandline the config file is mandetroy

# DeeperNetwork

More information on the DeeperNetwork product can be found [**here**](https://shop.deeper.network/pages/deeper-connect-decentralized-vpn)

If you like the project consider buying your DeeperNetwork hardware with my affiliat [**link**](https://shop.deeper.network/?sca_ref=3122711.jthhvz8Ao8&sca_source=GitHub)

chears!