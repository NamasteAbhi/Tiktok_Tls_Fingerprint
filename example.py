#pip install curl_cffi

from curl_cffi import requests
import warnings
warnings.filterwarnings("ignore")
ja3 = ",".join(
    [
        "771",
        "4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53",
        "0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513-21",
        "29-23-24",
        "0",
    ]
)
akamai = "1:65536;2:0;3:1000;4:6291456;6:262144|15663105|0|m,a,s,p"
extra_fp = {
    "tls_signature_algorithms": [
        "ecdsa_secp256r1_sha256",
        "rsa_pss_rsae_sha256",
        "rsa_pkcs1_sha256",
        "ecdsa_secp384r1_sha384",
        "rsa_pss_rsae_sha384",
        "rsa_pkcs1_sha384",
        "rsa_pss_rsae_sha512",
        "rsa_pkcs1_sha512"
    ]
}
r = requests.Session()
r.ja3=ja3
r.akamai=akamai
r.extra_fp=extra_fp
headers= {
    'user-agent': 'com.zhiliaoapp.musically/2023904000 (Linux; U; Android 13; en_GB; M2103K19I; Build/TP1A.220624.014; Cronet/TTNetVersion:26c4b559 2025-03-06 QuicVersion:55af8b7a 2024-11-18)',
}
r3 = r.get("https://tls.browserleaks.com/json",headers=headers)
print(r3.text)
