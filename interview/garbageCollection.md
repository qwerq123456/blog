# GarbageCollection

## stop-the-world
GC를 실행하기 위해 JVM이 어플리케이션 실행을 멈추는것<br>
실행시 GC쓰레드 제외 모든 쓰레드는 작업 중단
Major GC 발생

## garbageCollection
Java는 코드에서 메모리를 명시적으로 해제하지 않기에 GC가 더이상 필요없는 객체를 찾아서 지우게 된다. 

### GC의 가설(weak generational hypothesis)
- 대부분의 객체는 금방 unreachable이 된다.
- 오래된 객체에서 젊은 객체로의 참조는 아주 적게 존재한다.

### GC 영역
weak generational hypothesis의 강점을 살리기 위해 두개의 물리적 공간으로 나눈다.
- young 영역 : 새롭게 생성된 객체. 대부분이 금방 unreachable이 되기때문에 많은 객체들이 young영역에서 사라진다. 사라질때 minor GC가 발생

- old 영역 : young 영역에서 unreachable이 되지 않는 객체들이 old영역으로 온다. young영역보다 더 크게 할당되며, GC가 발생하는 빈도수가 young에 비해 적다. 사라질때 Major GC가 발생

### young 영역
young영역은 Eden영역과 Survivor영역 2개로 이루어진다.<br>
young영역에서의 처리 순서는 아래와 같다.

1. 새로 생성된 객체는 Eden영역에 위치
2. GC한번 실행후 살아남은 객체는 Survivor영역으로 이동
3. 계속 Survivor영역에 쌓이다가 가득 차게 되면 그중에서 살아남은 객체만 다른 Survivor영역에 옮기고 기존 Survivor영역을 비운ㄴ다.
4. 위의 과정이 반복되다가 계속 살아있는 객체는 old영역으로 이동

위의 모든 과정에서 survivor영역 둘중 하나는 비어있어야한다. 둘다 비어있지 않거나 둘다 비어있는건 시스템이 정상적으로 작동하지 않는것.

### old 영역
old영역에 데이터가 가득 차면 실행한다.