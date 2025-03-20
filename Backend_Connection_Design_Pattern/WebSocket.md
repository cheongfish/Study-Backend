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

