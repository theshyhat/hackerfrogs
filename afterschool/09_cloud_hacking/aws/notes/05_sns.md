# SNS Operations
SNS is a subscription / publishing-based message service
## SNS Enumeration
```
aws sns list-topics
```
## Subscribe to a topic
```
aws sns subscribe --topic-arn <ARN> --protocol email --notification-endpoint
```
* we need to confirm the subscription from our email
* after confirmation, wait up to 5 minutes to receive another message
* this method may leak API keys or other secrets
* don't forget to unsubscribe when you're done
