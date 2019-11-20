# iptables
playground for iptables
First to redirect all outbound traffic to another IP.
For example, if you want to copy all the send traffic to another IP address, you can use iptables to route that.
Say, for a server which has two IP address: 192.168.11.107 and 10.1.2.10. Now there is a program send UDP package to 10.1.2.1:8765.
If you want repulicate the traffic to anther IP, say 192.168.11.107:8889.
Then below iptables rule will do the job:\
"sudo iptables -t nat -A OUTPUT -p udp -d 10.1.2.1 --dport 8765 -j DNAT --to-destination 192.168.11.107:8889"
\
If want to redirect all port 8765 to 192.168.11.107:8889, then \
sudo iptables -t nat -A OUTPUT -p udp  --dport 8765 -j DNAT --to-destination 192.168.11.107:8889
