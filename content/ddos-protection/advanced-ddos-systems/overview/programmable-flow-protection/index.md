---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/
  description: Create custom flow-based rules to detect and mitigate volumetric DDoS attacks.
  full_title: Cloudflare Programmable Flow Protection (Beta) · Cloudflare DDoS Protection docs
  head_html: <title>Cloudflare Programmable Flow Protection (Beta) · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Create custom flow-based rules to detect and mitigate volumetric DDoS attacks."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/index.md"><meta property="og:title" content="Cloudflare Programmable Flow Protection (Beta) · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create custom flow-based rules to detect and mitigate volumetric DDoS attacks."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DDoS Protection"><meta name="pcx_tags" content="UDP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/#page","headline":"Cloudflare Programmable Flow Protection (Beta) \u00b7 Cloudflare DDoS Protection docs","description":"Create custom flow-based rules to detect and mitigate volumetric DDoS attacks.","url":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["UDP"]}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/
  schema: 1
---
<p>Programmable Flow Protection is a DDoS protection system that protects against DDoS attacks over custom or standardized Layer 7 UDP-based protocols, such as gaming protocols, financial services protocols, VoIP, telecom, and streaming. In terms of topology, it supports both asymmetric and symmetric configurations, but it will only inspect ingress traffic.</p>
<p>Programmable Flow Protection is currently in closed beta and available as an add-on for the <a href="/magic-transit/">Magic Transit</a> (<a href="/byoip/">BYOIP</a> or Cloudflare-leased IPs) service only. If you would like to enable the system, contact your account team or fill out this <a href="https://www.cloudflare.com/lp/programmableddosprotection/">form</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>The Programmable Flow Protection system allows you to write and run your own packet-layer stateful program in C across Cloudflare's global anycast network as extended Berkeley Packet Filter (eBPF) programs running in the user space. An <a href="https://docs.kernel.org/bpf/">eBPF program</a> is a packet filter system that allows a developer to write performant custom networking logic.</p>
<p>Programmable Flow Protection inspects and parses your UDP-based application's protocols (deep packet inspection) and determines the outcome of the packets based on your program. Using your custom program's logic, you can permit authorized users while actively blocking attacks.</p>
<p>The system is built on top of the <code>flowtrackd</code> platform, Cloudflare's stateful mitigation platform. The Programmable Flow Protection system relies on the DDoS Advanced Protection system's <a href="/ddos-protection/advanced-ddos-systems/overview/">general settings</a> to operate. It respects the <a href="/ddos-protection/advanced-ddos-systems/overview/#prefixes">prefixes</a> that you have selected to route through the Advanced Protection systems, as well as the <a href="/ddos-protection/advanced-ddos-systems/concepts/#allowlist">allowlist</a>. The Advanced DDoS Protection system should be <a href="/ddos-protection/advanced-ddos-systems/overview/#enablement">enabled</a> for the Programmable Flow Protection system to operate.</p>
<p>While in beta, Cloudflare will assist and provide guidance to users to write their own code. Out-of-the-box code snippets (templates) for popular gaming protocols and VoIP protocols may be provided later on.</p>
<hr />
<h2 id="get-started">Get started</h2>
<p>After Programmable Flow Protection has been enabled to your account, go to <strong>Networking</strong> &gt; <strong>L3/4 DDoS Protection</strong> &gt; <strong>Advanced Protection</strong> in the Cloudflare dashboard. Within the <strong>Programmable Flow Protection</strong> tab:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7487.md")
</div>
<p>You can create additional rules with different <a href="/ddos-protection/advanced-ddos-systems/concepts/#rule-settings">rule settings</a> <a href="/ddos-protection/advanced-ddos-systems/concepts/#scope">scoped</a> to various regions and Cloudflare locations to change the <a href="/ddos-protection/advanced-ddos-systems/concepts/#mode">mode</a> (Mitigation or Monitoring) to accommodate for your traffic patterns and business use cases.</p>
<p>The Programmable Flow Protection system supports the <a href="/data-localization/">Data Localization suite</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="beta-functionality-limitations">Beta functionality limitations</h3>
@markup("md", "content/.markup/bodies/7486.md")
</aside>
<h3 id="write-a-basic-program">Write a basic program</h3>
<p>The steps below write a sample program that drops all User Datagram Protocol (UDP) traffic with an IPv6 header. It also drops traffic destined to port 66, as well as traffic that does not have some custom specific application header value in the UDP payload.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7488.md")
</div>
<p>For reference, the example below is the basic program in its entirety:</p>
<pre tabindex="0"><code class="language-c">&#35;define CF_EBPF_HELPER_V0&#10;&#10;&#35;include &lt;cf_ebpf_defs.h&gt;&#10;&#35;include &lt;cf_ebpf_helper.h&gt;&#10;&#10;struct apphdr {&#10;    uint8_t       version;&#10;    uint16_t      length;   // Length of the variable-length token&#10;    unsigned char token[0]; // Variable-length token&#10;} __attribute__((packed));&#10;&#10;uint64_t&#10;cf_ebpf_main(void *state)&#10;{&#10;    struct cf_ebpf_generic_ctx *ctx = state;&#10;    struct cf_ebpf_parsed_headers headers;&#10;    struct cf_ebpf_packet_data *p;&#10;&#10;    if (parse_packet_data(ctx, &amp;p, &amp;headers) != 0) {&#10;        return CF_EBPF_DROP;&#10;    }&#10;    struct ipv6hdr *ipv6_hdr;&#10;    struct udphdr *udp_hdr;&#10;    ipv6_hdr = (struct ipv6hdr *)headers.ipv6;&#10;    if (ipv6_hdr != NULL) {&#10;        return CF_EBPF_DROP;&#10;    }&#10;&#10;    udp_hdr = (struct udphdr *)headers.udp;&#10;    if (ntohs(udp_hdr-&gt;dest) == 66) {&#10;        return CF_EBPF_DROP;&#10;    }&#10;&#10;    struct apphdr *app = (struct apphdr *)(udp_hdr + 1);&#10;    if ((uint8_t *)(app + 1) &gt; headers.data_end) {&#10;        return CF_EBPF_DROP;&#10;    }&#10;&#10;    // The verifier has a special limit that it will not allow offsets&#10;    // beyond 65535. We need this check (token_len &gt; 64000) in order&#10;    // to satisfy that, even though it is not possible.&#10;    uint16_t token_len = app-&gt;length;&#10;    if (token_len &gt; 64000) {&#10;        return CF_EBPF_DROP;&#10;    }&#10;&#10;    if ((uint8_t *)(app-&gt;token + token_len) &gt; headers.data_end) {&#10;        return CF_EBPF_DROP;&#10;    }&#10;&#10;    uint8_t *last_byte = app-&gt;token + token_len - 1;&#10;    if (*last_byte != 0xCF) {&#10;        return CF_EBPF_DROP;&#10;    }&#10;    return CF_EBPF_PASS;&#10;}&#10;</code></pre>
<h3 id="write-a-complex-program-challenge-based-response">Write a complex program: challenge-based response</h3>
<p>The example program below implements a UDP-based challenge-response mechanism using helper functions to maintain state between packets from the same source IP. This is useful for mitigating DDoS attacks by requiring clients to prove they can receive and respond to challenges before allowing their traffic through.</p>
<p>The challenge mechanism works as follows:</p>
<p>When a packet arrives from an unknown source IP, the program generates a challenge packet containing a random nonce and marks the source IP as &quot;challenged&quot; in the state table. The original packet is dropped.</p>
<p>If a packet arrives from a source IP that has already been challenged, the program checks if the packet contains the correct challenge response (the nonce XORed with a secret value). If the response is correct, the source IP is marked as &quot;verified&quot;. If incorrect, the source IP is immediately blocklisted.</p>
<p>Packets from verified source IPs are passed through without further checks.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7489.md")
</div>
<p>For reference, the example below is the complex program in its entirety:</p>
<pre tabindex="0"><code class="language-c">&#35;define CF_EBPF_HELPER_V0&#10;&#10;&#35;include &lt;cf_ebpf_defs.h&gt;&#10;&#35;include &lt;cf_ebpf_helper.h&gt;&#10;&#10;// Challenge-response protocol constants&#10;&#35;define CHALLENGE_SECRET 0xDEADBEEFCAFEBABEULL&#10;&#35;define CHALLENGE_EXPIRY_SECS 60&#10;&#35;define VERIFIED_EXPIRY_SECS 3600&#10;&#10;// Challenge packet structure&#10;struct challenge_packet {&#10;    uint64_t nonce;&#10;    uint64_t response;&#10;};&#10;&#10;uint64_t cf_ebpf_main(void *state)&#10;{&#10;    struct cf_ebpf_generic_ctx *ctx = state;&#10;    struct cf_ebpf_parsed_headers headers;&#10;    struct cf_ebpf_packet_data *p;&#10;&#10;    if (parse_packet_data(ctx, &amp;p, &amp;headers) != 0) {&#10;        return CF_EBPF_DROP;&#10;    }&#10;&#10;    struct udphdr *udp_hdr = headers.udp;&#10;&#10;    // Check source IP status&#10;    uint8_t status;&#10;    uint64_t expiry;&#10;    int ret = get_src_ip_status(&amp;status, &amp;expiry);&#10;&#10;    // Check if status has expired&#10;    int64_t now = timestamp();&#10;    if (ret == 0 &amp;&amp; expiry &gt; 0 &amp;&amp; (uint64_t)now &gt; expiry) {&#10;        ret = -1;  // Treat as new connection&#10;    }&#10;&#10;    // Handle verified source IPs - allow through&#10;    if (ret == 0 &amp;&amp; status == CF_EBPF_SRC_IP_STATUS_VERIFIED) {&#10;        return CF_EBPF_PASS;&#10;    }&#10;&#10;    // Handle challenged source IPs - check for valid response&#10;    if (ret == 0 &amp;&amp; status == CF_EBPF_SRC_IP_STATUS_CHALLENGED) {&#10;        uint64_t stored_nonce;&#10;        if (get_src_ip_data(&amp;stored_nonce) != 0) {&#10;            return CF_EBPF_DROP;&#10;        }&#10;&#10;        // Parse challenge response from packet payload&#10;        struct challenge_packet *resp = (struct challenge_packet *)(udp_hdr + 1);&#10;        if ((uint8_t *)(resp + 1) &gt; headers.data_end) {&#10;            return CF_EBPF_DROP;&#10;        }&#10;&#10;        // Check response using XOR&#10;        uint64_t expected_response = stored_nonce ^ CHALLENGE_SECRET;&#10;        if (resp-&gt;response == expected_response) {&#10;            // Correct response - mark as verified&#10;            set_src_ip_status(CF_EBPF_SRC_IP_STATUS_VERIFIED, VERIFIED_EXPIRY_SECS);&#10;            set_src_ip_data(0);&#10;            return CF_EBPF_PASS;&#10;        }&#10;&#10;        // Wrong response - blocklist immediately&#10;        set_src_ip_status(CF_EBPF_SRC_IP_STATUS_BLOCKLISTED, 0);&#10;        return CF_EBPF_DROP;&#10;    }&#10;&#10;    // New source IP - issue initial challenge&#10;    uint64_t nonce = rand();&#10;    set_src_ip_status(CF_EBPF_SRC_IP_STATUS_CHALLENGED, CHALLENGE_EXPIRY_SECS);&#10;    set_src_ip_data(nonce);&#10;&#10;    struct challenge_packet challenge;&#10;    challenge.nonce = nonce;&#10;    challenge.response = 0;&#10;    set_challenge((uint8_t *)&amp;challenge, sizeof(challenge));&#10;&#10;    return CF_EBPF_DROP;&#10;}&#10;</code></pre>
<p>This program demonstrates several key concepts:</p>
<ul>
<li><strong>State management</strong>: Using <code>get_src_ip_status</code>, <code>set_src_ip_status</code>, <code>get_src_ip_data</code>, and <code>set_src_ip_data</code> to track the challenge state for each source IP.</li>
<li><strong>Challenge emission</strong>: Using <code>set_challenge</code> to send a challenge packet back to the client.</li>
<li><strong>Cryptographic verification</strong>: Using a shared secret to verify that the client correctly responded to the challenge.</li>
<li><strong>Expiry handling</strong>: Using timestamps to expire stale state entries.</li>
</ul>
<h3 id="write-a-complex-program-rate-limiting">Write a complex program: rate limiting</h3>
<p>The example program below implements a per-source-IP rate limiter using a fixed window algorithm. This is useful for mitigating volumetric DDoS attacks by limiting how many packets a single source IP can send within a time window.</p>
<p>The rate limiting mechanism works as follows:</p>
<p>When a packet arrives, the program retrieves the stored state for that source IP. The state contains a window start timestamp and a packet counter, packed into a single 64-bit value. If the current time is still within the window, the counter increments. If the counter exceeds the configured limit, the packet is dropped. When the window expires, the counter resets.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7490.md")
</div>
<p>For reference, the example below is the rate limiting program in its entirety:</p>
<pre tabindex="0"><code class="language-c">&#35;include &lt;cf_ebpf_defs.h&gt;&#10;&#35;define CF_EBPF_HELPER_V0&#10;&#35;include &lt;cf_ebpf_helper.h&gt;&#10;&#10;// Rate limit configuration&#10;// This program implements a fixed (not sliding) window ratelimit.&#10;&#35;define RATE_LIMIT 100         // Maximum packets allowed per window&#10;&#35;define WINDOW_SECONDS 60      // Time window in seconds&#10;&#10;// The source IP table holds a mapping from source IP -&gt; custom u64. We will make the custom u64 value in the &#10;// table hold a timestamp and a counter to accomplish a ratelimit.&#10;// &#10;// NOTE: the source IP table is effectively a LRU cache. If it is full, old values will be evicted. &#10;// Values are also garbage collected from the table every 1hr.&#10;// &#10;// The macros below pack the timestamp (upper 32 bits) and counter (lower 32 bits) into 64-bit data&#10;// into a value that we can store into the source IP table.&#10;&#35;define PACK_STATE(ts, count) (((uint64_t)(ts) &lt;&lt; 32) | ((uint64_t)(count) &amp; 0xFFFFFFFF))&#10;&#35;define UNPACK_TIMESTAMP(data) ((uint32_t)((data) &gt;&gt; 32))&#10;&#35;define UNPACK_COUNTER(data) ((uint32_t)((data) &amp; 0xFFFFFFFF))&#10;&#10;uint64_t cf_ebpf_main(void *state)&#10;{&#10;    // Get current timestamp&#10;    int64_t now = timestamp();&#10;    if (now &lt; 0) {&#10;        return CF_EBPF_PASS; // If timestamp fails, allow the packet&#10;    }&#10;    uint32_t now_secs = (uint32_t)now;&#10;&#10;    // Try to get existing state for this source IP&#10;    uint64_t data;&#10;    int ret = get_src_ip_data(&amp;data);&#10;    uint32_t window_start;&#10;    uint32_t counter;&#10;&#10;    if (ret == -1) {&#10;        // No existing entry - first packet from this IP&#10;        // Initialize: window starts now, counter = 1&#10;        window_start = now_secs;&#10;        counter = 1;&#10;    } else if (ret != 0) {&#10;        // If there&#x27;s other unknown error with getting src_ip_data, pass packet&#10;        return CF_EBPF_PASS;&#10;    } else {&#10;        // Entry exists - unpack the state&#10;        window_start = UNPACK_TIMESTAMP(data);&#10;        counter = UNPACK_COUNTER(data);&#10;        // Check if we&#x27;re still in the same time window&#10;        if (now_secs - window_start &gt;= WINDOW_SECONDS) {&#10;            // Window expired - reset counter and start new window&#10;            window_start = now_secs;&#10;            counter = 1;&#10;        } else {&#10;            // Still in same window - increment counter&#10;            counter++;&#10;            // Check if rate limit exceeded&#10;            if (counter &gt; RATE_LIMIT) {&#10;                // Drop packet without updating state&#10;                // Here is where the actual ratelimit occurs.&#10;                return CF_EBPF_DROP;&#10;            }&#10;        }&#10;    }&#10;    // Store updated state&#10;    uint64_t new_data = PACK_STATE(window_start, counter);&#10;    set_src_ip_data(new_data);&#10;    return CF_EBPF_PASS;&#10;}&#10;</code></pre>
<p>This program demonstrates several key concepts:</p>
<ul>
<li><strong>Bit packing</strong>: Storing multiple values (timestamp and counter) in a single <code>u64</code> using bit shifting.</li>
<li><strong>Fixed window rate limiting</strong>: Tracking packet counts within discrete time windows and resetting when the window expires.</li>
<li><strong>Graceful error handling</strong>: Allowing packets through when helper functions fail to avoid false positives during edge cases.</li>
<li><strong>State table behavior</strong>: The source IP state table is an LRU cache. If it reaches capacity, old entries are evicted. Entries are also garbage collected after one hour of inactivity.</li>
</ul>
<hr />
<h2 id="state">State</h2>
<p>Each program has access to its own local state. State is local to each server and is not shared between datacenters.</p>
<p>State is tied to a specific program. If you modify a rule's mode (disabled, monitoring, or enabled), the content of the state tables persists. However, if you modify a rule's program or the contents of the program itself, the state tables are cleared.</p>
<p>There are two state tables available to your program.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7483.md")
</aside>
<h3 id="source-ip-state-table">Source IP state table</h3>
<p>The source IP state table stores state keyed by source IP address. Each entry contains:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Status</td>
<td>Enum</td>
<td>The status of the source IP: <code>None</code> (0), <code>Challenged</code> (1), <code>Verified</code> (2), or <code>Blocklisted</code> (3).</td>
</tr>
<tr>
<td>User data</td>
<td><code>u64</code></td>
<td>A user-defined value you can set for any purpose.</td>
</tr>
</tbody>
</table>
<p>The default maximum capacity is 1,000 entries.</p>
<p>Use the following helper functions to interact with this table:</p>
<ul>
<li><code>get_src_ip_status</code> — Retrieve the status of the current packet's source IP.</li>
<li><code>set_src_ip_status</code> — Set the status of the current packet's source IP.</li>
<li><code>get_src_ip_data</code> — Retrieve the user data for the current packet's source IP.</li>
<li><code>set_src_ip_data</code> — Store user data for the current packet's source IP.</li>
</ul>
<p>An entry is created in the source IP state table under the following conditions:</p>
<ol>
<li>the program calls <code>set_src_ip_status</code> to mark a source IP as Challenged, Verified, or Blocklisted.</li>
<li>the program calls <code>set_src_ip_data</code> to store custom u64 data for a source IP.</li>
<li>the program calls <code>set_challenge</code> for a new source IP that does not have an existing entry in the table.</li>
</ol>
<h3 id="flow-state-table">Flow state table</h3>
<p>The flow state table stores state keyed by the 4-tuple: source IP, source port, destination IP, and destination port. Each entry contains a <code>u64</code> value you can set for any purpose.</p>
<p>The default maximum capacity is 10,000 entries.</p>
<p>Use the following helper functions to interact with this table:</p>
<ul>
<li><code>get_flow_data</code> — Retrieve the user data for the current flow.</li>
<li><code>set_flow_data</code> — Store user data for the current flow.</li>
</ul>
<p>An entry is created in the flow state table under the following conditions:</p>
<ol>
<li>the program calls <code>set_flow_data</code> to store custom u64 data for a flow.</li>
</ol>
<h3 id="cache-behavior">Cache behavior</h3>
<p>Both state tables are LRU (least recently used) caches. If a table reaches its maximum capacity, the oldest entry is evicted to make room for new entries. Entries are also garbage collected if they have not been accessed in one hour.</p>
<hr />
<h2 id="bpf-helper-functions-and-structures">BPF helper functions and structures</h2>
<p>A helper function is a function provided by the Cloudflare runtime that a customer program calls.</p>
<p>Helper functions are crucial because the BPF Instruction Set Architecture (ISA) only supports certain system calls. For safety purposes, Cloudflare will only compile a BPF object file with a predetermined list of known libraries that a program developer cannot modify.</p>
<p>Helper function definitions and verifier wrapper sources are available on <a href="https://github.com/cloudflare/pfp-tools/tree/main/pfp-headers/include">GitHub</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7482.md")
</aside>
<h3 id="helper-functions">Helper functions</h3>
<h4 id="parse-packet-data"><code>parse_packet_data</code></h4>
<p>Constructs <code>cf_ebpf_parsed_headers</code> from <code>cf_ebpf_generic_ctx</code> and <code>cf_ebpf_packet_data</code>. Performs required memory checks to pass the verifier.</p>
<pre tabindex="0"><code class="language-c">static inline int parse_packet_data(&#10;   struct cf_ebpf_generic_ctx *ctx,&#10;   struct cf_ebpf_packet_data **out_p,&#10;   struct cf_ebpf_parsed_headers *out_headers&#10;);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>ctx</code> — Pointer to the generic context passed into the BPF program.</li>
<li><code>out_p</code> — Pointer to receive the packet data structure.</li>
<li><code>out_headers</code> — Pointer to receive the parsed headers structure.</li>
</ul>
<p><strong>Returns:</strong> <code>0</code> on success, <code>1</code> on failure (for example, packet too short or invalid length). On success, <code>out_headers</code> contains valid IP and UDP header pointers.</p>
<h4 id="rand"><code>rand</code></h4>
<p>Generates a random unsigned integer.</p>
<pre tabindex="0"><code class="language-c">uint64_t rand(void);&#10;</code></pre>
<p><strong>Returns:</strong> A random <code>uint64_t</code> value.</p>
<h4 id="timestamp"><code>timestamp</code></h4>
<p>Returns the current UNIX timestamp (number of non-leap seconds since January 1, 1970 0:00:00 UTC).</p>
<pre tabindex="0"><code class="language-c">int64_t timestamp(void);&#10;</code></pre>
<p><strong>Returns:</strong> The current timestamp as an <code>int64_t</code>.</p>
<h4 id="hash-md5"><code>hash_md5</code></h4>
<p>Computes MD5 hash of the source buffer and stores the result in the destination buffer.</p>
<pre tabindex="0"><code class="language-c">int hash_md5(uint8_t *src, size_t src_len, uint8_t *dest, size_t dest_len);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the source buffer.</li>
<li><code>src_len</code> — Length of the source buffer in bytes.</li>
<li><code>dest</code> — Pointer to the destination buffer (must be at least 16 bytes).</li>
<li><code>dest_len</code> — Length of the destination buffer in bytes.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li>Positive value (number of bytes written) on success.</li>
<li><code>-1</code> if the source buffer is invalid.</li>
<li><code>-2</code> if the destination buffer is null or too small.</li>
</ul>
<h4 id="hash-sha256"><code>hash_sha256</code></h4>
<p>Computes SHA-256 hash of the source buffer and stores the result in the destination buffer.</p>
<pre tabindex="0"><code class="language-c">int hash_sha256(uint8_t *src, size_t src_len, uint8_t *dest, size_t dest_len);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the source buffer.</li>
<li><code>src_len</code> — Length of the source buffer in bytes.</li>
<li><code>dest</code> — Pointer to the destination buffer (must be at least 32 bytes).</li>
<li><code>dest_len</code> — Length of the destination buffer in bytes.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li>Positive value (number of bytes written) on success.</li>
<li><code>-1</code> if the source buffer is invalid.</li>
<li><code>-2</code> if the destination buffer is null or too small.</li>
</ul>
<h4 id="hash-sha512"><code>hash_sha512</code></h4>
<p>Computes SHA-512 hash of the source buffer and stores the result in the destination buffer.</p>
<pre tabindex="0"><code class="language-c">int hash_sha512(uint8_t *src, size_t src_len, uint8_t *dest, size_t dest_len);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the source buffer.</li>
<li><code>src_len</code> — Length of the source buffer in bytes.</li>
<li><code>dest</code> — Pointer to the destination buffer (must be at least 64 bytes).</li>
<li><code>dest_len</code> — Length of the destination buffer in bytes.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li>Positive value (number of bytes written) on success.</li>
<li><code>-1</code> if the source buffer is invalid.</li>
<li><code>-2</code> if the destination buffer is null or too small.</li>
</ul>
<h4 id="hash-crc32"><code>hash_crc32</code></h4>
<p>Computes CRC32 hash of the source buffer and stores the result as a 64-bit integer. This is a convenience wrapper that handles the byte-to-integer conversion internally.</p>
<pre tabindex="0"><code class="language-c">int hash_crc32(uint8_t *src, size_t src_len, uint64_t *dest);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the source buffer.</li>
<li><code>src_len</code> — Length of the source buffer in bytes.</li>
<li><code>dest</code> — Pointer to a <code>uint64_t</code> to receive the CRC32 result.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li>Positive value (number of bytes written internally, always 8) on success.</li>
<li><code>-1</code> if the source buffer is invalid.</li>
<li><code>-2</code> if the destination buffer is null.</li>
</ul>
<h4 id="hash-blake2b512"><code>hash_blake2b512</code></h4>
<p>Computes BLAKE2B-512 hash of the source buffer and stores the result in the destination buffer.</p>
<pre tabindex="0"><code class="language-c">int hash_blake2b512(const uint8_t *src, size_t src_len, uint8_t *dest, size_t dest_len);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the source buffer.</li>
<li><code>src_len</code> — Length of the source buffer in bytes.</li>
<li><code>dest</code> — Pointer to the destination buffer (must be at least 64 bytes).</li>
<li><code>dest_len</code> — Length of the destination buffer in bytes.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li>Positive value (number of bytes written) on success.</li>
<li><code>-1</code> if the source buffer is invalid.</li>
<li><code>-2</code> if the destination buffer is null or too small.</li>
</ul>
<h4 id="hmac-sha256"><code>hmac_sha256</code></h4>
<p>Computes HMAC-SHA256 of the source buffer and stores the result in the destination buffer. The private key is configured at the platform level and is not exposed directly to the BPF program. The key is unique per server and per customer.</p>
<pre tabindex="0"><code class="language-c">int hmac_sha256(uint8_t *src, size_t src_len, uint8_t *dest, size_t dest_len);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the source buffer.</li>
<li><code>src_len</code> — Length of the source buffer in bytes.</li>
<li><code>dest</code> — Pointer to the destination buffer (must be at least 32 bytes).</li>
<li><code>dest_len</code> — Length of the destination buffer in bytes.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li>Positive value (number of bytes written) on success.</li>
<li><code>-1</code> if the source buffer is invalid.</li>
<li><code>-2</code> if the destination buffer is null or too small.</li>
</ul>
<h4 id="hmac-sha512"><code>hmac_sha512</code></h4>
<p>Computes HMAC-SHA512 of the source buffer and stores the result in the destination buffer. The private key is configured at the platform level and is not exposed directly to the BPF program. The key is unique per server and per customer.</p>
<pre tabindex="0"><code class="language-c">int hmac_sha512(uint8_t *src, size_t src_len, uint8_t *dest, size_t dest_len);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the source buffer.</li>
<li><code>src_len</code> — Length of the source buffer in bytes.</li>
<li><code>dest</code> — Pointer to the destination buffer (must be at least 64 bytes).</li>
<li><code>dest_len</code> — Length of the destination buffer in bytes.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li>Positive value (number of bytes written) on success.</li>
<li><code>-1</code> if the source buffer is invalid.</li>
<li><code>-2</code> if the destination buffer is null or too small.</li>
</ul>
<h4 id="hmac-blake2b512"><code>hmac_blake2b512</code></h4>
<p>Computes BLAKE2B-512 HMAC of the source buffer and stores the result in the destination buffer. The private key is configured at the platform level and is not exposed directly to the BPF program. The key is unique per server and per customer.</p>
<pre tabindex="0"><code class="language-c">int hmac_blake2b512(const uint8_t *src, size_t src_len, uint8_t *dest, size_t dest_len);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the source buffer.</li>
<li><code>src_len</code> — Length of the source buffer in bytes.</li>
<li><code>dest</code> — Pointer to the destination buffer (must be at least 64 bytes).</li>
<li><code>dest_len</code> — Length of the destination buffer in bytes.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li>Positive value (number of bytes written) on success.</li>
<li><code>-1</code> if the source buffer is invalid.</li>
<li><code>-2</code> if the destination buffer is null or too small.</li>
</ul>
<h4 id="set-challenge"><code>set_challenge</code></h4>
<p>Sets challenge data for the current packet. Use this to send a challenge packet back to the client.</p>
<pre tabindex="0"><code class="language-c">int set_challenge(uint8_t *src, size_t src_len);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the challenge data buffer.</li>
<li><code>src_len</code> — Length of the challenge data in bytes. If <code>0</code>, the challenge buffer is reset.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li><code>0</code> on success.</li>
<li><code>-4</code> if the source buffer is invalid or exceeds the maximum allowed size.</li>
<li><code>-5</code> if challenges are not enabled.</li>
<li><code>-6</code> if a challenge was sent too recently to this source IP or the global rate limit is exceeded.</li>
</ul>
<h4 id="get-src-ip-status"><code>get_src_ip_status</code></h4>
<p>Retrieves the status value associated with the source IP address from the state table.</p>
<pre tabindex="0"><code class="language-c">int get_src_ip_status(uint8_t *status, uint64_t *expiry);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>status</code> — Pointer to receive the status value (<code>CF_EBPF_SRC_IP_STATUS_CHALLENGED</code>, <code>CF_EBPF_SRC_IP_STATUS_VERIFIED</code>, or <code>CF_EBPF_SRC_IP_STATUS_BLOCKLISTED</code>). Can be null if only expiry is needed.</li>
<li><code>expiry</code> — Pointer to receive the expiry timestamp. Can be null if only status is needed.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li><code>0</code> on success.</li>
<li><code>-1</code> if no entry exists for the source IP.</li>
<li><code>-2</code> if no source IP context is set for the current packet.</li>
<li><code>-3</code> if the provided buffer is too small.</li>
<li><code>-4</code> if both <code>status</code> and <code>expiry</code> are null.</li>
<li><code>-5</code> if the source IP state table is not enabled.</li>
</ul>
<h4 id="set-src-ip-status"><code>set_src_ip_status</code></h4>
<p>Sets the status value associated with the source IP address in the state table.</p>
<pre tabindex="0"><code class="language-c">int set_src_ip_status(uint8_t status, uint64_t expiry_secs);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>status</code> — The status value to set (<code>CF_EBPF_SRC_IP_STATUS_CHALLENGED</code>, <code>CF_EBPF_SRC_IP_STATUS_VERIFIED</code>, or <code>CF_EBPF_SRC_IP_STATUS_BLOCKLISTED</code>).</li>
<li><code>expiry_secs</code> — Number of seconds until the status expires. If <code>0</code>, the status never expires.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li><code>0</code> on success.</li>
<li><code>-2</code> if no source IP context is set for the current packet.</li>
<li><code>-5</code> if the source IP state table is not enabled.</li>
</ul>
<h4 id="get-src-ip-data"><code>get_src_ip_data</code></h4>
<p>Retrieves custom data associated with the source IP address from the state table.</p>
<pre tabindex="0"><code class="language-c">int get_src_ip_data(uint64_t *data);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>data</code> — Pointer to receive the stored data value.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li><code>0</code> on success.</li>
<li><code>-1</code> if no entry exists for the source IP.</li>
<li><code>-2</code> if no source IP context is set for the current packet.</li>
<li><code>-3</code> if the provided buffer is too small.</li>
<li><code>-4</code> if <code>data</code> is null.</li>
<li><code>-5</code> if the source IP state table is not enabled.</li>
</ul>
<h4 id="set-src-ip-data"><code>set_src_ip_data</code></h4>
<p>Stores custom data associated with the source IP address in the state table.</p>
<pre tabindex="0"><code class="language-c">int set_src_ip_data(uint64_t data);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>data</code> — The data value to store.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li><code>0</code> on success.</li>
<li><code>-2</code> if no source IP context is set for the current packet.</li>
<li><code>-5</code> if the source IP state table is not enabled.</li>
</ul>
<h4 id="get-flow-data"><code>get_flow_data</code></h4>
<p>Retrieves custom data associated with the current flow from the state table.</p>
<pre tabindex="0"><code class="language-c">int get_flow_data(uint64_t *data);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>data</code> — Pointer to receive the stored data value.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li><code>0</code> on success.</li>
<li><code>-1</code> if no entry exists for the flow.</li>
<li><code>-2</code> if no flow context is set for the current packet.</li>
<li><code>-3</code> if the provided buffer is too small.</li>
<li><code>-4</code> if <code>data</code> is null or unaligned.</li>
<li><code>-5</code> if the flow state table is not enabled.</li>
</ul>
<h4 id="set-flow-data"><code>set_flow_data</code></h4>
<p>Stores custom data associated with the current flow in the state table.</p>
<pre tabindex="0"><code class="language-c">int set_flow_data(uint64_t data);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>data</code> — The data value to store.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li><code>0</code> on success.</li>
<li><code>-2</code> if no flow context is set for the current packet.</li>
<li><code>-5</code> if the flow state table is not enabled.</li>
</ul>
<h4 id="entropy"><code>entropy</code></h4>
<p>Calculates the Shannon entropy of the source buffer. The result is returned in millibits, ranging from <code>0</code> (all identical bytes) to <code>8000</code> (all 256 byte values equally distributed).</p>
<pre tabindex="0"><code class="language-c">int64_t entropy(uint8_t *src, size_t src_len);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>src</code> — Pointer to the source buffer.</li>
<li><code>src_len</code> — Length of the source buffer in bytes.</li>
</ul>
<p><strong>Returns:</strong></p>
<ul>
<li>Entropy value in millibits (0-8000) on success.</li>
<li><code>-1</code> if the source buffer is invalid.</li>
</ul>
<h4 id="set-network-analytics-tag"><code>set_network_analytics_tag</code></h4>
<p>Sets a custom tag for network analytics reporting. The tag appears along with the packet sample in the Network Analytics dashboard. By default, packets are sampled at 1/10,000 rate.
Only one tag is set per program execution. If program execution calls <code>set_network_analytics_tag</code> multiple times, the last tag value applies to the packet sample.</p>
<pre tabindex="0"><code class="language-c">int set_network_analytics_tag(uint64_t tag);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>tag</code> — The tag value to set. Defaults to <code>0</code> if not set.</li>
</ul>
<p><strong>Returns:</strong> <code>0</code> on success.</p>
<h4 id="ntohs"><code>ntohs</code></h4>
<p>Converts a 16-bit integer from network byte order to host byte order.</p>
<pre tabindex="0"><code class="language-c">uint16_t ntohs(uint16_t netshort);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>netshort</code> — The 16-bit value in network byte order.</li>
</ul>
<p><strong>Returns:</strong> The value in host byte order.</p>
<h4 id="htons"><code>htons</code></h4>
<p>Converts a 16-bit integer from host byte order to network byte order.</p>
<pre tabindex="0"><code class="language-c">uint16_t htons(uint16_t hostshort);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>hostshort</code> — The 16-bit value in host byte order.</li>
</ul>
<p><strong>Returns:</strong> The value in network byte order.</p>
<h4 id="ntohl"><code>ntohl</code></h4>
<p>Converts a 32-bit integer from network byte order to host byte order.</p>
<pre tabindex="0"><code class="language-c">uint32_t ntohl(uint32_t netlong);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>netlong</code> — The 32-bit value in network byte order.</li>
</ul>
<p><strong>Returns:</strong> The value in host byte order.</p>
<h4 id="htonl"><code>htonl</code></h4>
<p>Converts a 32-bit integer from host byte order to network byte order.</p>
<pre tabindex="0"><code class="language-c">uint32_t htonl(uint32_t hostlong);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>hostlong</code> — The 32-bit value in host byte order.</li>
</ul>
<p><strong>Returns:</strong> The value in network byte order.</p>
<h4 id="ntohll"><code>ntohll</code></h4>
<p>Converts a 64-bit integer from network byte order to host byte order.</p>
<pre tabindex="0"><code class="language-c">uint64_t ntohll(uint64_t netlonglong);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>netlonglong</code> — The 64-bit value in network byte order.</li>
</ul>
<p><strong>Returns:</strong> The value in host byte order.</p>
<h4 id="htonll"><code>htonll</code></h4>
<p>Converts a 64-bit integer from host byte order to network byte order.</p>
<pre tabindex="0"><code class="language-c">uint64_t htonll(uint64_t hostlonglong);&#10;</code></pre>
<p><strong>Arguments:</strong></p>
<ul>
<li><code>hostlonglong</code> — The 64-bit value in host byte order.</li>
</ul>
<p><strong>Returns:</strong> The value in network byte order.</p>
<h3 id="structures">Structures</h3>
<h4 id="cf-ebpf-generic-ctx"><code>cf_ebpf_generic_ctx</code></h4>
<p>The generic context structure passed into the BPF program.</p>
<pre tabindex="0"><code class="language-c">struct cf_ebpf_generic_ctx {&#10;   /* Pointer to the beginning of the context data. */&#10;   uint64_t data;&#10;   /* Pointer to the end of the context data. */&#10;   uint64_t data_end;&#10;   /* Space for the program to store metadata. */&#10;   uint64_t meta_data;&#10;};&#10;</code></pre>
<h4 id="cf-ebpf-packet-data"><code>cf_ebpf_packet_data</code></h4>
<p>Contains the raw packet data passed into the BPF program.</p>
<pre tabindex="0"><code class="language-c">struct cf_ebpf_packet_data {&#10;   /* Total length of the packet. */&#10;   size_t   total_packet_length;&#10;   /* Size of the IP header. Supports IPv4 (including options) and IPv6. */&#10;   size_t   ip_header_length;&#10;   /* Bytes of the packet, starting with the IP header. */&#10;   uint8_t  packet_buffer[1500];&#10;};&#10;</code></pre>
<h4 id="cf-ebpf-parsed-headers"><code>cf_ebpf_parsed_headers</code></h4>
<p>Contains pointers to parsed IP and UDP headers. Populated by calling <code>parse_packet_data</code>.</p>
<pre tabindex="0"><code class="language-c">struct cf_ebpf_parsed_headers {&#10;   /* Pointer to the parsed IPv4 header, if present (otherwise null). */&#10;   struct iphdr   *ipv4;&#10;   /* Pointer to the parsed IPv6 header, if present (otherwise null). */&#10;   struct ipv6hdr *ipv6;&#10;   /* Pointer to the parsed UDP header. */&#10;   struct udphdr  *udp;&#10;   /* Raw pointer to the last valid byte of the packet context data. */&#10;   uint8_t        *data_end;&#10;};&#10;</code></pre>
<h4 id="iphdr"><code>iphdr</code></h4>
<p>IPv4 header structure. Source: <a href="https://github.com/torvalds/linux/blob/a7423e6ea2f8f6f453de79213c26f7a36c86d9a2/include/uapi/linux/ip.h#L87">Linux kernel</a>.</p>
<pre tabindex="0"><code class="language-c">struct iphdr {&#10;&#35;if defined(__BYTE_ORDER__) &amp;&amp; __BYTE_ORDER__ == __ORDER_BIG_ENDIAN__&#10;    uint8_t  version:4,&#10;             ihl:4;&#10;&#35;else&#10;    uint8_t  ihl:4,&#10;             version:4;&#10;&#35;endif&#10;    uint8_t  tos;&#10;    uint16_t tot_len;&#10;    uint16_t id;&#10;    uint16_t frag_off;&#10;    uint8_t  ttl;&#10;    uint8_t  protocol;&#10;    uint16_t check;&#10;    uint32_t saddr;&#10;    uint32_t daddr;&#10;};&#10;</code></pre>
<h4 id="ipv6hdr"><code>ipv6hdr</code></h4>
<p>IPv6 header structure. Source: <a href="https://github.com/torvalds/linux/blob/a7423e6ea2f8f6f453de79213c26f7a36c86d9a2/include/uapi/linux/ipv6.h#L118">Linux kernel</a>.</p>
<pre tabindex="0"><code class="language-c">struct ipv6hdr {&#10;&#35;if defined(__BYTE_ORDER__) &amp;&amp; __BYTE_ORDER__ == __ORDER_BIG_ENDIAN__&#10;    uint8_t  version:4,&#10;             priority:4;&#10;&#35;else&#10;    uint8_t  priority:4,&#10;             version:4;&#10;&#35;endif&#10;    uint8_t  flow_lbl[3];&#10;    uint16_t payload_len;&#10;    uint8_t  nexthdr;&#10;    uint8_t  hop_limit;&#10;    uint8_t  saddr[16];&#10;    uint8_t  daddr[16];&#10;};&#10;</code></pre>
<h4 id="udphdr"><code>udphdr</code></h4>
<p>UDP header structure. Source: <a href="https://github.com/torvalds/linux/blob/a7423e6ea2f8f6f453de79213c26f7a36c86d9a2/include/uapi/linux/udp.h#L23">Linux kernel</a>.</p>
<pre tabindex="0"><code class="language-c">struct udphdr {&#10;    uint16_t source;&#10;    uint16_t dest;&#10;    uint16_t len;&#10;    uint16_t check;&#10;};&#10;</code></pre>
<h2 id="program-endpoints">Program endpoints</h2>
<h3 id="upload-a-program">Upload a program</h3>
<p>To upload a program, navigate to Networking &gt; L3/4 DDoS protection &gt; Advanced Protection in the Cloudflare dashboard. Then select the tab titled Programmable Flow Protection.</p>
<p>Under <strong>Programs</strong>, click the button &quot;Upload new program.&quot; This will prompt you to select a file to upload with your <code>C</code> source code.</p>
<p>The Cloudflare API will receive the source code in the <code>C</code> file, compile it into BPF bytecode, and run the verifier against it.</p>
<p>If compilation or verification fails, the API will return a detailed error message.</p>
<p>If compilation and verification succeeds, Cloudflare will store the source code and object file to the account and return the program ID.</p>
<h3 id="update-a-program">Update a program</h3>
<p>During the development process, you may find it useful to update the same program (identified by the same program ID) instead of repeatedly creating new programs as new resources.</p>
<p>To update the program, select the three dots next to your program. Then, select <strong>Overwrite</strong>. This will prompt you to choose a file to upload as your <code>C</code> source code.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7481.md")
</aside>
<h3 id="view-all-programs">View all programs</h3>
<p>To view all uploaded programs and their success statuses, view the table under the section entitled <strong>Programs</strong>.</p>
<p>A link icon next to the program name indicates that the program is currently in use in an active rule and may not be deleted.</p>
<h3 id="delete-a-program">Delete a program</h3>
<p>To delete a program, select the three dots next to the program that you wish to delete. Then, select <strong>Delete</strong>.</p>
<p>Note that you will not be able to delete a program that is referenced in an active Rule.</p>
<p>Note that programs that have a &quot;failed&quot; status (meaning they failed to compile or pass verification) will be automatically and permanently deleted after 30 days of inactivity.</p>
<hr />
<h2 id="rules">Rules</h2>
<p>Only one rule executes per packet. If your account has multiple rules configured, the rule with the most specific <a href="/ddos-protection/advanced-ddos-systems/concepts/#scope">scope</a> executes. For example, a rule scoped to a specific colo takes precedence over a rule scoped to a region, which takes precedence over a global rule. This is why you cannot create more than one global rule.</p>
<h3 id="list-all-rules">List all rules</h3>
<p>To view rules and their associated rule IDs, go to <strong>Networking</strong> &gt; <strong>L3/4 DDoS protection</strong> &gt; <strong>Advanced Protection</strong> in the Cloudflare dashboard. Then, select <strong>Programmable Flow Protection</strong>.</p>
<h3 id="create-a-rule">Create a rule</h3>
<p>To create a rule, go to <strong>Networking</strong> &gt; <strong>L3/4 DDoS protection</strong> &gt; <strong>Advanced Protection</strong> in the Cloudflare dashboard. Then, select <strong>Programmable Flow Protection</strong>.</p>
<p>Under <strong>Rules</strong>, select <strong>Create rule</strong>. Fill out the corresponding fields of your new rule. You will be prompted to select a program, mode, and scope for the rule.</p>
<h3 id="update-a-rule">Update a rule</h3>
<p>To update an existing rule, navigate to the Rules section. Click the three dots next to the rule and select <strong>Edit</strong>.</p>
<p>You will be prompted to edit the mode and scope of the rule. You may not edit the program of the rule because that is an unsafe rollout pattern.</p>
<h3 id="delete-a-rule">Delete a rule</h3>
<p>To delete an existing rule, navigate to the Rules section. Click the three dots next to the rule and select <strong>Delete</strong>.</p>
<hr />
<h2 id="debug-packet-capture-pcap">Debug Packet CAPture (PCAP)</h2>
<p>This API endpoint debugs a program by intaking:</p>
<ul>
<li>A local path to the input PCAP file provided as requested data in binary format. The input PCAP file has a maximum size limit of 5 MB and will be rejected if it is too large.</li>
<li>The program ID provided in the request path.</li>
<li>An optional query parameter <code>ip_offset=&lt;value&gt;</code> to specify IP offset. This is the number of bytes that the IP header is offset by in each packet of the input PCAP file.
If the ip offset query parameter is omitted, the API will make an educated guess on the correct offset value.
For example, if the PCAP file captures Ethernet packets, the detected IP offset value would be 14. This endpoint assumes that all packets in a PCAP have the same IP offset value and will otherwise parse packets incorrectly.</li>
</ul>
<p>This endpoint runs the referenced BPF program against the input PCAP and outputs a new annotated PCAP file. The output PCAP file will contain the exact same packets as the input PCAP file, and will also include the program verdict annotated in the <strong>Packet Comment</strong> section of each packet.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/programmable_flow_protection/configs/programs/$PROGRAM_ID/pcap&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/vnd.tcpdump.pcap&quot; \&#10;&#45;-data-binary &quot;@&lt;PATH_TO_INPUT_PCAP_FILE&gt;&quot; \&#10;&#45;-output output.pcap&#10;</code></pre>
<p>The Packet Comment annotation may contain:</p>
<ul>
<li>Program return value: <code>CF_EBPF_PASS</code> or <code>CF_EBPF_DROP</code></li>
<li><code>Ignored</code>: if the incoming packet is not UDP</li>
<li><code>Analytics tag</code>: the custom network analytics tag set by the program on this packet, if any</li>
</ul>
<p>The output PCAP file may also contain:</p>
<ul>
<li><code>Challenge packet</code>: a challenge packet emitted from the program back to the client, if any</li>
</ul>
<hr />
<h2 id="safe-program-and-rule-deployment-best-practices">Safe program and rule deployment best practices</h2>
<p>You will want to safely deploy and test programs without impacting existing production traffic. An initial deployment approach could be to set a global scoped rule to <code>disabled</code> and set a colo or region level scoped rule to <code>monitoring</code> with a filter expression only acting on some subset of IP traffic.</p>
<p>Each Cloudflare region or colo will apply the most granular rule. So, in the scenario described above, the colos or regions specified in the <code>monitoring</code> rule will execute the developer program in <code>monitoring</code> mode, while every other Cloudflare location will not execute the program at all. The <code>monitoring</code> rule would only execute on traffic that matches the filter expression.</p>
<p>Then, after verifying the correct behavior with Network Analytics, you can update and expand the <code>monitoring</code> rule's scope and filter expression. Eventually, you can delete the <code>disabled</code> and <code>monitoring</code> rules and apply a global <code>enabled</code> rule.</p>
<p>Using the <code>Expression</code> field to limit programs to a subset of IPs or prefixes and the <code>Mode</code> field to dictate whether a program actually drops packets ensures a program's safety and granularity upon rollout.</p>
<hr />
<h2 id="network-analytics">Network Analytics</h2>
<p>Traffic flowing through Programmable Flow Protection can be found in the <a href="/analytics/network-analytics/">Network Analytics</a> dashboard.</p>
<p>In the Network Analytics dashboard, select the <strong>Programmable Flow Protection</strong> tab to filter traffic based on this feature. You can filter traffic by program ID, custom network analytics tags, actions, IPs, and ports. By default, packets are sampled at a rate of 1/10,000.</p>
