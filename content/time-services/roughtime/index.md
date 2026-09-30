<p><a href="https://roughtime.googlesource.com/roughtime">Roughtime</a> is a simple, flexible, and secure authenticated time protocol developed by Google.</p>
<h2 id="background">Background</h2>
<p>Endpoints on the Internet often synchronize their clocks using the <a href="/time-services/ntp/">Network Time Protocol (NTP)</a>. NTP provides precise synchronization, but is frequently deployed without a means of authentication. This is due to a <a href="https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/dowling">combination of issues</a>.</p>
<p>As a result, a man-in-the-middle attacker can easily influence a victim’s clock. By moving them back in time, the attacker can, for example, force a victim to accept an expired (and possibly compromised) TLS certificate or session ticket.</p>
<p>For many applications, <em>precise</em> network time is not essential. It is sufficient to have <em>accurate</em> time to mitigate these kinds of attacks, such as within 10 seconds of real time. This observation is the primary motivation behind Roughtime.</p>
<h2 id="next-steps">Next steps</h2>
<p>For more technical details on Roughtime, refer to the <a href="https://blog.cloudflare.com/roughtime/">introductory blog post</a>.</p>
<p>To get started, refer to <a href="/time-services/roughtime/usage/">Get the Roughtime</a>. For more practical guidance on using the Roughtime, refer to our <a href="/time-services/roughtime/recipes/">how-to guide</a>.</p>
