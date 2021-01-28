Networking related

# iptables
playground for iptables

First to redirect all outbound traffic to another IP.

For example, if you want to copy all the send traffic to another IP address, you can use iptables to route that.

Say, for a server which has two IP address: 192.168.11.107 and 10.1.2.10. Now there is a program send UDP package to 10.1.2.1:8765.

If you want repulicate the traffic to anther IP, say 192.168.11.107:8889.

Then below iptables rule will do the job:
```
sudo iptables -t nat -A OUTPUT -p udp -d 10.1.2.1 --dport 8765 -j DNAT --to-destination 192.168.11.107:8889
```


If want to redirect all port 8765 to 192.168.11.107:8889, then :
```
sudo iptables -t nat -A OUTPUT -p udp  --dport 8765 -j DNAT --to-destination 192.168.11.107:8889
```
# remote SSH to IoT device

Remote accessing an IoT device is very useful for debugging purpose.

However, the IoT device may not have public IP address. What is more, the PC you want to access the IoT device also does not have public IP address. So it is a private to private networking connection.

Here is how to use revert SSH to access a IoT device from home PC.

As both PC and IoT device don't have public address, the first thing is to have a bridge server which has public address. So if you are using AWS IoT, a AWS EC2 instance can use for this purpose.

Steps:

    Start an AWS EC2 instance(or any Linux server with public IP) , for example has public IP :200.200.200.200.
    From IoT device, initial a SSH connection with revert option to this EC2 instance. If you use AWS IoT, it can be done by a IoT jobs.

ssh -R  200000:localhost:22 yourusername@200.200.200.200

Now a tunnel is established with port forwarding the 20000 to IoT device port 22 (SSH port). 3) From you PC, SSH to this AWS EC2 instance, generate key pairs, and Upload your SSH public key to the 'Security credentials' .

ssh yourusername@200.200.200.200

    initial connection to IoT device. As tunnel has been built, you EC2 instance port 20000 will revert map to IoT device port 22.

ssh root@localhost -p 20000

