## ✅ HTTP/2 강의 요약

### 📌 1. 등장 배경
- HTTP/1.1은 병렬 처리 제한, 헤더 중복, 파이프라이닝 문제 등의 단점이 있음.
- 이를 해결하기 위해 HTTP/2가 등장.

---

### 📌 2. 핵심 특징
- **멀티플렉싱**: 하나의 TCP 연결로 여러 요청/응답을 동시에 처리.
- **헤더 압축 (HPACK)**: 중복된 헤더 제거로 효율적인 데이터 전송.
- **스트림 ID**: 클라이언트와 서버 요청을 구분.
- **서버 푸시**: 리소스를 클라이언트 요청 없이 미리 전송 (지금은 거의 폐기됨).

---

### 📌 3. 성능 비교
- 여러 이미지 로딩 테스트 결과: HTTP/2가 HTTP/1.1보다 훨씬 빠름.
- 특히 네트워크 제약(예: 3G) 상황에서 성능 차이 더 큼.

---

### 📌 4. 단점 및 한계
- **TCP Head-of-Line Blocking**: 하나의 패킷 유실로 전체 요청이 지연될 수 있음.
- **복잡한 구조**: 프레임, 스트림, 흐름 제어 등 이해와 구현이 어려움.
- **높은 CPU 사용량**: 백엔드에 부담.
- 모든 상황에서 HTTP/2가 더 빠른 것은 아님.

---

### 📌 5. 결론
- HTTP/2는 자원 다중화에 최적화된 프로토콜.
- 요청이 적은 시스템에는 적합하지 않을 수 있음.
- 백엔드 엔지니어라면 HTTP/2의 작동 방식과 한계를 이해하고 적절히 선택해야 함.

---
