# Phase 3: Docker & Containerization
**Track:** Data & Middleware
**Parent:** 

## 🧠 Mental Model: The Process Illusion
A container is not a "lightweight VM." It is a normal Linux process with a fancy set of blinkers on.

1. **Namespaces (The Blinkers):** What the process can *see*. (PID, Net, Mount, UTS, IPC, User).
2. **Cgroups (The Cage):** What the process can *consume*. (CPU, Memory, I/O).
3. **Layered FS (UnionFS):** A stack of read-only filesystems with a thin read-write layer on top. This is why images are fast to pull—you only pull the layers you don't have.
4. **The Runtime:** Docker is just a manager. The heavy lifting is done by `containerd` and `runc`.

---

## 💻 Technical Deep Dive: Beyond `docker run`
Master the plumbing, not just the porcelain.

### 1. Image Engineering
```dockerfile
# Use Multi-stage builds to keep images tiny
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY . .
RUN go build -o main .

FROM scratch
COPY --from=builder /app/main /main
ENTRYPOINT ["/main"]
```

### 2. Introspection
```bash
# What is actually happening inside the container's environment?
docker inspect <container_id>

# Run a shell in a running container (The "I need to fix this" command)
docker exec -it <container_id> /bin/sh

# View real-time resource usage
docker stats
```

### 3. Modern Build Engine
```bash
# Build for multiple architectures (ARM/AMD64)
docker buildx build --platform linux/amd64,linux/arm64 -t user/app:latest .
```

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Break the abstraction.*

1. **The Ghost Shell:** Start a container and delete its `ENTRYPOINT` binary from inside using `docker exec`. Observe what happens to the container status.
2. **Layer Hunting:** Create a Dockerfile with 20 `RUN` commands. Build it. Re-write it to use only 1 `RUN` command (chaining with `&&`). Compare the final image sizes.
3. **Network Isolation:** Create a custom bridge network. Start two containers. Verify they can ping each other by container name. Disconnect one from the network while it's running.
4. **Volume Persistence:** Mount a local directory to a container. Write a file inside the container. Delete the container. Verify the file still exists on the host.

---

## 📜 Execution Contract
- **Timebox:** 3 Hours.
- **Start Command:** `docker info && docker network ls`
- **Completion Condition:** Successfully build a multi-stage Dockerfile that results in an image under 10MB and runs a static binary.

---
**Links:** [[AGENT_ACTIVITY|00_daily_logs/AGENT_ACTIVITY]]
