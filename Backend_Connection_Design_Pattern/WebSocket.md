<<<<<<< HEAD
## 📡 웹 소켓(WebSocket)이란?

### 1. 개요

웹 소켓은 **웹을 위한 양방향 통신 프로토콜**입니다. 일반적으로 웹은 HTTP 기반의 요청/응답 방식으로 통신하지만, 웹 소켓을 사용하면 **브라우저와 서버 간의 실시간, 전이중 통신**이 가능합니다.

- TCP는 본질적으로 양방향 통신이 가능하지만, 웹에 직접 노출되면 보안상 위험이 큽니다.  
- 그래서 웹에서는 TCP 대신 **HTTP 위에서 작동하는 안전한 양방향 통신 방식**, 즉 웹 소켓이 사용됩니다.

---

### 2. 웹 소켓은 어떻게 작동할까?

#### 🧾 웹 소켓 핸드셰이크 (Handshake)

1. 클라이언트가 HTTP 프로토콜을 사용해 웹 소켓 연결을 요청합니다:
   ```
   GET /chat HTTP/1.1
   Host: example.com
   Upgrade: websocket
   Connection: Upgrade
   Sec-WebSocket-Key: <랜덤 키>
   Sec-WebSocket-Version: 13
   ```

2. 서버는 다음과 같이 응답하여 프로토콜을 `HTTP`에서 `WebSocket`으로 전환합니다:
   ```
   HTTP/1.1 101 Switching Protocols
   Upgrade: websocket
   Connection: Upgrade
   Sec-WebSocket-Accept: <서명된 키>
   ```

3. 이후, HTTP는 더 이상 사용되지 않고 TCP 기반의 웹 소켓 연결로 대체됩니다. **양방향 통신**이 가능한 상태가 됩니다.

---

### 3. 웹 소켓 주소 체계

- 비보안: `ws://example.com`
- 보안: `wss://example.com`

---

## 🔄 웹 소켓 vs HTTP

| 특징                 | HTTP                              | WebSocket                        |
|----------------------|-----------------------------------|----------------------------------|
| 통신 방식            | 요청/응답 기반 (단방향)          | 전이중 통신 (양방향)            |
| 연결 유지 여부       | 기본적으로 연결 해제됨           | 연결을 지속함                   |
| 실시간 통신 지원     | 불편함 (폴링 필요)               | 실시간 통신에 적합              |
| 방화벽 친화성        | 높음                             | 상대적으로 높음 (HTTP 기반)     |
| 상태 유지 여부       | 무상태(stateless)                | 상태 유지(stateful)            |
| 서버 푸시            | 불가능 / 폴링 필요               | 가능                             |

---

## 🛠 웹 소켓 사용 사례

- 채팅 애플리케이션 (WhatsApp, Discord 등)
- 실시간 피드 (트위터 스트리밍, 뉴스 속보)
- 멀티플레이어 게임
- 실시간 알림 시스템 (Push Notification)
- 금융 거래 시스템 (주식 시세 등)

---

## ✅ 장점

- **실시간 양방향 통신 가능**
- **낮은 오버헤드**: HTTP 요청/응답 반복이 없음
- **빠른 응답 시간**
- **방화벽 우회 가능성 높음**: HTTP를 기반으로 하기 때문
- **서버 푸시 기능 내장**

---

## ⚠ 단점

- **상태 유지**: 서버가 클라이언트의 연결 상태를 관리해야 함
- **프록시/중간 장비 처리 복잡성**: WebSocket을 제대로 지원하지 않는 경우도 있음
- **수평 확장 어려움**: 연결이 오래 지속되기 때문에 로드 밸런싱 복잡
- **유지 관리 이슈**: Ping/Pong 등 keep-alive 처리가 필요
- **안정성 문제**: 라우터/방화벽에 의해 연결이 예기치 않게 끊길 수 있음

---

## 📌 웹 소켓은 언제 써야 하나?

- **실시간성**이 중요할 때
- 서버가 **능동적으로 클라이언트에게 알림을 전송해야 할 때**
- 지속적인 연결이 허용되고, 상태 유지가 가능할 때

