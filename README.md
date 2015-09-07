#Geotagx-UNASIGN-sourcerer
Generates/Syncs a tasks.csv (compatible with Pybossa) from the UNASIGN data feeds

#Usage
```bash
git clone --recursive https://github.com/geotagx/geotagx-UNASIGN-sourcerer.git
cd geotagx-UNASIGN-sourcerer
pip install -r requirements.txt
python geotagx-unasign-sourcerer.py 
# Will both create and sync the tasks.csv with the UNASIGN data feed in question
# Will also push new unseen images to geotagx-sourcerer-proxy
```

#Quick Tips
You can setup a cronjob to run this at particular intervals to time to keep your project in sync with the UNASIGN data feed   
You can learn more about cronjobs here : http://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800

#Author
S.P. Mohanty <sp.mohanty@cern.ch>   
