echo "install OpenJDK 11"
sudo apt update
sudo apt install openjdk-11-jdk

#echo "java -version"

java -version
sync

echo "install OpenJDK 8"
sudo apt install openjdk-8-jdk

java -version

sudo update-alternatives --config java

#sudo vim /etc/environment
#JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
#source /etc/environment
#echo $JAVA_HOME
# /usr/lib/jvm/java-11-openjdk-amd64
