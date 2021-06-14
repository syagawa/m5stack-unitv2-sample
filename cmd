ssh m5stack@unitv2.py
sudo chmod 666 /dev/null

scp ./server_core.py  m5stack@10.254.239.1:/media/sdcard/
cd ~/payload/
mv ./server_core.py ./_server_core.py
sudo cp /media/sdcard/server_core.py ./





sudo chmod 755 payload/server_core.py
sudo chown 501:staff ./payload/server_core.py
