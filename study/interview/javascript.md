# Javascript 관련 인터뷰 질문


## JavaScript
객체 기반의 스크립트 프로그래밍 언어

## EventLoop 란?

### JavaScript Engine
> Call Stack, Task Queue, Heap + Event loop으로 이루어진다.

- Queue : 
    - Stack이 비었을경우 queue에서 작업을 하나 stack으로 보냄
    - rxjs scheduler : queue 내에서도 순서가 다르네
        > 일단 task queue만 신경써도 될거같긴함...
        1. microtask
            - promise같은거
        2. task
            - settimeout같은거
- Stack :
    - 하나의 코드 실행해주는 공간 (싱글 쓰레드)
    - 코드를 순서대로 실행함
    - ajax, settimeout, eventlistener등의 것들은 queue로 보냄

- Heap : 변수 저장

## Hoisting

선언한게 맨위로 끌올되는것.

but 할당은 런타임에서 되기때문에 호이스팅 x

참고
https://asfirstalways.tistory.com/362
https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/JavaScript