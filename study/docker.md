# Docker

- 컨테이너를 만들고 사용할 수 있도록 하는 기술

- 이미지 기반 배포 모델 제공?ㅇ

- 이미지 계층?

- 에자일?
    - 신속하게 개발

CI/CD :continuous Integration/Continuous Deployment

- 컨테이너
    - 시스템의 나머지 부분과 분리된 1개 이상의 프로세스 세트
    - 환경과 독립적으로 프로그램 실행할 수 있게 해주는 것
    - 필요한 모든 파일은 고유한 이미지에서 제공
        - 이식성, 일관성 유지 가능

- 컨테이너 런타임
    - 도커와 같이 컨테이너를 다루는 도구

- 쿠버네티스
    - 컨테이너 런타임을 통해 컨테이너를 오케스트레이션 하는 도구

- 오케스트레이션
    - 여러 서버에 걸친 컨테이너를 관리하는 행위

## Docker vs Virtual Machine

- virtual machine
    - Host OS 위에 Hypervisor와 Guest OS를 올려서 사용
    - 장점
        - 가상화된 하드웨어 위에 Guest OS를 올리는 형식이기에 Host와 완전히 분리된다는 장점이 있다.
        - 더 높은 격리 레벨로 보안적 측면에서 유리
        - 커널을 공유하지 않아서 멀티 OS가능
            - linux 위에 window올리는 것등 여러가지 가능

    - 단점
        - OS위에 또 OS를 올리는거라 느림

- docker
    - docker engine 위에 바이너리만 올라감
    - 장점
        - Host 커널을 공유하다보니 io 처리에서 효율이 높다.
    - 단점

    - Host 커널 공유
        - io 처리에서 효율 높음

