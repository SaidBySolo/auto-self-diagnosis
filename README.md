# auto-self-diagnosis

[![GitHub license](https://img.shields.io/github/license/SaidBySolo/auto-self-diagnosis)](https://github.com/SaidBySolo/auto-self-diagnosis/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/SaidBySolo/auto-self-diagnosis)](https://github.com/SaidBySolo/auto-self-diagnosis/stargazers)
![GitHub All Releases](https://img.shields.io/github/downloads/SaidBySolo/auto-self-diagnosis/total)
> 일어나서 자가진단하기 매우엿같아요

![이미지](https://i.imgur.com/76zCDVn.gif)  

## 일반 사용자

### 소스코드관련

현재 ChromeWebdriver로 잡아두었는데
헤드리스 브라우저를 사용하셔도 큰문제는 없을거같습니다.

### 파일관련

백신에서 안전하지 않다고 잡는데 웹드라이버넣고 그대로 빌드시키고 릴리즈했습니다.  
걱정마시고 사용하시면됩니다.  
[릴리즈 1.0 바이러스 토탈](https://www.virustotal.com/gui/file/055adf001392e2a8b66a7c3ed6c19393138d00e2522a8b9fb481b68428e6fffe/detection)  

Malicious가 있는데 그냥 알려지지않은 파일이라 잡는거같네요

### 의존성

Chrome 85 버전을 필요로합니다.

### 사용방법

1. [링크](https://github.com/SaidBySolo/auto-self-diagnosis/releases/tag/4.0.0)에서 auto-self-diagnosis파일을 다운로드하고 압축을 풉니다.

2. info.json을 메모장으로 엽니다.

3. 학교이름 및 모든 사항을 맞게 수정해주세요

4. 수정한것을 **UTF-8**로 저장합니다. 일반적으로 저장하시면 UTF-8로 저장이 될것입니다.

5. 프로그램을 실행해주세요

## 개발자용

개발환경은 Windows입니다.

### 의존성

* CPython 3.8+

* requirements.txt 참고

* chrome버전과 맞는 chromedriver

### 실행방법

```sh
git clone https://github.com/SaidBySolo/auto-self-diagnosis.git

cd auto-self-diagnosis

python script.py
```

### exe 빌드

```sh
./make_exe.bat
```

## 기타

### 문제발생

[이슈](https://github.com/SaidBySolo/auto-self-diagnosis/issues)또는 Pull Request넣어주세요

### 면책조항

이 프로그램 및 소스코드를 사용하는 불이익은 사용자 본인에게있습니다.  
저작권자와 기여자는 이 소스코드를 '있는 그대로' 제공하며 어떠한 보증도 하지않습니다.

### 라이센스

이 소스코드는 [MIT LICENSE](LICENSE)를 따릅니다.

chromedriver는 [BSD 3-Clause](LICENSE.chromedriver)에 따라 배포됩니다.
