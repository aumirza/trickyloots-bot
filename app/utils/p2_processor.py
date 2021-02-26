from config import p2_config
import re

class processor:
    
    def __init__ (message):
        self.message = message

    def process():

        message = self.message

        if p2_blockwords.match_text in message:

            msg_list = []

            for line in message.splitlines():
            
                if re.match("—————",line, re.IGNORECASE):
                    break
                else:
                    if any(re.match(blockword,line, re.IGNORECASE) for blockword in p2_config.blockwords):		
                        for blockword in p2_blockwords:	
                            line = re.sub(blockword,"",line)
                            msg_list.append(line)
                    else:
                        msg_list.append(line)
                            
            message = "\n".join(msg_list)	
            return message

        else:
            return None