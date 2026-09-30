<p><a href="https://datatracker.ietf.org/doc/html/rfc8915">Network Time Security</a> (NTS) provides cryptographic security for the client-server mode of the Network Time Protocol (NTP). This allows users to obtain time in an authenticated manner.</p>
<h2 id="background">Background</h2>
<p>The NTS protocol is divided into two phases:</p>
<ol>
<li><strong>NTS Key Exchange</strong>: Establishes the necessary key material between the NTP client and the server, using a <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">Transport Layer Security (TLS) handshake</a> (the same public key infrastructure as the web). Once the keys are exchanged, the TLS channel is closed and the protocol enters the second phase.</li>
<li><strong>NTS Extension Fields for NTPv4</strong>: Authenticates NTP time synchronization packets using previously established key material. For more information, refer to <a href="https://tools.ietf.org/html/rfc8915">RFC 8915</a>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>NTS is gaining support in many NTP implementations, including <a href="https://chrony-project.org/documentation.html">Chrony</a>, <a href="https://www.ntpsec.org/">NTPsec</a>, and <a href="https://github.com/pendulum-project/ntpd-rs">ntpd-rs</a>. Read the relevant documentation for guidance on setting them up to point to our time service, <code>time.cloudflare.com</code>. Also see <a href="https://www.netnod.se/netnod-time/how-to-use-nts">Netnod's documentation</a> for configuring NTS clients.</p>
