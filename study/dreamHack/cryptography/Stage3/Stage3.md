# Stage3 블록 암호

# AES (Advanced Encryption Standard)

DES가 더 이상 안전하지 않게 되자, 새로 선정된 블록 암호 알고리즘이다.

-   Vincent Rijmen, Joan Daemen이 제안한 Rijndael구조
-   암호화, 복호화 성능 뛰어남
-   갈루아 필드, 체, 군

## SPN (Substitution Permutaion Network)

-   곱암호
-   S-Box를 이용하는 치환(Substitution) 과 P-Box를 이용하는 순열 (Permutation)을 여러 라운드에 걸쳐 반복
-   페이스텔 구조보다 두배 안정성 가짐 (페이스텔이 뭔데...)

## AES 구조

-   라운드마다 128비트 크기의 블록을 암호화함
-   암호화 방법
    1. 각 블록을 4\*4 상태 배열로 바꿈(1칸에 8비트)
    2. AddRoundKey함수 적용
    3. 마지막 라운드 전까지 SubBytes, ShiftRows, MixColumns, AddRoundKey 함수 반복 적용
    4. 마지막 라운드는 SubBytes,ShiftRows,AddRoundKey 함수 적용 ( MixColumns 제외 )
-   역함수가 존재하기 때문에 역함수를 이용하여 복호화 함

## AES 라운드 함수

1. SubBytes

    - 각 바이트를 S-Box를 참조하여 치환함. 한 바이트가 48 이면 S-Box의 4,8을 참조하여 치환

2. ShiftRows

    - 2행 한칸, 3행 두칸, 4행 세칸을 왼쪽으로 시프트

3. MixColumns

    갈루아 필드 내에서의 행렬 연산으로 구해짐

    $\begin{bmatrix}b_0\\b_1\\b_2\\b_3 \end{bmatrix}$ = $\begin{bmatrix}02&03&01&01\\01&02&03&01\\01&01&02&03\\03&01&01&02 \end{bmatrix}$\*$\begin{bmatrix}a_0\\a_1\\a_2\\a_3 \end{bmatrix}$

    복호화 시엔 역행렬인

    $\begin{bmatrix}0E&0B&0D&09\\09&0E&0B&0D\\0D&09&0E&0B\\0B&0D&09&0E \end{bmatrix}$

    를 곱한다.

4. AddRoundKey

    - 키 생성 함수로 (Key Schedule) 키를 생성하고, 그 키와 XOR연산을 한다.

5. Key Schedule (키 생성 함수)

    - 키를 하나 입력받고, 첫번째 라운드에선 그대로 사용, 그 이후 라운드에선 RotWord, SubWord, Rcon을 적용하여 키로 사용

    - RotWord

        - 열을 위로 한번 회전

    - SubWord

        - SubBytes에서 사용한 S-Box를 이용하여 각 바이트 치환

    - Rcon
        - R=[01,02,04,08,10,20,40,80,1B,36]인 R에 대해, W<sub>i</sub> 의 최상위 바이트를 R[i/4-1]과 XOR합니다.
        > ~~다른건 정성들여 썼는데 이건 진짜 복붙밖에 답이 없다...ㅠ~~


# DES
이제 안전하지 않아서 다른 암호 기술에 밀려났는데 왜 더 어렵냐 빡치게;;ㅋㅋㅋ