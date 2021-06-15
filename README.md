# M5Stack UnitV2 shot image sample


## usage


1. Copy serve_core.py to UnitV2
    ```bash
    # @PC login to UnitV2 with ssh
    $ ssh m5stack@unitv2.py

    # @UnitV2 change /dev/null permission
    $ sudo chmod 666 /dev/null

    # @PC copy server_core.py to UnitV2
    $ scp ./server_core.py  m5stack@10.254.239.1:/media/sdcard/

    # @UnitV2 rename server_core.py
    $ sudo mv ~/payload/server_core.py ~/payload/_server_core.py

    # @UnitV2 copy server_core.py to ~/payload/
    $ sudo cp /media/sdcard/server_core.py ~/payload/

    ```
2. reboot UnitV2

3. Open `http://10.254.239.1/image_shot` in Browser.