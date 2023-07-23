import base64
import json

lines = """
{"type": "http.response.start", "status": 200, "headers": [[{"$base64": "ZGF0ZQ=="}, {"$base64": "U3VuLCAyMyBKdWwgMjAyMyAxOToyMzoxNiBHTVQ="}], [{"$base64": "Y29udGVudC10eXBl"}, {"$base64": "dGV4dC9ldmVudC1zdHJlYW0="}], [{"$base64": "dHJhbnNmZXItZW5jb2Rpbmc="}, {"$base64": "Y2h1bmtlZA=="}], [{"$base64": "Y29ubmVjdGlvbg=="}, {"$base64": "a2VlcC1hbGl2ZQ=="}], [{"$base64": "YWNjZXNzLWNvbnRyb2wtYWxsb3ctb3JpZ2lu"}, {"$base64": "Kg=="}], [{"$base64": "Y2FjaGUtY29udHJvbA=="}, {"$base64": "bm8tY2FjaGUsIG11c3QtcmV2YWxpZGF0ZQ=="}], [{"$base64": "b3BlbmFpLW9yZ2FuaXphdGlvbg=="}, {"$base64": "dXNlci1yM2U2MWZwYWswNGNiYW9rcDVidW9hZTQ="}], [{"$base64": "b3BlbmFpLXByb2Nlc3NpbmctbXM="}, {"$base64": "OQ=="}], [{"$base64": "b3BlbmFpLXZlcnNpb24="}, {"$base64": "MjAyMC0xMC0wMQ=="}], [{"$base64": "c3RyaWN0LXRyYW5zcG9ydC1zZWN1cml0eQ=="}, {"$base64": "bWF4LWFnZT0xNTcyNDgwMDsgaW5jbHVkZVN1YkRvbWFpbnM="}], [{"$base64": "eC1yYXRlbGltaXQtbGltaXQtcmVxdWVzdHM="}, {"$base64": "MzUwMA=="}], [{"$base64": "eC1yYXRlbGltaXQtbGltaXQtdG9rZW5z"}, {"$base64": "OTAwMDA="}], [{"$base64": "eC1yYXRlbGltaXQtcmVtYWluaW5nLXJlcXVlc3Rz"}, {"$base64": "MzQ5OQ=="}], [{"$base64": "eC1yYXRlbGltaXQtcmVtYWluaW5nLXRva2Vucw=="}, {"$base64": "ODk5ODA="}], [{"$base64": "eC1yYXRlbGltaXQtcmVzZXQtcmVxdWVzdHM="}, {"$base64": "MTdtcw=="}], [{"$base64": "eC1yYXRlbGltaXQtcmVzZXQtdG9rZW5z"}, {"$base64": "MTJtcw=="}], [{"$base64": "eC1yZXF1ZXN0LWlk"}, {"$base64": "NDhjZmI5MDI3ZDc2ZTYyYzczOTJkNTEyZjViMzAwNTY="}], [{"$base64": "Y2YtY2FjaGUtc3RhdHVz"}, {"$base64": "RFlOQU1JQw=="}], [{"$base64": "c2VydmVy"}, {"$base64": "Y2xvdWRmbGFyZQ=="}], [{"$base64": "Y2YtcmF5"}, {"$base64": "N2ViNjRiZmIxOTBmN2NjZS1MQVg="}], [{"$base64": "YWx0LXN2Yw=="}, {"$base64": "aDM9Ijo0NDMiOyBtYT04NjQwMA=="}]]}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsicm9sZSI6ImFzc2lzdGFudCIsImNvbnRlbnQiOiIifSwiZmluaXNoX3JlYXNvbiI6bnVsbH1dfQoK"}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsiY29udGVudCI6IkhlbGxvIn0sImZpbmlzaF9yZWFzb24iOm51bGx9XX0KCg=="}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsiY29udGVudCI6IiEifSwiZmluaXNoX3JlYXNvbiI6bnVsbH1dfQoK"}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsiY29udGVudCI6IiBIb3cifSwiZmluaXNoX3JlYXNvbiI6bnVsbH1dfQoK"}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsiY29udGVudCI6IiBjYW4ifSwiZmluaXNoX3JlYXNvbiI6bnVsbH1dfQoK"}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsiY29udGVudCI6IiBJIn0sImZpbmlzaF9yZWFzb24iOm51bGx9XX0KCg=="}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsiY29udGVudCI6IiBhc3Npc3QifSwiZmluaXNoX3JlYXNvbiI6bnVsbH1dfQoK"}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsiY29udGVudCI6IiB5b3UifSwiZmluaXNoX3JlYXNvbiI6bnVsbH1dfQoK"}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsiY29udGVudCI6IiB0b2RheSJ9LCJmaW5pc2hfcmVhc29uIjpudWxsfV19Cgo="}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnsiY29udGVudCI6Ij8ifSwiZmluaXNoX3JlYXNvbiI6bnVsbH1dfQoK"}, "more_body": true}
{"type": "http.response.body", "body": {"$base64": "ZGF0YTogeyJpZCI6ImNoYXRjbXBsLTdmWXhneTZRaTJnMlltTjBPb2hDTXFjYkxibFpMIiwib2JqZWN0IjoiY2hhdC5jb21wbGV0aW9uLmNodW5rIiwiY3JlYXRlZCI6MTY5MDE0MDE5NiwibW9kZWwiOiJncHQtMy41LXR1cmJvLTA2MTMiLCJjaG9pY2VzIjpbeyJpbmRleCI6MCwiZGVsdGEiOnt9LCJmaW5pc2hfcmVhc29uIjoic3RvcCJ9XX0KCmRhdGE6IFtET05FXQoK"}, "more_body": true}
{"type": "http.response.body", "more_body": false}
""".strip().split("\n")

def as_base64(dct):
    if '$base64' in dct:
        return base64.b64decode(dct["$base64"])
    return dct

messages = []
for line in lines:
    messages.append(json.loads(line, object_hook=as_base64))

async def app(scope, receive, send):
    if scope["type"] != "http":
        return
    for message in messages:
        await send(message)
