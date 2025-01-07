Target user: isabel
Method of solve: We need to brute force readable files in a directory where we have no read permissions
Key command:
cat dict.txt | xargs -I {} sh -c 'if [ -r /etc/xdg/{} ]; then echo "Readable file found: /etc/xdg/{}"; exit 0; fi' || echo "No readable file found in /etc/xdg directory."
