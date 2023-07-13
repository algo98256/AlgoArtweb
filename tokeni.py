import jwt,json
import datetime
from jwt.exceptions import InvalidTokenError
class AToken:
    def __init__(self,token_str,secret_key):
        self.token_data = self.decode_token(token_str,secret_key)
        if self.token_data == None:
            self.token_id = None
            self.token_stamp = None
            self.token_exp = None
        else:
            self.token_id = self.token_data["encodedValue"]
            self.token_stamp = self.token_data["timestamp"]
            self.token_exp = self.token_data["extimestamp"]
            #self.token_stamp + (24 * 60 * 60 * 1000)
            print(self.token_data)


    def getId(self):
        print(f"token id: {self.token_id}")
        return self.token_id

    def getCreatedTS(self):
        print(f"created on: {self.token_stamp}")
        return self.token_stamp

    def getExpiryTS(self):
        print(f"will expire on: {self.token_exp}")
        return self.token_exp

    def is_token_expired(self,token, secret_key):
        try:
            decoded_token = jwt.decode(token, secret_key,algorithms=["HS256"])
            exp_timestamp = decoded_token.get('extimestamp')
            current_timestamp = datetime.datetime.utcnow().timestamp()
            return True
        except InvalidTokenError:
            print("token error")
        # Handle invalid token
            return True

    def decode_token(self,token, secret_key):
        is_expired = self.is_token_expired(token,secret_key)

        if is_expired == False:
            print("token expired")
            #return None
        else:
            try:
                payload = jwt.decode(token, secret_key, algorithms=["HS256"])
                return payload
            except InvalidTokenError as e:
                print(f"error: {e}")
        # Handle invalid token
                return None


#secretKey = "iwasbornandraisedbutcutfromadifferentcloth,lifewasn'tfunnywhenbeingcalledbrokewasajoke"
#tkn_str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbmNvZGVkVmFsdWUiOiJabXg1TnpKdmNtUnBaVEkzTlRFMk9EYzNNREF3TWpNME9UWT0iLCJ0aW1lc3RhbXAiOjE2ODc3MDAwMjM0OTYsImV4dGltZXN0YW1wIjoxNjg3Nzg2NDIzNDk2LCJpYXQiOjE2ODc3MDAwMjN9.o23aDbDxHFuJ5NVI2syx0PiYgX3iHXJilKzCU7zB3FQ"
#tkn = AToken(tkn_str,secretKey)