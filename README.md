# dfwlb
dfwlb = dorm firewall login bot

A login is required to use the internet connection of the dorm. A barracuda firewall is used. It seems to be configured to logout the client if there is no activity for a certain amount of time (probably 24 hours). The firewall could be misconfigured as it happened multiple times already that I was logged out in the middle of a download. Furthermore one raspberry pi behind my router is running as a seedbox 24/7 and therefore generating traffic continuously. Still it occurs that Im getting logged out and my traffic is blocked. This script will run on the same pi and automatically log me in every few hours to prevent this from happening in the future.

Also the genius who set the firewall up thought it is a good idea to use username = password. Its very easy to bruteforce other logins as the firewall also seems to allow unlimited requests. Maybe it would even be possible to dos the webserver and after someone gets logged out prevent a new login. Still theres no real use for a login with a different account or blocking access for somebody else. Just a thought that it is possible.
