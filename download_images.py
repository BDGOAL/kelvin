#!/usr/bin/env python3
"""Fetch Commons-licensed photos for local static hosting. Python standard library only.
Run: python3 download_images.py
"""
import json,urllib.request,urllib.parse, pathlib, time, sys
BASE=pathlib.Path(__file__).resolve().parent
manifest=json.loads((BASE/'photo_manifest.json').read_text(encoding='utf-8'))
folder=BASE/'images'; folder.mkdir(exist_ok=True)
headers={'User-Agent':'JapanTravelPersonalWebsite/1.0 (Wikimedia Commons image attribution downloader; https://commons.wikimedia.org/)', 'Accept':'application/json'}
ok=0
for key,meta in manifest.items():
    dest=folder/(key+'.jpg')
    if dest.is_file() and dest.stat().st_size>3000:
        print('Already exists:',dest.name);ok+=1;continue
    name=meta['file']
    url='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','format':'json','prop':'imageinfo','iiprop':'url','iiurlwidth':960,'titles':'File:'+name})
    try:
        req=urllib.request.Request(url,headers=headers)
        with urllib.request.urlopen(req,timeout=35) as res:
            data=json.load(res)
        pages=data['query']['pages']
        page=next(iter(pages.values()))
        src=page['imageinfo'][0].get('thumburl') or page['imageinfo'][0]['url']
        req=urllib.request.Request(src,headers={'User-Agent':headers['User-Agent']})
        with urllib.request.urlopen(req,timeout=45) as res:
            blob=res.read(12_000_000)
        if not blob.startswith(b'\xff\xd8\xff'):
            raise ValueError('The downloaded bytes are not a JPEG')
        dest.write_bytes(blob)
        print('OK',dest.name,len(blob),'bytes');ok+=1
    except Exception as exc:
        print('FAILED',key,':',exc,file=sys.stderr)
    time.sleep(0.35)
print(f'\nDownloaded/available {ok}/{len(manifest)} photographs.')
if ok!=len(manifest):
    sys.exit(1)
