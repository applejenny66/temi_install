# Temi complete installation
** the whole steps for robot "Temi" installation.**
** Chinese version will be done in the future.**

## Environment
- python3
- ubuntu 20

## Set up a vitual env first
$: `python3 -m venv temi-env`
"tem-env" could change to the name you prefer.

$: `source temi-env/bin/activate`
to activate your virtual env

## Use pytemi to manipulate temi
Please refer to the link to clone or install pytemi:
<https://github.com/applejenny66/pytemi>

## build up the java environment
Because pytemi is not very powerful now, we need to write some java or kotlin codes to get more information from temi.
Here we choose java instead of kotlin.

step 1. go to the official website to download a version. <https://www.java.com/zh-TW/download/linux_manual.jsp>
 e.g. I use Linux x64

step 2. install it refer the this page. <https://www.java.com/zh-TW/download/help/linux_install.html>
e.g.  (java_name = java_download_file)
$: `sudo mkdir /usr/java`
$: `sudo cd /usr/java `
$: `sudo mv ~/Download/java_name .`
$: `sudo tar zxvf java_name`
$: `sudo rm -rf java_name`

step 3. go to download Eclipse <https://www.eclipse.org/downloads/download.php?file=/oomph/epp/2021-09/R/eclipse-inst-jre-linux64.tar.gz>

step 4. extract the Eclipse
e.g. 
$: `cd ~`
$: `mv ./Download/eclipse_name .`
$: `tar -xzvf eclipse_name`

step 5. install by clicking the extracted file
e.g. I get a dir name "eclipse-installer". Direct click the dir and click the "eclipse-inst". 
Just follow the hints and launch it.

step 6. install Android ADT
e.g. After launching the eclipse, you can find "Help" on the top.
click Help > Install New Software > Add > location: https://dl-ssl.google.com/android/eclipse/ > Select All > Add > Install anyway

step 7. go to download "Andriod SDK" <https://developer.android.com/studio>

step 8. extract Android SDK
e.g.
$: `cd ~`
$: `mv ./Download/android-studio-xxx.tar.gz .`
$: `tar -xzvf android-studio-xxx.tar.gz`

step 9. reboot your computer
e.g. $:`sudo reboot`

step 10. restart your eclipse and install Android SDK Build-tools
e.g.
click the eclipse icon to open it, then you will be reminded that the "Android SDK Build-tools is not installed".
Just follow the hints to complete the installation.
This step will take more time. Please wait a minute.

congratulate! You finish the java installation.
