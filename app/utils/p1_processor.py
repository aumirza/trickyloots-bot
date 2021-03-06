# Importing Modules

import re
from config import p1_config , az_aff ,f_aff
import requests
from bs4 import BeautifulSoup as bs
from json import dumps
from urllib.parse import (urlencode, unquote, urlparse, parse_qsl, ParseResult)

class processor:

    def __init__ (self,message):
        self.message = message

    def process(self):
        '''Main function'''
        self.pre_process()

        if self.message == "":
            return self.message

        urls_list = self.urls_list_from_string(self.message)

        if len(urls_list) == 0:
            return self.message
        else:
            self.converter()
            return self.message

    def pre_process(self):
        '''Removes Watermarks from message.'''	
        if any( re.search(blockmessage, self.message, re.IGNORECASE) for blockmessage in p1_config.blockmessages):
            self.message = ""
            return 
        else:
            msg_list = []	
            for line in self.message.splitlines():	
                if any( re.search(blockline,line, re.IGNORECASE) for blockline in p1_config.blocklines):
                    pass
                else:
                    if any(re.search(blockword,line, re.IGNORECASE) for blockword in p1_config.blockwords):		
                        for blockword in p1_config.blockwords:
                            blockword = "(?i)"+blockword	
                            line = re.sub(blockword,"",line)
                        if line != "":
                            msg_list.append(line)	
                    else:
                        msg_list.append(line)		
                            
            self.message = "\n".join(msg_list)


    def converter(self):
        domains_list = self.domains_list_from_string(self.message)
        urls_list = self.urls_list_from_string(self.message)

        new_url_list = []

        for i, domain in enumerate(domains_list): #make affilate urls
            new_url = self.in_loop_converter(domain,urls_list[i])
            new_url_list.append(new_url)

        for i in range(len(urls_list)):  # Replaces url with affilate url in message.
            self.message = self.message.replace(urls_list[i], new_url_list[i])


    def in_loop_converter(self,domain,url):

        if domain in p1_config.shorturl_domains:
            return self.shorturl_converter(url)

        elif domain in p1_config.flipkart_domains:
            return self.flipkart_converter(domain, url)

        elif domain in p1_config.amazon_domains:
            return self.amazon_converter(domain, url)
        
        elif domain in p1_config.ek_domains:
            return self.ek_converter(url)

        else:
            return url

    def flipkart_converter(self,domain,url):
        if domain != p1_config.flipkart_domains[0]:
            raw_url = re.sub("([a-z0-9|-]+\.)*flipkart+\.[a-z]+", p1_config.flipkart_domains[0]+"/dl", url)
        long_url = self.add_url_params(raw_url, f_aff)
        new_url = self.flipkart_url_shortner(long_url)
        return new_url

    @staticmethod
    def flipkart_url_shortner(long_url):
        payload = { "url": long_url }
        resp = requests.get(p1_config.flipkart_shortner_api,params=payload)
        return resp.json()["response"]["shortened_url"]

    def amazon_converter(self,domain,url):
        if domain != p1_config.amazon_domains[0]:
            raw_url = re.sub("([a-z0-9|-]+\.)*amazon+\.[a-z]+",p1_config.amazon_domains[0],url)
        long_url = self.add_url_params(raw_url, az_aff)
        new_url = self.amazon_url_shortner(long_url)
        return new_url

    @staticmethod
    def amazon_url_shortner(long_url):
        payload = {
            "longUrl": long_url,
            "marketplaceId": p1_config.amazon_marketplace_id
        }
        resp = requests.get(p1_config.amazon_shortner_api,params=payload,cookies=p1_config.amazon_cookies)
        return resp.json()["shortUrl"]


    def shorturl_converter(self,url):
        raw_url = requests.get(url)
        domains_list = self.domains_list_from_string(raw_url.url)
        domain = "\n".join(domains_list)
        new_url = self.in_loop_converter(domain, raw_url.url)
        return new_url

    @staticmethod
    def ek_converter(url):
        payload = {'message': url}
        r = requests.post(p1_config.ek_api, data=payload, headers=p1_config.ek_headers,cookies=p1_config.ek_cookies)
        return r.text

    @staticmethod
    def urls_list_from_string(string):
        '''This function returns a list of URLs from message.'''
        regex = r"(?:http|ftp|https):\/\/(?:[\w\-_]+(?:\.[\w\-_]+))(?:[\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?"
        urls_list = re.findall(regex, string)
        return urls_list

    @staticmethod
    def domains_list_from_string(string):
        '''This function returns a list of sub/domain from message.'''
        regex = r'(?:http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))(?:[\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?'
        domains_list = re.findall(regex, string)
        return domains_list

    @staticmethod
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