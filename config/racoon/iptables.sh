iptables -A INPUT -p udp -m udp --dport 500 -j ACCEPT
iptables -A INPUT -p udp -m udp --dport 4500 -j ACCEPT
iptables -A INPUT -p esp -j ACCEPT
iptables -A FORWARD -s 10.1.0.0/255.255.255.0 -j ACCEPT
iptables -t nat -A POSTROUTING -s 10.1.0.0/255.255.255.0 -o eth0 -j MASQUERADE

iptables --table nat --append POSTROUTING -o eth0 --jump MASQUERADE
