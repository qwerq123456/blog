# Internet

## How does the internet work?

### Internet
컴퓨터들이 서로 통신 가능한 거대한 네트워크

### 연결
두 컴퓨터를 유선 혹은 무선으로 연결 할 수 있다. 

![internet-schema-1](./internet-schema-1.png)

이러한 방식으로 n대의 컴퓨터를 연결 할 수 있다. 이 방법으로 n대의 컴퓨터를 연결하려면 $nC_2$개의 연결이 필요하다. 예를들어 10개의 컴퓨터를 연결하기 위해선 45개의 연결이 필요하다.

![internet-schema-2](./internet-schema-2.png)

이는 컴퓨터가 늘어나게되면 제곱으로 늘어나기 때문에 매우 비효율적이다. 이러한 문제를 해결하기 위해 각 컴퓨터는 라우터라는 다른 컴퓨터에 연결되게 된다. 라우터는 한 컴퓨터에서 다른 컴퓨터로 정보를 전달하는 역할만 하는 컴퓨터이다.
이러한 방식을 채택하면 n개의 연결과 하나의 라우터만 있으면 된다.

![internet-schema-3](./internet-schema-3.png)

위에서 n개의 연결이 있으면 된다고 했지만 사실 아니다. 컴퓨터가 많아지면 하나의 라우터가 모든 컴퓨터의 연결을 다 감당할 수 없다. 라우터도 컴퓨터이기 때문에 라우터 끼리도 연결 할 수 있다. 이를 이용하여 컴퓨터 - 라우터 - 라우터 - 컴퓨터로 연결 하면 네트워크를 무한히 확장할 수 있다.

![internet-schema-5](./internet-schema-5.png)

### 컴퓨터 찾기
네트워크에 연결된 모든 컴퓨터엔 고유한 IP주소가 있고, 이를 이용하여 컴퓨터를 찾을 수 있다. IP주소는 점으로 구분된 4개의 숫자로 이루어 지는데 이를 기억하기 어렵기에 IP주소에 도메인 네임을 지정하여 사용한다.
> 구글의 경우 도메인 네임은 'google.com', IP주소는 '173.194.121.32'이다

### 인터넷과 웹
도메인 네임을 이용하여 웹 사이트에 접속하곤 했다. 이때문에 인터넷과 웹이 같은 개념이라 생각하기 쉽다. 하지만 인터넷은 여러 컴퓨터를 연결하는 기술이고, 웹은 웹서버가 웹 브라우저가 이해할 수 있는 무언가를 제공하는 서비스이다. 즉 인터넷은 인프라, 웹은 서비스 인것이다. 인터넷이라는 인프라에는 웹 말고도 이메일,IRC등의 다른 서비스도 있다. 

## What is HTTP? 

### HTTP (HyperText Transfor Protocol)
인터넷에서 데이터를 주고받을 수 있는 프로토콜

### HTTP 특징
- stateless protocol
    - 상태가 없다 : 이전의 요청과 다음 요청이 독립적이다.
- 연결을 유지하지 않는다.
    - Request 와 Response를 이용하여 동작한다.

## 브라우저 작동 원리

### 브라우저
동기(Synchronous)적으로 (HTML + CSS), Javascript 언어를 해석하여 내용을 화면에 보여주는 응용 소프트웨어<br>
웹 브라우저가 웹 서버에 요청하면 서버의 응답을 받아 이를 클라이언트에 보여준다. 이는 HTML뿐만 아니라 PDF, 이미지등 다양한 형태일 수 있다.



### 참고자료
https://developer.mozilla.org/ko/docs/Learn/Common_questions/How_does_the_Internet_work
https://velog.io/@surim014/HTTP%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80
https://joshua1988.github.io/web-development/http-part1/
https://bbangson.tistory.com/87