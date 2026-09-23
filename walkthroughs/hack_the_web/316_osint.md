# URL
https://hack.arrrg.de/challenge/316
# Category
OSINT
# Concept
* reverse image search
# Method of solve
* we're given a picture with a bridge and a river, and we're asked to answer which river is depicted in the picture
* when we submit the picture to Google reverse image search, we see an [article](https://wanderlustig2019.wordpress.com/2025/02/14/street-art-in-rosenheim-bayern/) that features the same graffiti under the bridge
  * that article says that the street art was from Bayern (Bavaria) Rosenheim
  * if we take one of the photos from that article featuring the bridge, and ask Google (Gemini):
    * it will identify the river as the Mangfall river
    * also, if we search for rivers in Rosenheim, there are only two, the Inn, and the Mangfall

