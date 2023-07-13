class Tkman:
    def __init__(self,tk_id,deta_man):
        try:
            self.xtk_id = tk_id
            self.deta_ctrl = deta_man
            self.tk_data = self.deta_ctrl.get(tk_id)
            print(self.tk_data)
        except ValueError:
            print("token error")
            self.tk_data = None
            self.tk_stat = None
        else:
            if self.tk_data == None:
                self.tk_stat = None
            else:
                self.tk_stat = self.tk_data["tkstatus"]
        print(self.tk_data)
    
    def isValid(self):
        if self.tk_stat == True:
            return False
        if self.tk_stat == False:
            return True
        if self.tk_stat == None:
            return None

    def validate(self):
        if self.tk_data == None:
            return False
        else:
            self.deta_ctrl.update({"tkstatus":True},self.xtk_id)
            return True
