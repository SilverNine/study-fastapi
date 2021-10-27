import re
import requests
import lzstring
import uuid
import rsa

def encrypt(naver_id, naver_pw):
    key_str = requests.get('https://nid.naver.com/login/ext/keys.nhn').content.decode("utf-8")
    sessionkey , Keyname, evalue, nvalue = key_str.split(',')
    evalue, nvalue = int(evalue, 16), int(nvalue, 16)
    pubkey = rsa.PublicKey(evalue, nvalue)
    message = [sessionkey,naver_id,naver_pw]
    merge_message = ""
    for s in message:
        merge_message = merge_message + ''.join([chr(len(s)) + s])
    merge_message = merge_message.encode( )
    encpw = rsa.encrypt(merge_message, pubkey) .hex()
    return Keyname, encpw
    
def naver_login(nid, npw):
    encnm, encpw = encrypt(nid, npw)
    bvsd_uuid = uuid.uuid4()
    o = '{"a":"' + str(bvsd_uuid) + '","b":"1.3.4","h":"1f","i":{"a":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Whale/2.7.100.20 Safari/537.36"}}'
    encData = lzstring.LZString.compressToEncodedURIComponent(o)
    bvsd = '{"uuid":"'+ str(bvsd_uuid) + '","encData":"'+ encData +'"}'
    session = requests.Session()
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Whale/2.7.100.20 Safari/537.36'}
    data = {
        'enctp': '1',
        'svctype': '0',
        'encnm': encnm,
        'locale': 'ko_KR',
        'url': '‘www.naver.com',
        'smart_level': '1',
        'encpw': encpw,
        'bvsd': bvsd
    }
    resp = session.post('https://nid.naver.com/nidlogin.login', data=data, headers=headers)
    if(resp.text.find("location")>-1):
        print("로그인 성공")
        print(resp.text)
        login_url = resp.text.split('("')[1].split('"')[0]
        session.get(login_url)
    else:
        print("로그인 실패")

if __name__ == "__main__":
    naver_login('ID', 'PASSWORD')
