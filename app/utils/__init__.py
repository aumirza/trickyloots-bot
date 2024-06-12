# Importing Modules
import re
import requests
from json import dumps
from urllib.parse import (quote, urlencode, unquote,
                          urlparse, parse_qsl, ParseResult)

from config import p1_config


def flipkart_url_shortner(long_url):
    payload = {"url": long_url}
    resp = requests.get(p1_config.flipkart_shortner_api, params=payload)
    return resp.json()["response"]["shortened_url"]


def amazon_url_shortner(long_url):

    long_url = quote(long_url, safe='')
    reqUrl = f'{p1_config.amazon_shortner_api }?longUrl={long_url}&marketplaceId={p1_config.amazon_marketplace_id}'

    headersList = {
        "Cookie": "x-acbin= OqHJgLfKkFlIeyCx66lbRN6rxFJG4ivUhm@gFQW0jLBWsYDDxrjUj6bUo1gLK1@V;"
    }
    # payload = {
    #     "longUrl": long_url,
    #     "marketplaceId": p1_config.amazon_marketplace_id
    # }
    # resp = requests.get(p1_config.amazon_shortner_api, params=payload)

    resp = requests.request("GET", reqUrl, headers=headersList)
    return resp.json()["shortUrl"]


def urls_list_from_string(string):
    '''This function returns a list of URLs from message.'''
    regex = r"(?:http|ftp|https):\/\/(?:[\w\-_]+(?:\.[\w\-_]+))(?:[\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?"
    urls_list = re.findall(regex, string)
    return urls_list


def domains_list_from_string(string):
    '''This function returns a list of sub/domain from message.'''
    regex = r'(?:http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))(?:[\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?'
    domains_list = re.findall(regex, string)
    return domains_list


def add_url_params(url, params):
    ''' This function adds parameters in an url, if already exits its replaces with new value.'''
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
