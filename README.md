# SuperView
### 
In this project we aim to give the user a personal viewing experience of the places where human intervention is not feasible or of the places that are comparatively difficult to reach by humans.
It consists of 2 modules:

1. VR
2. OCYV (On Command Youtube View)

APIs mainly used for collecting youtube comments

https://www.googleapis.com/youtube/v3/liveBroadcasts/?part=snippet&broadcastStatus=active&broadcastType=persistent

https://www.googleapis.com/youtube/v3/liveChat/messages?liveChatId=EiEKGFVDMExWM0xVSk9YYlozSEF3T3I2SG9sQRIFL2xpdmU&part=snippet

APIs data is processed and the relevant data is made live to cloud from where servo motors take in the input 
and rotate the motor as per user's will.
