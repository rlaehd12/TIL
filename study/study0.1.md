# ggul_tip

## vscode 단축키

| 단축키 | 실행 |
| --- | --- |
| ctrl + c | 터미널 프로세스 break |
| Alt + Shift + 방향키 | 원하는 방향에 복붙 |
| Alt + 방향키 | 코드 원하는 방향으로 넘기기 |
| ctrl + Enter | 다음 줄 생성 (코드 중간에서 실행하면 안짤림) (뭐라해야하지 한번 해보시면 알듯..) |
| ctrl + / | 주석처리/해제 |
| ctrl + [ or] | 내어쓰기/들여쓰기 |
| ctrl+ shift + ` | 터미널 열기 |
| ↑  + Enter (터미널에서) | 위에 실행한 명령어 다시 실행 |
| ctrl + k + c | 주석처리(한줄) |
| ctrl + k + u | 주석해제(한줄) |
| ctrl + shift + p, F1 | show all comments |
| Tab  | 들여쓰기 / 터미널에서 자동완성 |
| ctrl + shift + k | 해당 행 삭제 |
| ctrl + b   | 탐색기 켜기  → 토글 사이드 바 |
| shift + PgUp / PgDn | 해당 줄 위 / 아래로 모두 선택 |
|  |  |

## 파이참 단축키

### **코드**

| shift + Enter | 아래로 라인 하나를 추가하며 줄바꿈 |
| --- | --- |
| alt + ctrl + Enter | 위로 라인 하나를 추가하며 줄바꿈 |
| alt + shift + 위/아래 방향키 | 선택된 라인 가지고 이동 |
| ctrl + shift + F10 | Run current File |
| alt + 1 / alt + 2 / ... | 특정 탭 열고 닫기 |
| alt + F12 | 터미널 열고닫기 |
| ctrl + F4 | 탭 닫기 |
| ctrl + g | 특정 라인으로 Go to (이후 라인입력) |
| shift + F11 | 북마크 기능 |
| ctrl + alt + L | 인덴테이션 문제 생겼을 때 align을 자동으로 맞춤 |
| ctrl + d | 한 줄 복사 |
| shift + F6 | 변수 이름 변경 |

---

### **디버깅**

</aside>
💡 (참고) step into & over는 for문과 관계없이 함수 안으로 들어가냐 여부
</aside>

* `shift` + `F9`
  * 현재 위치한 파일 디버거 켜기
* `alt` + `shift` + `F9`
  * 특정 파일 선택해서 디버거 켜기
* `F7` Step INTO
  * 함수 안으로 들어가서 내부 로직 수행
* `F8` Step OVER
  * 함수 안으로 들어가지 않고 return 이후의 statement 수행
* `Alt` + `F9` Run to Cursor
  * 반복문을 수행할 때 1회 수행의 로직이 복잡한 상황에서 (예를 들어) 5번째 로직을 확인해야 하는 경우 0~4번째 로직은 건너뛰고 확인하고 싶을 때 사용하면된다.
* **`ctrl` + `F5`**
  * **Re-debug**
  