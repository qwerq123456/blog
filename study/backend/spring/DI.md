# DI (Dependency Injection)

## 의존성

의존성이 무엇인지 예시로 보자.

ex) 
``` java
public class Cook {

    private Knife knife;

    public Cook() {
        knife = new Knife();
    }

    public void cook(Food food) {
        knife.cut(food);
    }
}
```

위의 예시를 보면 Cook 클래스는 cook() 메소드를 실행할때 Knife 클래스의 cut() 메소드가 필요하다. 이런것을 **Cook 클래스가 Knife에 의존성을 가지고 있다**고 한다.

### 의존성에 의한 문제점

1. Unit Test어려움
    - 내부 객체에 대해서 mocking할 방법이 없어서 Unit Test하기 까다로움
    - ~~그렇다는데 아직 안해봐서 모르겠음~~

2. 코드 변경 어려움
    - 위의 예시의 경우 Knife 클래스에 변경사항이 생겼을때 Cook 클래스 또한 변경해야한다. (강한 결합력) 
    - 낮은 결합력과 높은 응집도에 해가 가는 행위이다. 

### 의존성 주입

위의 문제를 해결하기 위해 의존성 주입이 생겨났다.

1. 생성자
``` java
public class Cook {
    
    private Knife knife;

    public Cook(Knife knife) {
        this.knife = knife;
    }
}
```
2. setter

``` java
public void setKnife (Knife knife) {
    this.knife = knife;
}
```

## DI (Spring)

스프링의 IOC Container가 Bean객체를 생성하고 의존성을 대신 주입해주는것. 
> IOC Container : 사용자가 작성한 메타데이터에 따라 Bean 클래스를 생성 관리해주는 컴포넌트

