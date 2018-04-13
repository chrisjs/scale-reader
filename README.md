Things to do / consider. May not apply to this project directly so storing here before creating issues..

* Can /data be easily recreated in a failure?
* Backups for /data, disk images for SDcard and USB stick to restore from?
* Start reading from scale at system startup? Need to add error handling to keep reconnecting to
  scale if say for example it gets unplugged. Should there be some reporting so the UI can display
  a connection failure, etc?
* The battery status is available via an API, should that be displayed on the UI or depend on the LED's
  on the HAT and display through the case?


