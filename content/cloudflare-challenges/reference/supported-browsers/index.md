<p>Cloudflare uses browser-based challenges across <a href="/cloudflare-challenges/challenge-types/challenge-pages/">Challenge Pages</a>, <a href="/turnstile/">Turnstile</a>, <a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections (JSD) in Bot Management</a>, and <a href="/cloudflare-challenges/precursor/">Precursor</a>. This page describes the browser environments that support these checks.</p>
<h2 id="browser-support">Browser support</h2>
<p>Cloudflare challenges support major desktop and mobile browsers.</p>
<h3 id="limited-browser-support">Limited browser support</h3>
<p>The following browsers and environments have limited support and may experience issues.</p>
<ul>
<li>Browsers or operating systems that are more than five years old or have not received security updates in over two years.</li>
<li>Custom or heavily modified browser engines and embedded browsers.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4028.md")
</aside>
<h3 id="unsupported-environments">Unsupported environments</h3>
<p>The following environments are not supported.</p>
<ul>
<li>Internet Explorer browser.</li>
<li>Command-line tools such as <code>wget</code>, <code>curl</code>, or others that lack JavaScript execution capabilities required for Cloudflare Challenges.</li>
<li>Automated browsers are not supported for solving production challenges.</li>
<li>Browser automation frameworks, such as Selenium, Puppeteer, Playwright, and Cypress, are not supported for solving production challenges. For automated Turnstile testing, use <a href="/turnstile/troubleshooting/testing/">Turnstile test keys</a>.</li>
</ul>
<h2 id="common-issues">Common issues</h2>
<h3 id="browser-extensions">Browser extensions</h3>
<p>Browser extensions can interfere with challenges in several ways.</p>
<ul>
<li>Ad blockers and content blockers may prevent challenge scripts from loading properly or block communication with Cloudflare's validation servers.</li>
<li>Privacy-focused extensions like script blockers, fingerprinting protection, or canvas blockers can interfere with the challenge verification process.</li>
<li>Virtual private network (VPN) or proxy extensions might trigger additional security checks or cause IP address inconsistencies.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4027.md")
</aside>
<h3 id="device-emulation-and-developer-tools">Device emulation and developer tools</h3>
<p>Device emulation settings can alter browser signals used by challenges. Results from emulated devices may differ from results on physical devices.</p>
<ul>
<li>Mobile emulation in desktop browsers does not reproduce every characteristic of a physical mobile device.</li>
<li>Browser developer tools can apply network, user-agent, viewport, or JavaScript overrides. Disable these overrides when troubleshooting challenge behavior.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4026.md")
</aside>
<h3 id="webviews-and-in-app-browsers">WebViews and in-app browsers</h3>
<p>Challenges may behave differently depending on embedded browser contexts.</p>
<ul>
<li>WebViews in mobile applications may have limited functionality compared to full browsers</li>
<li>In-app browsers often have restricted JavaScript capabilities</li>
<li>Email client preview windows typically cannot complete Interactive Challenges</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If your visitors consistently experience challenge issues, refer to <a href="/cloudflare-challenges/troubleshooting/challenge-solve-issues/">Challenge solve issues</a> for additional troubleshooting information.</p>
