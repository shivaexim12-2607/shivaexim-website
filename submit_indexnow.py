"""Notify IndexNow after successful publication; receipt does not mean indexing."""
import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent
BASE = 'https://shivaexim.com'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--all', action='store_true', help='Initial submission of current sitemap URLs')
    parser.add_argument('urls', nargs='*', help='Only published added, changed or deleted URLs')
    args = parser.parse_args()
    if args.all and args.urls:
        parser.error('Use --all or individual URLs')
    urls = args.urls
    if args.all:
        tree = ElementTree.parse(ROOT/'dist/sitemap.xml')
        urls = [node.text for node in tree.findall('.//{*}loc')]
    urls = list(dict.fromkeys(urls))
    if not urls or len(urls) > 10000:
        parser.error('Provide between 1 and 10000 URLs')
    if any(urlsplit(url).scheme != 'https' or urlsplit(url).netloc != 'shivaexim.com' for url in urls):
        parser.error('Only canonical HTTPS shivaexim.com URLs are allowed')
    key = (ROOT/'indexnow-key.txt').read_text().strip()
    location = f'{BASE}/{key}.txt'
    with urlopen(location, timeout=30) as response:
        if response.status != 200 or response.read().decode('utf-8').strip() != key:
            raise RuntimeError('Published key file could not be verified')
    payload = dict(host='shivaexim.com', key=key, keyLocation=location, urlList=urls)
    request = Request('https://api.indexnow.org/indexnow', data=json.dumps(payload).encode(), headers={'Content-Type':'application/json; charset=utf-8'}, method='POST')
    with urlopen(request, timeout=30) as response:
        if response.status not in (200, 202):
            raise RuntimeError(f'Unexpected status: {response.status}')
        print(f'IndexNow HTTP {response.status}: {len(urls)} URLs received; indexing is not guaranteed.')

if __name__ == '__main__':
    main()
