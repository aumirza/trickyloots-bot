from config import p2_config
import re

class processor:
    
    def __init__ (self,message):
        self.message = message
    
    def process(self):

        message = self.message

        if p2_config.fqg_text in message:

            msg_list = []

            for line in message.splitlines():
            
                if re.match("—————",line):
                    break
                else:
                    if any( re.search( blockword ,line, re.IGNORECASE ) for blockword in p2_config.blockwords):
                        for blockword in p2_config.blockwords:
                            blockword = "(?i)"+blockword
                            line = re.sub(blockword,"",line)
                        if line != "":
                            msg_list.append(line)
                    else:
                        msg_list.append(line)
                            
            message = "\n".join(msg_list)	
            return message

        else:
            return None