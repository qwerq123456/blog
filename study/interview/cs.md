# Thread vs Process

## Process

프로세스(process)는 컴퓨터에서 연속적으로 실행되고 있는 컴퓨터 프로그램을 말한다.

## Thread

스레드(thread)는 어떠한 프로그램 내에서, 특히 프로세스 내에서 실행되는 흐름의 단위를 말한다.

## 프로세스, 스레드 작동방식

프로세스가 메모리에 올라갈때 OS는 프로세스에 Code/Data/Stack/Heap의 방식으로 메모리를 할당해준다. 모든 프로세스는 독립적인 메모리를 가진다.

스레드는 메모리를 서로 공유할 수 있다. 프로세스의 메모리 영역 내에서 Stack 영역은 각 스레드가 따로 할당 받고, 나머지 Code/Data/Heap영역은 공유한다.

## 멀티태스킹

멀티테스킹은 한 OS내에서 여러 프로세스가 실행되는것이다. 하지만, 여러 프로세스가 동시에 실행되는 것은 아니다. 

## 멀티 스레드

한 프로세스 내에서 여러개의 스레드를 이용하여 작업을 동시에 처리하는 것



