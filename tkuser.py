import datetime
class Tkuser:
    def __init__(self,usr,service,deta_man):
        #self.deta_man = Deta(deta_token)
        self.user = str(usr)+"_"+str(service)
        self.dt_user_db = deta_man
        print(f"using service: {self.user}")

        try:
            self.user_params = self.dt_user_db.get(self.user)
        except ValueError:
            self.user_params = None
            self.ucmd = None
            self.tk_id = None
            print("key error")
        else:
            if self.user_params == None:
                self.ucmd = None
                self.tk_id = None
            else:
                self.ucmd = self.user_params["user_cmd"]
                self.tk_id = self.user_params["token_id"]
        print(self.user_params)

    def getCmd(self):
        #if self.user_params == None:
        #    return None
        #else:
        #    ucmd = self.user_params
        print(f"user commad: {self.ucmd}")
        return self.ucmd

    def getTokenID(self):
        print(f"user token: {self.tk_id}")
        return self.tk_id

    def addUser(self,token_dic,usr_cmd):
        ts_epoch = (token_dic.getCreatedTS()/1000)
        exp_epoch = (token_dic.getExpiryTS()/1000)
        dt_exp = datetime.datetime.fromtimestamp(exp_epoch)
        ct_exp = datetime.datetime.fromtimestamp(ts_epoch)
        print(f"\n\ncreated on: {ct_exp} with epoch: {ts_epoch}")
        print(f"\n\nto expiry on: {dt_exp} with epoch: {exp_epoch}")
        self.dt_user_db.put({"token_id":token_dic.getId(),"user_cmd":usr_cmd},self.user,expire_at=dt_exp)
        print('adding user')
        #self.dt_user_db.put({"token_id":""})