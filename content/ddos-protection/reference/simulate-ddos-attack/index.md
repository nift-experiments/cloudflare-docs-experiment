<p>After onboarding to Cloudflare, you may want to simulate DDoS attacks against your Internet properties to test the protection, <a href="/ddos-protection/reference/reports/">reporting</a>, and <a href="/ddos-protection/reference/alerts/">alerting</a> mechanisms. Follow the guidelines in this section to simulate a DDoS attack.</p>
<p>You can only launch DDoS attacks against your own Internet properties — your zone, Spectrum application, or IP range (depending on your Cloudflare services) — and provided that:</p>
<ul>
<li>The Internet properties are not shared with other organizations or individuals.</li>
<li>The Internet properties have been onboarded to Cloudflare in an account under your name or ownership.</li>
</ul>
<h2 id="before-you-start">Before you start</h2>
<p>You do not have to obtain permission from Cloudflare to launch a DDoS attack simulation against your own Internet properties.</p>
<p>It is recommended that you choose the right service and enable the correct features to test against the corresponding DDoS attacks. For example, if you want to test Cloudflare against an HTTP DDoS attack and you are only using Magic Transit, the test is going to fail because you need to onboard your HTTP application to Cloudflare's reverse proxy service to test our HTTP DDoS Protection.</p>
