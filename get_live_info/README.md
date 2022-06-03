## 配信チャットの情報を取得するための順序 <br>

### 1.配信しているURLから動画IDを取得する <br>
配信のURLは<br>
#### https://www.youtube.com/watch?v=XXXXXXX <br>
のように、動画と同じ形式をとっている。動画IDは「?v=XXXXXXX」の部分となる。<br>
これを<br>
#### https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=XXXXXXX&key=APIキー <br>
のAPIにリクエストを送信して、レスポンスを得ることで配信IDを得ることができる。<br>
レスポンス形式はJSONで<br>

```
{
  "kind": "youtube#videoListResponse",
  "etag": "******",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "******",
      "id": "******",
      "liveStreamingDetails": {
        "actualStartTime": "2021-11-30T08:04:55Z",
        "scheduledStartTime": "2021-11-30T08:00:00Z",
        "concurrentViewers": "968",
        "activeLiveChatId": "YYYYYYYYYY"
      }
    }
  ],
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  }
}
```

のようになる。<br>
配信IDは「items.liveStreamingDetails.activeLiveChatId」プロパティより。<br>

### 2.得られた配信IDからチャット情報APIにリクエストを送信する <br>
チャット情報APIは<br>
#### https://www.googleapis.com/youtube/v3/liveChat/messages?key=APIキー&part=snippet,authorDetails&liveChatId=配信ID&pageToken= <br>
へリクエストを送信して、得られたレスポンスから取得する。<br>
レスポンス形式はJSONで<br>

```
{
  "kind": "youtube#liveChatMessageListResponse",
  "etag": "************",
  "pollingIntervalMillis": 4868,
  "pageInfo": {
    "totalResults": 75,
    "resultsPerPage": 75
  },
  "nextPageToken": "******",
  "items": [
    {
      "kind": "youtube#liveChatMessage",
      "etag": "******",
      "id": "******",
      "snippet": {
        "type": "textMessageEvent",
        "liveChatId": "*****",
        "authorChannelId": "*****",
        "publishedAt": "2022-06-03T13:23:22.764696+00:00",
        "hasDisplayContent": true,
        "displayMessage": "******",
        "textMessageDetails": {
          "messageText": "******"
        }
      },
    },
      "authorDetails": {
        "channelId": "*****",
        "channelUrl": "http://www.youtube.com/channel/******",
        "displayName": "clgildner",
        "profileImageUrl": "https://yt3.ggpht.com/ytc/AKedOLSf1nEn3Sev3kPqcBqMSdFn1fE7Hp1wysJoUFMr=s88-c-k-c0x00ffffff-no-rj",
        "isVerified": false,
        "isChatOwner": false,
        "isChatSponsor": false,
        "isChatModerator": true
      }
    },
```
<b>pageToken</b>のクエリパラメータを空欄にすることで、全件取得になる。<br>
<b>nextpageToken</b>の値を<b>pageToken</b>に与えることで、更新分のチャットを取得できる。<br>
<b>nextpageToken</b>の値を代入し続けて、0になった時に更新分のチャットが無くなったということになる。<br>
⇒<u>チャットの瞬間風速を知るには、<b>nextpageToken</b>のレスポンス内容の「item」のリストのCountを目安にできる。</u><br>

### ※Youtube公式APIの使用について
```
TBD
```