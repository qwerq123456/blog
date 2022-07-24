# png

무손실 압축을 하는 비트맵 이미지

> bitmap vs vector
bitmap : 픽셀단위로 이미지 처리

vector : 점 + 점 => 선 & 선을 모아 면 만들기

## Header
8바이트의 헤더로 시작한다. 고정인거 같은데 의미를 알아야 할까?ㅋㅋ 8비트 데이터를 지원하지 않는 전송 시스템이나 혹은 다른 텍스트 파일들이 잘못 해석될 수 있는 가능성 등을 걸러내기 위한 헤더인듯 하다. 

## Chunk 

|length|chunk type|chunk data|crc|
|---|---|---|---|
|4 byte|4 byte|{length} byte|4byte|


1. length 
    - chunk data의 길이 

2. chunk type
    - 4개의 ascii 문자로 이루어짐
    - critical, ancillary 두가지 존재
    1. 첫번째 문자
        - chunk가 critical 인지 여부 대문자이면 critical 소문자이면 ancillary
    2. 두번째 문자
        - chunk가 public인지 private인지 여부 확인
    3. 세번째 문자
        - png이려면 대문자여야함. 확장을 위해 남겨둔것. 소문자이면 다른 알 수 없는 chunk들과 동일하게 처리
    4. 네번째 문자
        - 복사 안정성 여부
        - 대문자인 경우 critical chunk를 수정하지 않았을 때만 복사가능

3. chunk data 
    - chunk type에 따른 데이터가 들어있는 부분

4. crc
    - length를 제외한 type, data의 checksum

## critical chunk
critical chunk는 파일을 읽는데에 필요한 정보를 가지는 chunk이다.
ancillary일 경우 decoder가 해석할 수 없을때 넘어갈 수 있지만, critical인 경우는 유저에게 경고를 띄우는 등의 예외처리를 해야함. 

- IHDR : Image Header 첫 번째 청크여야 한다. 아래의 순서로 13바이트 이다. (괄호 바이트 수, 화살표 뒤는 가질 수 있는 값)
    - width (4)
    - height (4)
    - bit depth (1) => 1,2,4,8,16
    - color type (1) => 0,2,3,4,6
    - compression method (1) => 0
    - filter method (1) => 1
    - interlace method (1) => 0,1

- PLTE : Color Palette : 색상 목록. IHDR에서의 color type에 따라 필요없을 수도 있다. ex) 0,4의 경우 gray scale이기 때문에 필요없다. 

- IDAT : Image Data : 여러개의 IDAT chunk로 나뉠 수 있는 이미지를 포함한다. 이렇게 쪼개는게 용량을 늘리지만, 이는 png를 streaming에서 생성할 수 있게 해준다. 압축 알고리즘의 결과값인 실제 이미지 데이터를 포함한다. 


- IEND : End of the Image 이미지 끝

## ancillary chunk
critical에 표현하지 않는 다른 이미지 데이터를 가지는 chunk이다. 위키피디아에 많은 설명이 있지만 그중에 중요해 보이는 것(무슨소리인지 알 수 있는 것)만 적으려 한다.
- bKGD : 디폴트 배경색 
- dSIG : 디지털 서명
- eXIf : Exif 메타데이터 저장 (다른건 잘 모르겠고, 이미지에 위치 정보 있는것도 여기다 저장하는것 같음)
- gAMA : gamma값 저장 (유니티 할때 gamma, linear 형식 관련 이슈가 있었는데 생각 나서 적었다)
- pHYs : 픽셀 크기, 픽셀 종횡비 
- tEXt : key-value쌍으로 텍스트를 저장할 수 있다.
- tIME : 이미지 마지막 변경 시간 저장
- tRNS : 투명도 정보
    - chunk data필드에 PLTE의 팔레트 0 ~ n까지 알파값을 넣는다. 

## 압축
PNG는 두단계의 압축 단계를 거친다.

- pre-compression : filtering (prediction)
    - DEFLATE을 적용하기 전에 prediction method로 데이터를 변환한다.(압축이 더 잘 되는 형태)
    -  이전 픽셀값을 기준으로 다음 픽셀값을 예측하고 실제값에서 그 값을 빼서 값을 저장. 차이가 적을 수록 압축이 잘된다. 
    
- compression : DEFLATE
    - 특허 없는 무손실 데이터 압축 알고리즘 DEFLATE사용. 이는 LZ777과 Huffman coding을 사용한다.


- interace
    - critical chunk 중에 IHDR에서 마지막 값에따라 선택적으로 사용한다.
    - Adam7 알고리즘 사용
    - interace를 사용하면, 압축성이 떨어지지만, 전송 초기에 저해상도 이미지를 볼 수 있다. 

## 다른 형식과의 비교

1. GIF
    - gif는 8비트(256)개의 색만 지원. png는 더 많은 색을 커버할 수 있다. (PFTE)
    - GIF는 움짤 가능

2. JPEG
    - 일반적으로 png보다 작은 용량으로 이미지 저장 가능 => jpeg는 대비가 적은 사진 이미지에 유리하도록 설계되어있다. 이러한 사진들은 png로 저장할경우 파일크기가 크게 증가한다.
    - png의 경우 text, inline art, graphic이 포함된 이미지를 저장할때 jpeg보다 유리할 수 있다. 
    - png는 무손실, JPEG는 손실 압축 방식 사용. 
    - png는 투명 사용 가능, jpeg는 투명 전환 안함.
    - jpeg는 반복하여 디코딩후, 인코딩하면 이미지가 손실된다. 


# jpg

## 압축방식

1. 색 공간 변환

    RGB를 YCbCr로 변경.

    이때 YCbCr은 Y는 픽셀의 밝기, Cb,Cr은 색차 성분을 나타낸다.

2. 다운 샘플링

    사람의 눈은 색상 성분보다 밝기 성분에 더 민감하기 때문에 밝기정보보다 색상 성분을 압축하는것이 좋다.

    따라서 Cb, Cr값을 압축하는 방향으로 샘플링

    J:a:b 비율로 샘플링 전략이 

참고 자료 

https://velog.io/@nurungg/PNG-image-format
https://en.wikipedia.org/wiki/Portable_Network_Graphics
https://m.blog.naver.com/data_flow/221825910467

https://bskyvision.com/485

