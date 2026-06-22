# This Week in Bitcoin (2026-06-15 to 2026-06-21)

> 📈 **This Week's Pulse:** **16** PRs Merged | **221** Review Events | **1** First-time Contributors | **21** Active Discussions

## The TL;DR
Significant technical exploration into novel blockchain data management strategies, specifically discussions around Fountain Codes, aiming to fundamentally reduce full node storage requirements and resource costs.
Intensified focus on protocol-level advancements for privacy and scalability, highlighted by ongoing work on Pay-to-Many-Recipients (P2MR) and related public key recovery schemes, alongside discussions on more robust K-of-N Lightning Network node architectures.

## Core Code: Merged This Week
### 🛠️ Build, CI & Testing
*   [#1860](https://github.com/bitcoin/bitcoin/pull/1860) **cmake: Emulate Libtool's behavior on NetBSD and OpenBSD** (by [@hebasto](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_hennadii_stepanov))
    * This improves the build process for Bitcoin Core on NetBSD and OpenBSD by emulating Libtool's behavior.
*   [#35441](https://github.com/bitcoin/bitcoin/pull/35441) **ci: inline runner selection** (by [@willcl-ark](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_will_clark))
    * This streamlines CI runner selection, potentially improving the efficiency of automated tests.
*   [#35503](https://github.com/bitcoin/bitcoin/pull/35503) **guix: CMake-related improvements** (by [@hebasto](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_hennadii_stepanov))
    * This PR enhances CMake integration within Guix, benefiting deterministic builds for developers.
*   [#35520](https://github.com/bitcoin/bitcoin/pull/35520) **lint: remove redundant test suite uniqueness check** (by [@l0rinc](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_lorinc_pap))
    * This refines the linting process by removing a redundant test suite uniqueness check.
*   [#35396](https://github.com/bitcoin/bitcoin/pull/35396) **ci: Rewrite broken wrap-valgrind.sh to .py** (by [@maflcko](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_marcofalke))
    * Rewriting the Valgrind wrapper to Python improves the reliability of memory error detection in CI.
*   [#35547](https://github.com/bitcoin/bitcoin/pull/35547) **lint: Require scripted-diff script to succeed** (by [@hodlinator](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_hodlinator))
    * This enforces stricter quality checks for scripted-diffs, improving code maintainability.
*   [#35526](https://github.com/bitcoin/bitcoin/pull/35526) **ci: bump MSan fuzz timeout from 150 to 180 minutes** (by [@Sjors](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_sjors_provoost))
    * Increasing the MSan fuzz test timeout allows for more thorough detection of potential bugs.
*   [#35540](https://github.com/bitcoin/bitcoin/pull/35540) **test: descriptor: bare multisig at TOP level with exactly 3 pubkeys is allowed** (by [@brunoerg](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_bruno_garcia))
    * This clarifies and corrects the behavior for bare multisig descriptors with three pubkeys, relevant for wallet developers.
*   [#35463](https://github.com/bitcoin/bitcoin/pull/35463) **depends: Drop trailing slash from `CMAKE_INSTALL_LIBDIR`** (by [@hebasto](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_hennadii_stepanov))
    * This minor build system fix standardizes library installation paths for better compatibility.
*   [#35546](https://github.com/bitcoin/bitcoin/pull/35546) **ci: Use GCC consistently in i686 task** (by [@maflcko](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_marcofalke))
    * This ensures consistent use of GCC in i686 CI tasks, improving build reliability.
*   [#35538](https://github.com/bitcoin/bitcoin/pull/35538) **test: make TestChain100Setup's m_clock timestamp more readable** (by [@HowHsu](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_hao_xu))
    * This improves the readability of test timestamps, making development and debugging easier.
*   [#1865](https://github.com/bitcoin/bitcoin/pull/1865) **test: enable -Wunused-function in test suite (Fix #1831)** (by [@kallal79](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_kallal79))
    * Enabling a new compiler warning in the test suite helps identify and remove unused code, improving overall quality.
*   [#1867](https://github.com/bitcoin/bitcoin/pull/1867) **test: musig: fix dead "aggnonce encodes two points at infinity" check** (by [@theStack](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_sebastian_falbesoner))
    * This fixes a test related to MuSig nonce validation, ensuring correctness for future Schnorr-related implementations.

### 🛡️ Consensus & Cryptography
*   [#1859](https://github.com/bitcoin/bitcoin/pull/1859) **field: force-inline 5x52 mul and sqr** (by [@l0rinc](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_lorinc_pap))
    * This optimizes field arithmetic operations, potentially improving the performance of cryptographic computations.

### 🔄 Misc / Other
*   [#35173](https://github.com/bitcoin/bitcoin/pull/35173) **util: shorten thread names to avoid Linux truncation** (by [@l0rinc](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_lorinc_pap))
    * Shortening thread names improves debuggability on Linux by preventing name truncation in system tools.
*   [#35470](https://github.com/bitcoin/bitcoin/pull/35470) **argsman: Prevent duplicate option registration across categories** (by [@pablomartin4btc](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_pablo_martin))
    * This prevents duplicate registration of configuration options, enhancing the robustness of command-line argument parsing.

## Core Code: Under Review (Hot PRs)
### 🔄 Misc / Other
*   [#1859](https://github.com/bitcoin/bitcoin/pull/1859) **add LOCK() for proxy related data-structures** (13 review events)
*   [#1859](https://github.com/bitcoin/bitcoin/pull/1859) **field: force-inline 5x52 mul and sqr** (13 review events)
*   [#35173](https://github.com/bitcoin/bitcoin/pull/35173) **util: shorten thread names to avoid Linux truncation** (11 review events)
*   [#35496](https://github.com/bitcoin/bitcoin/pull/35496) **kernel: add `btck_set_mock_time` for testing time-dependent paths** (9 review events)
*   [#35511](https://github.com/bitcoin/bitcoin/pull/35511) **RFC: consensus: Make `CAmount` a class** (7 review events)
*   [#35531](https://github.com/bitcoin/bitcoin/pull/35531) **txindex: use 5-byte siphash keys to optimize disk usage** (7 review events)

## Research & Governance
*   **[Delving]** [Re: Fountain Codes: a way to reduce blockchain storage costs](https://delvingbitcoin.org/t/fountain-codes-a-way-to-reduce-blockchain-storage-costs/2624/2) (8 messages)
    * This thread discusses Fountain Codes as a novel approach to significantly reduce the storage requirements for Bitcoin full nodes. By allowing nodes to store only a fraction of the blockchain while ensuring data availability, this could enhance node accessibility and decentralization.
*   **[Delving]** [Re: State of the transaction privacy work in Bitcoin](https://delvingbitcoin.org/t/state-of-the-transaction-privacy-work-in-bitcoin/2622/2) (8 messages)
    * This discussion provides an update on the ongoing efforts and various proposals aimed at enhancing transaction privacy within the Bitcoin protocol. Participants review the current state of privacy improvements, technical challenges, and future directions for better fungibility.

## Contributor Shoutouts
A huge thanks to everyone who contributed code or reviewed PRs this week!

🎉 **Welcome First-Time Contributors!**
* [@kallal79](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_kallal79)

🥇 **Top Authors (Merged PRs)**
* [@hebasto](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_hennadii_stepanov) (3), [@l0rinc](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_lorinc_pap) (3), [@maflcko](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_marcofalke) (2), [@HowHsu](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_hao_xu) (1), [@Sjors](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_sjors_provoost) (1)

🏆 **Top Reviewers**
* [@maflcko](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_marcofalke) (21), [@fanquake](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_michael_ford) (15), [@ryanofsky](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_russell_yanofsky) (15), [@real-or-random](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_tim_ruffing) (14), [@hebasto](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_hennadii_stepanov) (14)

**All Active Contributors:**
* [@ajtowns](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_anthony_towns), [@andrewtoth](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_andrew_toth), [@brunoerg](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_bruno_garcia), [@danielabrozzoni](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_daniela_brozzoni), [@darosior](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_antoine_poinsot)
* [@edilmedeiros](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_jos_edil_guimar_es_de_medeiros), [@fanquake](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_michael_ford), [@fernandguil](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_guillermo_fernandes), [@furszy](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_matias_furszyfer), [@hebasto](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_hennadii_stepanov)
* [@hodlinator](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_hodlinator), [@HowHsu](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_hao_xu), [@instagibbs](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_greg_sanders), [@ismaelsadeeq](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_abubakar_sadiq_ismail), [@janb84](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_jan_b)
* [@Jay-1409](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_jay_1409), [@josibake](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_oghenovo_usiwoma), [@kallal79](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_kallal79), [@l0rinc](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_lorinc_pap), [@m3dwards](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_max_edwards)
* [@maflcko](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_marcofalke), [@mzumsande](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_martin_zumsande), [@nervana21](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_nervana21), [@optout21](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_optout21), [@pablomartin4btc](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_pablo_martin)
* [@pseudoramdom](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_pseudoramdom), [@real-or-random](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_tim_ruffing), [@rkrux](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_rkrux), [@ryanofsky](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_russell_yanofsky), [@sedited](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_sebastian_kung)
* [@ShauryaaSharma](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_shauryaasharma), [@sipa](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_pieter_wuille), [@siv2r](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_sivaram_dhakshinamoorthy), [@Sjors](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_sjors_provoost), [@stickies-v](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_stickies_v)
* [@stringintech](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_stringintech), [@theStack](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_sebastian_falbesoner), [@theuni](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_cory_fields), [@tobtoht](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_tobtoht), [@vasild](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=can_vasil_dimov)
* [@w0xlt](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_woltx), [@willcl-ark](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_will_clark), [@winterrdog](https://sorukumar.github.io/orange-dev-network/profile.html?uuid=auto_winterrdog)