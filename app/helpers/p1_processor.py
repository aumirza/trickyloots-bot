import re
import requests
from config import p1_config, az_aff, f_aff
from utils import add_url_params, amazon_url_shortner, domains_list_from_string, flipkart_url_shortner, urls_list_from_string
import urllib.parse

class processor:

    def __init__(self, message):
        self.message = message

    def process(self):
        '''Main function'''

        self.pre_process()

        if not self.message:
            return self.message

        urls_list = urls_list_from_string(self.message)

        if len(urls_list) == 0:
            return self.message
        else:
            self.converter()
            return self.message

    def pre_process(self):
        '''Removes Watermarks from message.'''
        if any(re.search(blockmessage, self.message, re.IGNORECASE) for blockmessage in p1_config.blockmessages):
            self.message = ""
        else:
            msg_list = []
            for line in self.message.splitlines():
                if any(re.search(blockline, line, re.IGNORECASE) for blockline in p1_config.blocklines):
                    pass
                else:
                    if any(re.search(blockword, line, re.IGNORECASE) for blockword in p1_config.blockwords):
                        for blockword in p1_config.blockwords:
                            blockword = "(?i)"+blockword
                            line = re.sub(blockword, "", line)
                        if line != "":
                            msg_list.append(line)
                    else:
                        msg_list.append(line)

            self.message = "\n".join(msg_list)

    def converter(self):
        domains_list = domains_list_from_string(self.message)
        urls_list = urls_list_from_string(self.message)

        new_url_list = []

        for i, domain in enumerate(domains_list):  # make affiliate urls
            new_url = self.in_loop_converter(domain, urls_list[i])
            new_url_list.append(new_url)

        # Replaces url with affiliate url in message.
        for i in range(len(urls_list)):
            self.message = self.message.replace(urls_list[i], new_url_list[i])

    def in_loop_converter(self, domain, url):

        if domain in p1_config.shorturl_domains:
            return self.shorturl_converter(url)

        elif domain in p1_config.flipkart_domains:
            return self.flipkart_converter(domain, url)

        elif domain in p1_config.amazon_domains:
            return self.amazon_converter(domain, url)

        elif domain in p1_config.ek_domains:
            return self.ek_converter(url)
        
        elif domain in p1_config.extrape_domains:
            return self.extrape_converter(url)

        else:
            return url

    def flipkart_converter(self, domain, url):
        if domain != p1_config.flipkart_domains[0]:
            url = re.sub("([a-z0-9|-]+\.)*flipkart+\.[a-z]+",
                         p1_config.flipkart_domains[0]+"/dl", url)
        long_url = add_url_params(url, f_aff)
        new_url = flipkart_url_shortner(long_url)
        return new_url

    def ek_converter(self, url):
        payload = {"deal": url,"convert_option": "convert_only"}
        r = requests.post(
            p1_config.ek_api,
            json=payload,
            headers=p1_config.ek_headers
        )
        if r.status_code == 200:
            response_data = r.json()
            return response_data.get("data")
    
    def extrape_converter(self, url):
        payload = {"inputText": url}
        r = requests.post(
            p1_config.extrape_api,
            json=payload,
            headers=p1_config.extrape_headers
        )
        if r.status_code == 200:
            response_data = r.json()
            encoded_text = response_data.get("convertedText")
            if encoded_text:
                return urllib.parse.unquote(encoded_text)

    def amazon_converter(self, domain, url):
        if domain != p1_config.amazon_domains[0]:
            url = re.sub("([a-z0-9|-]+\.)*amazon+\.[a-z]+",
                         p1_config.amazon_domains[0], url)
        long_url = add_url_params(url, az_aff)
        new_url = amazon_url_shortner(long_url)
        return new_url

    def shorturl_converter(self, url):
        raw_url = requests.get(url)
        domains_list = domains_list_from_string(raw_url.url)
        domain = "\n".join(domains_list)
        new_url = self.in_loop_converter(domain, raw_url.url)
        return new_url
