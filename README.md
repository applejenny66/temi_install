# Temi complete installation
** The whole steps for robot "Temi" installation.**

** Chinese version will be done in the future.**

## Environment
- python3
- ubuntu 20

## Set up a vitual env first
$: `python3 -m venv temi-env`
"temi-env" could change to the name you prefer.

$: `source temi-env/bin/activate`
to activate your virtual env

## Mosquitto install (MQTT)
To use pytemi, we use tools “mosquitto” to help us.  
First, we’d like to make sure the version of mosquitto, so we remove all related to make the environment clear.  

e.g.  
$: `sudo apt-get purge --remove mosquitto*` (remove mosquitto, mosquitto-clients, mosquitto-dev)  
$: `sudo apt-add-repository --remove ppa:mosquitto-dev/mosquitto-ppa` (remove repository type)   

Then, follow the link: <https://www.arubacloud.com/tutorial/how-to-install-and-secure-mosquitto-on-ubuntu-20-04.aspx>  

$: `sudo apt update -y && sudo apt install mosquitto mosquitto-clients -y`  
$: `sudo systemctl status mosquitto`  
$: `sudo systemctl enable mosquitto`  
$: `sudo systemctl start mosquitto`  

When you check the status,  
- if you see "activate", you are successful!  
- if you see "failed", I just reboot my computer to solve this problem.   

Also, to subscribe to a topic, respect the following syntax:  
$: `mosquitto_sub -h address -t topic`  


## Use pytemi to manipulate temi
Please refer to the link to clone or install pytemi:  
<https://github.com/applejenny66/pytemi>  

## Build up the java environment
Because pytemi is not very powerful now, we need to write some java or kotlin codes to get more information from temi.  
First, we build the java environment.

**step 1.** Go to the official website to download a version. <https://www.java.com/zh-TW/download/linux_manual.jsp>  
e.g. I use Linux x64  

**step 2.** Install it refer the this page. <https://www.java.com/zh-TW/download/help/linux_install.html>  
e.g.  (java_name = java_download_file)  
$: `sudo mkdir /usr/java`  
$: `sudo cd /usr/java `  
$: `sudo mv ~/Download/java_name .`  
$: `sudo tar zxvf java_name`  
$: `sudo rm -rf java_name`  

**step 3.** Go to download Eclipse <https://www.eclipse.org/downloads/download.php?file=/oomph/epp/2021-09/R/eclipse-inst-jre-linux64.tar.gz>  

**step 4.** Extract the Eclipse  
e.g.   
$: `cd ~`  
$: `mv ./Download/eclipse_name .`  
$: `tar -xzvf eclipse_name`  

**step 5.** Install by clicking the extracted file  
e.g. I get a dir name "eclipse-installer". Direct click the dir and click the "eclipse-inst".  
Just follow the hints and launch it.  

**step 6.** Install Android ADT  
e.g. After launching the eclipse, you can find "Help" on the top.  
click Help > Install New Software > Add > location: https://dl-ssl.google.com/android/eclipse/ > Select All > Add > Install anyway  

**step 7.** Go to download "Andriod SDK" <https://developer.android.com/studio>  

**step 8.** Extract Android SDK  
e.g.  
$: `cd ~`  
$: `mv ./Download/android-studio-xxx.tar.gz .`  
$: `tar -xzvf android-studio-xxx.tar.gz`  

**step 9.** Reboot your computer  
e.g. $:`sudo reboot`  

**step 10.** Restart your eclipse and install Android SDK Build-tools  
e.g.  
click the eclipse icon to open it, then you will be reminded that the "Android SDK Build-tools is not installed".  
Just follow the hints to complete the installation.  
This step will take more time. Please wait a minute.  

Congratulate! You finish the java installation.  


## intelliJ IDEA (community) install  
To write kt code, first download intelliJ IDEA.  

Download link: <https://www.jetbrains.com/idea/download/download-thanks.html?platform=linux&code=IIC>  

and extract it.  
e.g. $: `tar -xzvf “idea-xxx”`  

To start the “jetbrains-idea-ce”, please refer to the file “ideal-IC/Install-Linux-tar.txt”.  
e.g.  
$: `cd ~/ideal-IC/bin`  
$: `./idea.sh`  

## ADB (Android Debug Bridge) install  
$: `sudo apt-get install android-tools-adb`  

To check for the devices connection:  
$:  `sudo adb devices`  

Some useful related command:  
Print a list of connected devices: `adb devices`  
Kill the ADB server: `adb kill-server`  
Install an application: `adb install <path_to_the_APK>`  
Set up port forwarding: `adb forward tcp:6100 tcp:7100`  
Copy a file/directory from the device: `adb pull <path_to_the_remote_object> <path_to_the_local_destination>`  
Copy a file/directory to the device: `adb push <path_to_the_local_object> <path_to_the_remote_destination>`  
Initiate an ADB shell: `adb shell`  
