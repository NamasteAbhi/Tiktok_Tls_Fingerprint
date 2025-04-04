# Note

When You Use This Js Script For Hook Tls Fingerprint You Need To Clear Your App Data Before Start

# TikTok TLS Fingerprint Hook

This repository contains a Frida script designed for hooking the TLS fingerprint of TikTok version 39.4.0. The script allows for the monitoring and manipulation of TLS traffic for educational and security research purposes.

## Supported Version

- **TikTok APK Version**: 39.4.0

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Frida**: This tool must be installed on your system. Frida is a dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers. [Learn more about installing Frida here](https://frida.re/docs/installation/).
- **TikTok APK**: Download the TikTok version 39.4.0 from APKMirror: [Download TikTok 39.4.0](https://www.apkmirror.com/apk/tiktok-pte-ltd/tik-tok-including-musical-ly/tiktok-39-4-0-release/tiktok-39-4-0-android-apk-download/).

## Tls FingerPrint Of Tiktok

```
{
  "user_agent":"com.zhiliaoapp.musically/2023904000 (Linux; U; Android 13; en_GB; M2103K19I; Build/TP1A.220624.014; Cronet/TTNetVersion:26c4b559 2025-03-06 QuicVersion:55af8b7a 2024-11-18)",
  "ja3_hash": "cd08e31494f9531f560d64c695473da9",
  "ja3_text": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513-21,29-23-24,0",
  "ja3n_hash": "aa56c057ad164ec4fdcb7a5a283be9fc",
  "ja3n_text": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-5-10-11-13-16-18-21-23-27-35-43-45-51-17513-65281,29-23-24,0",
  "akamai_hash": "a345a694846ad9f6c97bcc3c75adbe26",
  "akamai_text": "1:65536;2:0;3:1000;4:6291456;6:262144|15663105|0|m,a,s,p"
}
```

## Websites For Test Tls Fingerprint

- **BrowserLeaks TLS Test**: Returns detailed information about your TLS connection.
  - URL: [https://tls.browserleaks.com/json]
  - URL2: [https://tls.peet.ws/api/all]
 
# Disclaimer
This project is provided only for educational purposes. It should not be used for illegal activities or to compromise any systems. The author assumes no responsibility for any misuse of this code.
