# Importing Modules

import re
from config import p1_config
import requests
from bs4 import BeautifulSoup as bs
from json import dumps
from urllib.parse import (urlencode, unquote, urlparse, parse_qsl, ParseResult)

class processor:

    def __init__ (message):
        self.message = message

    def process():
        '''Main function'''
        message = self.message
        message = pre_process(message)
        if message == None:
            return ""
        urldl = find_urldl(message)
        if len(urldl) == 0:
            return message
        else:
            return converter(message)


    def pre_process(message):	
        '''Removes Watermarks from message.'''	
        if any( re.match(blockmessage, message, re.IGNORECASE) for blockmessage in p1_config.blockmessages):	
            return None	
        else:
            msg_list = []	
            for line in message.splitlines():	
                if any( re.match(blockline,line, re.IGNORECASE) for blockline in p1_config.blocklines):	
                    pass
                else:
                    if any(re.match(blockword,line, re.IGNORECASE) for blockword in p1_config.blockwords):		
                        for blockword in p1_config.blockwords:	
                            if re.match(blockword,line, re.IGNORECASE):	
                                line = re.sub(blockword,"",line)	
                        msg_list.append(line)	
                    else:
                        msg_list.append(line)		
                            
            message = "\n".join(msg_list)	
            return message


    def find_url(string):
        '''This function returns a list of URLs from message.'''
        regex = r"(?:http|ftp|https):\/\/(?:[\w\-_]+(?:\.[\w\-_]+))(?:[\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?"
        url = re.findall(regex, string)
        return url


    def find_urldl(string):
        '''This function returns a list of sub/domain from message.'''
        regex = r'(?:http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))(?:[\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?'
        url = re.findall(regex, string)
        return url


    def converter(message):
        urldl = find_urldl(message)
        urll = find_url(message)

        nurll = []

        for i, urld in enumerate(urldl):
            nurll.append(in_conveter(urld, urll[i]))

        for i in range(len(urll)):  # Replaces url with affilate url in message.
            message = message.replace(urll[i], nurll[i])

        return message


    def in_conveter(domain, url):
        ''' Domain for matching 
            And the url to be converted '''

        if domain in p1_config.flipkart_domain:
            if domain == p1_config.flipkart_domain[0]:  # if url is of type dl.flipkart.com
                nurl = add_url_params(url, f_aff)

            elif domain == p1_config.flipkart_domain[1]:  # if url is of type fkrt.it
                nurl_r = requests.get(url)
                nurl = re.sub(p1_config.flipkart_domain[2], p1_config.flipkart_domain[0]+"/dl", nurl_r.url)
                nurl = add_url_params(nurl, f_aff)

            elif domain == p1_config.flipkart_domain[2]:  # if url is of type www.flipkart.com.
                nurl = re.sub(p1_config.flipkart_domain[2], p1_config.flipkart_domain[0]+"/dl", url)
                nurl = add_url_params(nurl, f_aff)

        elif domain in amazon:
            if domain == amazon[0]:  # if url is of type www.amazon.in
                nurl = add_url_params(url, az_aff)

            elif domain == amazon[1]:  # if url is of type amzn.to
                nurl_r = requests.get(url)
                nurl = add_url_params(nurl_r.url, az_aff)

        elif domain in eklist:
            nurl = ek_converter(url)

        elif domain in shorturl:
            nurl_r = requests.get(url)
            a = find_urldl(nurl_r.url)
            a = "\n".join(a)
            b = nurl_r.url
            nurl = in_conveter(a, b)

        else:
            nurl = url

        return nurl


    def ek_converter(url):
        payload = {'message': url}
        r = requests.post(post_url, data=payload, headers=headers)
        return r.text


    def add_url_params(url, params):

        url = unquote(url)
        parsed_url = urlparse(url)
        get_args = parsed_url.query
        parsed_get_args = dict(parse_qsl(get_args))
        parsed_get_args.update(params)

        parsed_get_args.update(
            {k: dumps(v) for k, v in parsed_get_args.items()
            if isinstance(v, (bool, dict))}
        )

        encoded_get_args = urlencode(parsed_get_args, doseq=True)
        new_url = ParseResult(
            parsed_url.scheme, parsed_url.netloc, parsed_url.path,
            parsed_url.params, encoded_get_args, parsed_url.fragment
        ).geturl()

        return new_url