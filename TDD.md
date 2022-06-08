# TDD
tdd 관련 공부를 하면서 정리하기

# Setting
테스트 전에 세팅 한것 정리

## package.json
### scripts

test : 테스트만 돌음 ( 내가 만든 테스트 케이스에 대해 돌아감 )

coverage : 테스트 다 돌고 나서 지정한 테스트 범위에 대한 coverage 보여줌 
- jest.config.js의 collectCoverageFrom 에 추가하면 coverage 보여줄 파일 추가 가능

### devDependencies
jest, ts-jest, babel-jest, @types/jest 를 27버전으로 설치 (하위는 안같아도 되지만 메인 버전은 같아야함. 처음 init 할때 26버전 이였고 최신이 28인데 둘다 싫어서 27버전으로함...)


## jest.config.js
이것저것 세팅 해봤는데 겁나 어려움... 하여튼 엥간한건 다 했다 생각하고 있음. package.json 에서 "jest" 항목에 명시하여 똑같이 할 수 있지만 파일 길어지는게 싫어서 따로 만들었다. 

다른 세팅 없이 jest가 알아서 상단에서 이 파일을 찾아서 적용하는것으로 보인다. 

### setupFiles
- 미리 setup 할 파일 지정 여기서 jest.setup.js 넣어주었다.
- jest.setup.js가 관리가 안되면 파일 하나 더 추가해서 해도 가능할듯?

### collectCoverageFrom 
- --coverage 옵션으로 coverage볼때 이에 해당하는 파일들만 보여줌. 

다른 세팅 많긴 한데 기본 세팅 다 되어있어서 다른건 안건들여도 될듯하다. 

## jest.setup.js
테스트 돌기전에 미리 돌아가는 파일이라 보면 된다. 현재는 미리 모킹을 해두어야 하는 라이브러리들을 모킹해 두었다.

react-native-localize, react-native/Libraries/EventEmitter/NativeEventEmitter, react-native-device-info, rn-fetch-blob의 4개 라이브러리에 대해 모킹해둠. 

resourceManager만 따로 처리를 했고, 나머지는 getInstance만 undefined가 되지 않도록 jest.fn(() => {})로 모킹해둠.



# TestCode 만드는 과정 정리
코드가 완성된 상태로 테스트 코드를 다는 형태긴 하지만, 이후엔 tdd방식으로 진행할 것 이므로 나름대로 순서를 정해놓고 일을 진행하려 했다. 

나 혼자 만든 기준이기에 이게 좋다는것은 아니다. 좋은 방법은 구글링 하면 많이 나오니 그걸 보자.

1. 코드가 다 완성되어있다고 생각하자
2. describe단에 어떤 주제에 대해 테스트 할지 적는다.
    - 예를 들어 A라는 component에 대해 테스트를 하면 descrbe("Component A Test", () => {}) 이런식으로 적는다.
3. test단에 구체적으로 어떻게 테스트 할지 적는다.
    - ex) A에 props로 temp1 을 줄때와 temp2를 줄때를 기능이 달라서 테스트 해야한다 하면 아래와 같이 적는다.
    - test("should do Something1 with props temp1" , () => {})
    - test("should do Something2 with props temp2" , () => {})
4. test케이스를 모두 정의 하고 나면 사이드 케이스가 없는지 한번 더 확인하고 그 후에 실제로 테스트 코드를 적는다.

2,3,4를 실제 코드를 가지고 있지 않은채로 기획을 보고 진행하면 그게 tdd인듯 하다.

실제 코드를 가지고 하는거보다 어려울 것으로 보이고, 기획 명세 변화, 기획만 보고는 알 수 없는 여러 사이드 케이스 등이 문제가 될 수 있다.

이런 문제를 발생시키지 않으려면 기획측에서도 어느정도 책임감 있는(?) 기획을 던져줘야 할것으로 보이고, 개발단에서도 신중하게 설계하고 테스트 코드를 짜야할 것 같다. 