💡 단, 단순한 웹 서비스나 불특정 다수에게 빈번히 연결이 발생하는 서비스에는 **SSE(Server-Sent Events)** 또는 **HTTP Long Polling**도 고려할 수 있습니다.
=======
## 웹 소켓 강의 요약

### 1. 웹 소켓이란?
웹 소켓(WebSocket)은 웹을 위한 양방향 통신 기술로, 클라이언트와 서버 간의 지속적인 데이터 교환을 가능하게 합니다. HTTP를 통해 연결을 설정한 후, TCP 기반의 지속적인 통신으로 업그레이드됩니다.

### 2. 웹 소켓의 필요성
- TCP는 강력하지만, 보안상의 이유로 웹 브라우저에서 직접 사용하기 어려움
- 웹 소켓을 이용하면 HTTP 기반 보안 환경에서 TCP의 양방향 통신을 활용할 수 있음

### 3. 웹 소켓 연결 과정
1. **클라이언트가 HTTP 요청을 보냄** (`Upgrade: websocket` 포함)
2. **서버가 응답하여 연결을 업그레이드함** (`101 Switching Protocols` 반환)
3. **양방향 데이터 전송 가능** (연결이 유지되며 메시지를 주고받음)

### 4. 웹 소켓의 주요 사용 사례
- **실시간 채팅 (예: WhatsApp, Discord)**
- **라이브 피드 및 알림 (예: Twitch, 뉴스 업데이트)**
- **멀티플레이어 게임**
- **실시간 데이터 모니터링 및 대시보드**

### 5. 웹 소켓의 장단점
#### ✅ 장점
- **전이중(Full-Duplex) 통신**: 서버와 클라이언트가 동시에 데이터를 주고받을 수 있음
- **낮은 오버헤드**: HTTP 요청-응답 방식보다 효율적
- **방화벽 친화적**: 기본적으로 HTTP 포트를 사용하여 연결 유지 가능

#### ❌ 단점
- **프록시 및 방화벽 문제**: 일부 네트워크 환경에서 차단될 수 있음
- **연결 유지 비용**: 서버가 지속적으로 연결을 관리해야 함
- **로드 밸런싱 어려움**: 상태 유지(Stateful) 방식이라 수평 확장에 불리함

### 6. 웹 소켓 vs. 다른 기술
| 기술 | 특징 | 주요 사용 사례 |
|------|------|--------------|
| 웹 소켓 | 양방향, 실시간 | 채팅, 게임, 실시간 알림 |
| HTTP 폴링 | 주기적으로 요청 | 상태 업데이트, 간단한 알림 |
| SSE(Server-Sent Events) | 서버에서 클라이언트로 일방향 전송 | 뉴스 피드, 실시간 대시보드 |

### 7. 웹 소켓 코드 예제 (Python)
#### 서버 코드 (Python + websockets 라이브러리 사용)
```python
import asyncio
import websockets

connected_clients = set()

async def handler(websocket, path):
    # 클라이언트 연결 관리
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # 연결된 모든 클라이언트에게 메시지 전송
            for client in connected_clients:
                if client != websocket:
                    await client.send(f"서버 응답: {message}")
    finally:
        # 연결 종료 시 클라이언트 제거
        connected_clients.remove(websocket)

# 웹 소켓 서버 실행
start_server = websockets.serve(handler, "localhost", 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

#### 클라이언트 코드
```python
import asyncio
import websockets

async def client():
    async with websockets.connect("ws://localhost:8080") as websocket:
        await websocket.send("안녕하세요!")
        response = await websocket.recv()
        print(f"서버로부터 수신된 메시지: {response}")

asyncio.run(client())
```

### 8. 결론
웹 소켓은 실시간 데이터 처리를 위한 강력한 기술이지만, 모든 경우에 적합한 것은 아닙니다. 필요에 따라 SSE, 폴링 등의 대안을 검토하고, 성능 및 확장성을 고려하여 최적의 기술을 선택해야 합니다.

>>>>>>> refs/remotes/origin/main
