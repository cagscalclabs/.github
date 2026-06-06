![Metrics](https://raw.githubusercontent.com/cagscalclabs/cagscalclabs/main/metrics.svg)

## CagsCalcLabs

Embedded networking and security research on constrained hardware.  
Primary platform: TI-84+ CE — eZ80 CPU, 60KB RAM, 48MHz, no OS, 
no hardware crypto acceleration.

---

## Projects

**[lwIP-CE](https://github.com/cagscalclabs/lwip-ce)** — TCP/IP and TLS 1.3 on a calculator.  
A port of lwIP with USB CDC Ethernet, a custom memory allocator, and a full 
TLS 1.3 client stack fit into 60KB of shared RAM. CAVP-validated primitives, 
differential timing analysis, SAST, and a published security whitepaper. A formalized continuation of CryptX.  
→ [Docs](https://cagscalclabs.github.io/lwip-ce/) • [Whitepaper](https://github.com/cagscalclabs/lwip-ce/releases/download/whitepaper-latest/whitepaper.pdf)

**[CryptX](https://github.com/cagscalclabs/cryptx)** — Embedded cryptography suite for eZ80.  
AES, RSA, SHA-256, HMAC, PBKDF2, SECT233k1, PKCS#1, PKCS#8, SEC1.

---

## What This Work Demonstrates

- TLS 1.3 on 60KB RAM with no hardware crypto acceleration
- Entropy modeling and HWRNG design on hardware with no dedicated RNG
- CAVP-derived vector validation against on-device binaries via emulator pipeline
- Differential timing analysis for side-channel regression detection
- SAST scoped to fork delta against upstream lwIP

---

## Support This Work

If this project is useful or interesting to you, consider sponsoring it.  
→ [Ko-fi](https://ko-fi.com/cagscalclabs) • [GitHub Sponsors](https://github.com/sponsors/cagscalclabs) • [Buy Me a Coffee](https://buymeacoffee.com/cagscalclabs)

---

*Lead developer: [Anthony Cagliano](https://github.com/acagliano97) —  
available for embedded security consulting and employment.*
