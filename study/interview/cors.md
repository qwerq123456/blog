# CORS (Cross Origin Resource Sharing)

다른 두개의 어플리케이션이 마음대로 소통하는 환경 위험하다. 웹같은 경우는 심지어 소스도 다 보인다. CSRF나 XSS 등에 취약

## 같은 출처

Scheme, Host, Port가 같을때 같은 출처이다.

## CORS 동작 원리

1. 클라에서 다른 출처에 요청할때 헤드의 Origin 필드에 출처를 담아서 보낸다. 
2. 서버가 응답 헤드에 Access-Control-Allow-Origin에 요청에서 온 출처를 담아 보내준다.
3. 클라는 응답을 받고 요청과 응답의 origin을 비교한다. 

## preflight request

클라가 예비 요청을 하고 그 이후에 본요청을 하는것

예비 요청을 preflight라고 하며 OPTIONS 메소드를 사용해 보낸다. 

## simple request

그냥 예비 요청 없이 보내는것. 근데 이는 조건을 충족할때만 가능

1. GET,HEAD,POST중 하나
2. Accept, Accept-Language, Content-Language, Content-Type, DPR, Downlink, Save-Data, Viewport-Width, Width 이외희 헤더 사용 금지
3. 만약 Content-Type를 사용하는 경우에는 application/x-www-form-urlencoded, multipart/form-data, text/plain만 허용된다.

1번의 경우 PUT, DELETE를 안쓴다고 하더라도, 2,3번은 많이 까다롭다. 유저 인증이나, json도 못쓰는 상태이다. 

## Credentialed Request

인증된 요청 사용

요청에 credentials 옵션을 다는것
credentials :   include 옵션을 사용할 경우 아래의 두가지 조건을 만족해야 한다.

1. Access-Control-Allow-Origin에는 *를 사용할 수 없으며, 명시적인 URL이어야한다.
2. 응답 헤더에는 반드시 Access-Control-Allow-Credentials: true가 존재해야한다.



## CORS 해결

1. Access-Control-Allow-Origin값 세팅. 그냥 * 넣어두면 좋은것 같아보이진 않는다.
2. 로컬에서 할때 Access-Control-Allow-Origin값에 Localhost:3000 이런게 들어있지 않기때문에 발생하곤 한다. 프록시 기능으로 cors정책을 우회하도록 하자.