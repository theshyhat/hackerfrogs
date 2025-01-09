# Target user:
celeste
# Method of solve:
We needed to fuzz the localhost website for a valid page based on a list of potential endpoint names
# Key commands:
sed 's/$/.html/' pages.txt > url.txt
cat url.txt | xargs -I {} sh -c 'response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/{}); if [ "$response" -eq 200 ]; then echo "Valid endpoint found: http://localhost/{}"; else echo "Invalid or inaccessible endpoint: http://localhost/{} (HTTP $response)"; fi'
