# Connect to remote server

Make sure you have installed openssh-client at your local.  
$: `sudo apt-get install openssh-client`  
Then make sure the openssh-server is installed in server.  
$ `sudo apt-get install openssh-server`  

## Connect by ssh
$: `ssh -p 2223 hihapaddy@192.168.10.77`  
and then enter the password.  

## Transmit your file at local to server by “scp”   

Please notice that the post set is 22. If you use other ports, please refer to the below.  

$: ` scp filename user@remote_ip:/dir/file`  
e.g.  `scp test.py basia@192.168.0.1:/home/`  


If your port is 86, then 
$: `scp -P 86 filename user@remote_ip:/dir/file`  
e.g. `scp -P 86 basia@192.168.0.1:/home/test.py`  
(vice versa)

If you’d like to transmit a directory, not a file, then
$: `scp -r dir user@remote_ip:/home/dir`  
e.g. `scp -r test basia@192.168.0.1:/home/`  
(vice versa)

## Transmit file at remote to your local  
$: `scp user@remote_ip:/dir/file .`  
e.g. `scp basia@192.168.0.1:/home/test.py .`  
