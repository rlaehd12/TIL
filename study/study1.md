# Git 기본기
* README.md
 * 설명서

####Repository

* 특정 디렉토리를 버전 관리하는 저장소
 * git init으로 로컬 저장소 생성
 * 절대 root에서 git init 하면 안됨 - 내 컴퓨터에 일어나는 모든 일을 관리
 * 내가 버전 관리할 구간에서 git init

* README.md 생성하기
 * 새 폴더를 만들고 init로 생성
 * 특정 버전으로 남긴다 = commit 한다
 * 커밋은 3가지 영역을 바탕으로 동작

>working directory
* 변화를 만드는 곳 -> git add로 staging area에 넘겨야 함
* 아무것도 안하면 untracked

>staging area
* 삭제/생성/변경 ***커밋***으로 남기고 싶은, ***특정 버전***으로 관리하고 싶은 파일이 있는 곳
*git commit 명령어로 repository에 넘김

>repository
* 커밋들이 저장되는 곳

#### staging area 필요성
* 중간 확인?

# github에 올리기
* git remote add origin *LINK~* 
 * repository link를 연결
 * origin은 바꿔도 됨
* git push -u origin master
 * 자격인증
* git push 만 하면 됨

* github에서는 수정 안하는게 좋음

> add - commit - push 순서로 이루어짐