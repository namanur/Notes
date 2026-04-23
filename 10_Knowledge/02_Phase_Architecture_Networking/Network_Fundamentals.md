# Phase 2: Network Fundamentals
**Track:** Architecture & Networking
**Parent:** 

## 🧠 Mental Model: The Brutal Reality of Bits
Forget the "cloud." Networking is the violent negotiation of voltage and light across physical media, abstracting into a stack of lies we call layers.

1. **L2 (Data Link):** MAC addresses and ARP. This is your immediate neighborhood. If ARP is poisoned, you're shouting at a thief.
2. **L3 (Network):** IP addresses and Routing. The global map. Routers don't care about your "connection"; they only care about the next hop for a specific packet.
3. **L4 (Transport):** TCP (The Reliable Bureaucrat) vs. UDP (The Fire-and-Forget Chaos). TCP is a state machine (SYN -> SYN-ACK -> ACK). If the state machine hangs, the application dies.
4. **L7 (Application):** DNS, HTTP, SSH. This is where the human-readable magic happens. DNS is the most fragile link in the chain—always assume it's DNS.

---

## 💻 Technical Deep Dive: Modern Diagnostics
Stop using `ifconfig` and `netstat`. They are fossils.

### 1. The `ip` Suite (Routing and Interface)
```bash
# Show all interfaces and IPs
ip -c a

# Show the routing table (Who is my gateway?)
ip route show

# Monitor network events in real-time (Link up/down, IP changes)
ip monitor
```

### 2. The `ss` Tool (Socket Statistics)
```bash
# List all listening TCP ports with process IDs
ss -tulpn

# Show established connections and their timers
ss -teoi
```

### 3. DNS & Connectivity
```bash
# Query DNS records (Modern alternative to nslookup)
dig +short google.com A

# Inspect the HTTP handshake and headers
curl -vI https://google.com

# Scan for open ports on a target (Use responsibly)
nmap -sV -p- localhost
```

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Force mistakes and handle failure.*

1. **The Gateway Blindness:** Manually delete your default route (`sudo ip route del default`) and try to ping 8.8.8.8. Restore it using `sudo ip route add default via <your_gateway_ip>`.
2. **The Port Hunt:** Run a simple Python server (`python3 -m http.server 8080`). Use `ss` to find its PID. Kill it using only the information from `ss`.
3. **Header Autopsy:** Use `curl -v` on a site with a 301 redirect. Trace the `Location` header manually.
4. **DNS Debugging:** Edit `/etc/hosts` to point `google.com` to `127.0.0.1`. Try to browse. Experience the "Ghost in the Machine" before reverting.

---

## 📜 Execution Contract
- **Timebox:** 2 Hours.
- **Start Command:** `ip -c a && ss -tulpn`
- **Completion Condition:** Successfully trace a packet from your machine to a public IP using `mtr` or `traceroute`, identifying every hop.

---
**Links:** [[00_daily_logs/AGENT_ACTIVITY]]
