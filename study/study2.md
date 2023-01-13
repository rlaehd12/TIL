# 마크다운, 깃 복습
###이란?

* 문서의 구조를 나타내기 위한 사용
 * 디자인X
* 제목
 * '#' h1/h2 -> 모든 마크다운 문서의 기본 틀/골격
* 리스트
 * 순서X - '*' or '-'
 * 순서O - 1,2,3
    * python
        * 자료구조
            * List - 연속된 인덱스를 가진 iterable 한 자료구조
        * tuple
        * dictionary
* 코드블록
```python
a=3
print(a)
```
* URL & image
 * [link]()
 * ![image]()
* 테이블

---

# Git의 기초
> 분산 버전 관리 프로그램
>> 중앙 집중식 관리가 아닌, 서버 그리고 개발자 개인의 PC에도 버전이 동시에 관리가 되어, 리소스를 분산으로 관리하는 것.

1. 백업
2. 복구
3. 협업

### **Git문법**
1. 깃 시작하기

    1. 초기화: `git init`:git local repository 초기화

        * 로컬 레포지토리 생성 후 버전으로 관리할 파일을 `git add`로 단 한번이라도 staging area 에 옮겨줘야 한다.`git init`해도 깃은 어떤 파일의 버전을 관리해야 하는지 모름.

        * 파일의 상태 ***git status***
         1. 최초 생성시 : untracked - 명령어를 통해 지시 필요

         2. git add 후 : staged

         3. git commit : tracked

         4. 파일의 수정이 있을 때 : modified

         5. 최신이면 : up-to-date

    2. `git add` : staging area로 버전관리 할 파일 옮기기

        1. `git add.` : 현재 위치한 워킹 디렉토리에 생긴 모든 변화사항을 staging

        2. `git add {file name}` : file을 지정해서 staging

    3. `git commit -m '하고싶은 말'`

        1. 커밋 메세지는 해당 버전이 어떤 목적에서 생성됐는지.

            * 수정자, 날짜, 수정사항 등은 자동 생성됨.

            * 길이 제한 있음

* `git config --global user.name "username"`

**여기까지가 Local Repository 의 일들**

---

# Remote Repository(원격 레포지토리 / 깃허브)
* 레포지토리 연결하기 : `git remote add origin {remote_repo URL}`

    * root commit 이 존재해야 연결 가능

    * origin이라는 이름은 *원격 저장소*에 *별명*
        * 별명이니까 바꿀 수 있음

*  `git push origin master` : local -> remote로 upload

 * 인증 : 권한이 있는지 확인

 * 인증된 자격은 제어판에 ***자격증명 관리*** 에 보관됨

    * 여러개 쓰면서 꼬이면 그냥 삭제하는게 맘 편함

 * `git push -u origin master`

    * -u 옵션을 주면 나중에 `git push`만 써도 origin에 저장됨.

* add -> commit -> push 순

* `git clone {URL}`
    * 원격에 생성된 저장소를 로컬에 가져옴, 다운로드

---
# 협업
### 1. shared repository

* 권한 있음

* 저장소 생성 후 다른 사용자들에게 공유

* `git pull` 원격이 앞서고 있을때 로컬로 받아오는 것, 업데이트

* ***pull*** 협업시 자주 사용

### 2. folk & PR(Pull Request)

* 권한 없음, 소유권을 안줌.

* 조원이 fork로 저장소를 떠옴 

    * 완전한 복사본을 가져옴, 원본은 수정불가

* 자신의 수정본을 권한자에게 push 요청을 보냄

 ### branch 요약

 * 병렬적인 작업환경을 위해서

 * 완벽하게 분리된/ 독립된 환경

---
### .gitignore

* `touch .gitignore`로 생성

* 깃이 추적 못하게 무시하는 기능

* 저장소 생성시 가장 먼저 .gitignore 생성해야됨.

    * 단 한번이라도 staging area에 들어가면 이제 무시할수 없음

* gitignore.io

    * 관리할것들 다 보여줌.

---
# 기타 등등

> ### 깃 되돌리기(UNDOING)

1. wd 에서 수정된 내용을 이전 상태/ 이전 버전으로

    * `restore`

        * 이전 commit으로 돌아감

        * 버전 기록이 안된 상태여서 위험

        * 깃이 추적하고 있는/ 버전이 기록되고 있는 상태

    * `checkout`

        * 안씀

2. staging area에서 다시 wd로 내리기.
    
    * 작업 내용 남아있음

    1. root-commit 없는 경우

        * `git rm --cached <filename~>`
    
    2. root-commit 있는 경우

        * `git restore --staged <filename~>`

3. repository 단계// 커밋 이후 다시 staging area로

    1. staging area에 새로운게 없을 때

        * 커밋 하자마자 / `git commit --amend`

            * 커밋 메세지 여기서 변경 가능

            * 고유 해시값이 바뀜

    2. staging area에 새거 있을 때

        * 뭔가 있을 때 / `git commit --amend`

        * 바로 전 commit에 현재 staging area에 있는것 까지 추가함

        * 굳?이

### `git reset [옵션] <커밋 ID/해시 값>`

* 옵션

    1. --soft

        * 돌아갈 커밋 이후 커밋된 파일을 staging area로 돌려놓음

    2. --mixed

        * default 값

        * wd로 돌려줌, add하지 않은 상태

        * 수정사항은 남은 상태로

    3. --hard

        * 돌아갈 커밋 이후 커밋된 파일을 전부 없앰

        * untracked상태 파일들은 당연히 남아있음

* 3가지 옵션 모두 커밋내역을 삭제함.

### `git revert`

* 이전의 커밋을 취소했다는 새로운 커밋을 생성함.