# System Architecture & Scaling: Process Models & Memory

**Phase:** Phase 2 — Architecture & Networking (Days 12-15)
**Links:** [[Linux Fundamentals]]

---

## 🧠 Mental Model: The EEVDF & Virtual Deadlines (Brutal Internals)

Forget simple "round-robin" or even basic CFS (Completely Fair Scheduler). Modern Linux (6.6+) uses **EEVDF (Earliest Eligible Virtual Deadline First)**. 

- **The Core Conflict:** Fairness vs. Latency. CFS was fair but let latency-sensitive tasks (audio, UI) jitter.
- **The Mechanism:** Every task has a **Lag** (Fair share - Actual time).
- **Eligibility:** If your lag is positive, you are "eligible."
- **The Deadline:** The scheduler calculates a **Virtual Deadline** based on your requested time slice.
- **The "Jump":** Tasks can request *smaller* time slices to get *earlier* deadlines, effectively jumping the queue without violating the long-term fair-share math.

**Memory Scaling Mental Model:** The **Buddy Allocator** handles page-level (4KB) allocation, but the **SLUB Allocator** manages the "slabs" of memory for kernel objects (like task structs). SLUB is the "scalability king" because it removes per-CPU queues in favor of metadata stored directly in the page.

---

## 🛠️ Technical Deep Dive: Modern Scaling Patterns

### 1. Transparent Hugepages (THP) & mTHP
- **Pattern:** Using 2MB pages instead of 4KB to reduce TLB (Translation Lookaside Buffer) misses.
- **Command:** `cat /sys/kernel/mm/transparent_hugepage/enabled`
- **Modern Warning:** Databases (Redis, Postgres) hate standard THP because "promotion" causes latency spikes. Use **mTHP** (Multi-size THP) for intermediate 16K/64K sizes.

### 2. NUMA (Non-Uniform Memory Access)
- **Concept:** In multi-socket servers, accessing RAM "far" from your CPU socket is 30-50% slower.
- **Tool:** `numactl --hardware` (Check distance)
- **Pattern:** Bind high-performance processes to specific cores AND their local memory:
  `numactl --cpunodebind=0 --membind=0 ./my_app`

### 3. Load Balancing Domains
- The kernel views hardware as a hierarchy: `SMT -> Core -> Socket -> NUMA Node`.
- **High-Signal Pattern:** It is often faster to wait 10ms for a local CPU with a "hot" L3 cache than to migrate a task to an idle CPU on a different socket.

---

## 🧪 Mastery Drills: High Pain

1. **The Scheduler Torture:** Run a CPU-heavy compilation (`make -j$(nproc)`) and attempt to play a low-latency audio stream. Use `chrt` to change the stream to `SCHED_RR` (Real-Time) and observe the system's choice between fairness and execution.
2. **NUMA Misalignment:** Force a process to run on Node 0 but use memory only from Node 1 using `numactl`. Measure the latency penalty using `perf stat`.
3. **Hugepage Starvation:** Manually reserve all hugepages via `sysctl -w vm.nr_hugepages=1024` and observe the failure mode of an application that requires 2MB contiguous blocks.

---

## 📜 Execution Contract

- **Timebox:** 4 Hours
- **Start Command:** `watch -n 1 "cat /proc/sched_debug | grep -A 20 '.+'"`
- **Completion Condition:** Successfully identify a task with a negative "lag" in `sched_debug` and explain why it was de-scheduled.

---
*Last Updated: 21-04-2026*
