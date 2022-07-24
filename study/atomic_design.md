# Atomic Design

> We’re not designing pages, we’re designing systems of components. <br> - Stephen Hay

인터페이스를 체계적으로 구성하는것에 중점을 둔 디자인

모든 물질이 원자로 구성되어 있다는 화학에서 아이디어를 얻어서 원자 -> 분자 -> 유기체로 결합하는 과정처럼 인터페이스를 체계적으로 구성한다. 

![img1](./PeriodicTableOftheElements.png)

## Atoms

HTML 테그들을 의미한다. label, input, button 등의 것들을 의미한다.

> 내 개인적인 생각으로는 atoms 단위로 파일을 나누는건 좀 투머치 느낌이긴 하다. 

## Molecules

> “do one thing and do it well” 

재사용을 위해 만들어진 atom의 단순한 조합. <br>
각각의 atom은 큰 의미를 가지기 힘들지만, 모이고 나면 의미를 가진다.

## Organisms

비교적 복잡한 부분을 형성하기 위해 결합된 Molecules 그룹. <br>
Organisms를 통해 인터페이스가 형태를 가지기 시작한다.

Molecules로 Organisms을 만드는것은 독립적이고, 휴대성 있으며, 재사용가능한 컴포넌트를 만들 수 있게 해준다. (standalone, portable, reusable components)

## Templates

Page를 형성하기 위해 Organisms들을 결합한것. <br>
레이아웃이 실제로 작동하게 되는 곳.<br>
처음엔 HTML wireframe으로 시작하지만 점점 구체적으로 변함.

## Pages

Templates의 실제 인스턴스.<br>
실제 사용자가 보게될 페이지.

테스트 해보고 Molecules, Organisms, Templates로 루프백해서 수정.





참고링크

https://bradfrost.com/blog/post/atomic-web-design/