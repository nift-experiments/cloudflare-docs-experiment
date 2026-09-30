<p>Cloudflare's Under Attack mode performs additional security checks to help mitigate layer 7 DDoS attacks. Validated users access your website and suspicious traffic is blocked. It is designed to be used as one of the last resorts when a zone is under attack (and will temporarily pause access to your site and impact your site analytics).</p>
<p>When enabled, visitors receive an interstitial page.</p>
<h2 id="turn-on-under-attack-mode">Turn on Under Attack mode</h2>
<p>Under Attack mode is turned off by default for your zone.</p>
<h3 id="globally">Globally</h3>
<p>To put your entire zone in Under Attack mode:</p>
<ol>
<li>In the Cloudflare dashboard, select your account and zone from the <strong>Account home</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the zone overview page, turn on <strong>Under Attack Mode</strong> in the <strong>Quick Actions</strong> sidebar.</li>
</ol>
<h3 id="selectively">Selectively</h3>
<p>To enable Under Attack mode for specific pages or sections of your site, use a <a href="/rules/configuration-rules/">configuration rule</a> to adjust the <strong>Security Level</strong>.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/8770.md")
</div>
<p>To turn it on for specific ASNs (hosts/ISPs that own IP addresses), countries, or IP ranges, use <a href="/waf/tools/ip-access-rules/">IP Access Rules</a>.</p>
<hr />
<h2 id="preview-under-attack-mode">Preview Under Attack mode</h2>
<p>To preview what Under Attack mode looks like for your visitors:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configurations</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Custom Pages</strong>.</li>
<li>For <strong>Managed Challenge / I'm Under Attack Mode™</strong>, select <strong>Custom Pages</strong> &gt; <strong>View default</strong>.</li>
</ol>
<p>The <code>Checking your browser before accessing...</code> challenge determines whether to block or allow a visitor within five seconds. After passing the challenge, the visitor does not observe another challenge until the duration configured in <a href="/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/">Challenge Passage</a>.</p>
<hr />
<h2 id="potential-issues">Potential issues</h2>
<p>Since the Under Attack mode requires your browser to support JavaScript to display and pass the interstitial page, it is expected to observe impact on third party analytics tools.</p>
