> When we open up the packet capture in Wireshark, we can order the packets by time. We notice that there's a bunch of 12-length packets followed by a single 4-length packet. We can select the contents of the packets in the hex-view and select the contents as ASCII characters, then use Linux commands to decode the base64 strings.
```
echo -n 'cGljb0NURg==' | base64 -d
echo -n 'ezF0X3c0cw==' | base64 -d
echo -n 'bnRfdGg0dA==' | base64 -d
echo -n 'XzM0c3lfdA==' | base64 -d
echo -n 'YmhfNHJfZA==' | base64 -d
echo -n 'NGI1NzkwOQ==' | base64 -d
echo -n 'fQ==' | base64 -d
```
Finis
