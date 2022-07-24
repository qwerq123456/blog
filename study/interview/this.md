# JS this

4가지 케이스가 있다.

## 1.Regular Function Call
일반적인 함수 내에서 this를 사용하는 방식
이때 this는 Global Object를 가리킨다. (브라우저에선 window 객체) 
- ex
    ``` js
    var name = "qwerq123456";
    function foo () { 
        console.log(this.name); // "qwerq123456"
    }
    foo();
    ```
- strict mode
    - 코드 상단에 "use strict" 를 추가하면 strict모드가 된다. 이때는 모든 this가 undefined가 된다.

## 2.Dot Notation
Object를 만들고, Object내에서 key, value로 만든 뒤 Dot(.)으로 값에 접근하는 방식
이때 this 는 객체 자체를 가리킨다.
- ex
    ``` js
    const name = "no name";

    const person = {
        name : "qwerq123456",
        getName : function() {
            console.log(this.name); // "qwerq123456"
        }
    }
    person.getName();
    ```

이때 getName의 this는 person을 가리키므로 this.name은 qwerq123456이 된다.

## 3.Explicit Binding (call, apply, bind)
this의 역할을 명백하게 지정해준다는 뜻. 
call은 this에 해당하는 객체를 넘겨준 뒤, 인자들을 각각 넘겨주고, apply는 인자들을 배열로 넘긴다.
- ex(call, apply)
    ```js
    const age = 15;

    function addAge (a, b) {
        console.log(this.age+a+b);
    }

    const person = {
        age : 25,
        foo : addAge
    }
    addAge.call(person, 1, 2); // 25+1+2 = 28
    addAge.apply(person, [2, 3]); // 25+2+3 = 30
    ```
- ex(bind)
    ```js
    function getAge() {
        return this.age;
    }

    const getAge1 = getAge.bind({age : 1});
    console.log(getAge1());                     // 1

    const getAge2 = getAge1.bind({age : 10});   // bind는 1회만 유효함. 
    console.log(getAge2());                     // 1

    const object = {age: 100, getAge:getAge, getAge1: getAge1, getAge2: getAge2 };
    console.log(object.age, object.getAge(), object.getAge1(),object.getAge2());            // 100, 100, 1, 1
    ```

## 4. new 키워드 이용
new를 이용하여 생성자로 만들어서 사용 할 수 있다.
이때 this는 새로 생긴 객체에 묶인다.
- ex
    ```js
    function getName () {
        console.log(this.name);     // undefined
        this.name = "qwerq123456";
        console.log(this.name);     // "qwerq123456"
    }

    new getName();
    ```
- ex2
    ```js
   function Foo1 () {
        this.age = 1;
    }

    const object1 = new Foo1();
    console.log(object1.age);       // 1

    function Foo2 () {
        this.age = 1;                   
        return {age : 10};
    }

    const object2 = new Foo2();
    console.log(object2.age);       // 10
    ```

참고자료 
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/this
- https://im-developer.tistory.com/96