import requests

from .Config import Config

class RequestParams(Config):

    def reply_to_tweet(self, tweetId, complain, complain_type, entities, user):
        PARAMS = {'tweetId': tweetId.strip(), "complain": complain, "complain_type": complain_type, "entities": entities,
                  "user": user.strip()}
        print(PARAMS)
        r = requests.post(url=self.URL, data=PARAMS)

        data = r.json()
        print("reply to tweeeeeeeeeeeeeet", data)
        if data['replied']:
            return str(data["ticketId"])
        else:
            return ""

# a = RequestParams()
# a.reply_to_tweet("1415389426465656832","1231", "sdafs", "aefas", "    _nihit_")