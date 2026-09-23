## CagsCalcLabs

Embedded networking and security research on constrained hardware.  
Primary platform: TI-84+ CE — eZ80 CPU, 60KB RAM, 48MHz, no OS,
no hardware crypto acceleration.

---

## Projects

<!-- PROJECTS_START -->
**[lwip-ce](https://github.com/cagscalclabs/lwip-ce)** — An IP stack implementation for the TI-84+ CE derived from lwIP code. Implements custom memory management for <60K RAM, assembly optimizations, and a custom lightweight TLS stack engineered for the constraints of the system.  
★ 27 &nbsp;•&nbsp; C &nbsp;•&nbsp; updated 1 week ago  
→ [Site](https://cagscalclabs.github.io/lwip-ce/)

**[cryptx](https://github.com/cagscalclabs/cryptx)** — A standard-derived suite of cryptography libraries for the TI-84+ CE graphing calculator.  
★ 14 &nbsp;•&nbsp; Assembly &nbsp;•&nbsp; updated 3 months ago  
→ [Site](https://cagscalclabs.github.io/cryptx/)

**[.github](https://github.com/cagscalclabs/.github)** — No description.  
★ 0 &nbsp;•&nbsp; Python &nbsp;•&nbsp; updated yesterday

**[discord-ce-server](https://github.com/cagscalclabs/discord-ce-server)** — Discord on a TI-84+ CE. Relay bot server bridging calculators to Discord over TLS, with OIDC device login and verified account linking. Bot posts on behalf of authenticated users.  
★ 0 &nbsp;•&nbsp; Python &nbsp;•&nbsp; updated 3 days ago

**[discord-ce-client](https://github.com/cagscalclabs/discord-ce-client)** — TI-84+ CE Discord client — real-time messaging over the Discord Bot API via lwIP-CE and TLS. Device-code OAuth2/OIDC login, per-server session tokens, channel/server picker, live chat and history.  
★ 0 &nbsp;•&nbsp; C &nbsp;•&nbsp; updated 3 days ago
<!-- PROJECTS_END -->

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
