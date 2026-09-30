<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 7, 2026</time><h2 id="post-title">WAF and framework adapter mitigations for React and Next.js vulnerabilities</h2>
<div class="changelog-badges"><span>workers</span><span>waf</span></div><div class="changelog-body"><p>Multiple security vulnerabilities were disclosed by the React team and Vercel affecting React Server Components and Next.js. These include denial of service, middleware and proxy bypass, server-side request forgery, cross-site scripting, and cache poisoning issues across a range of severity levels.</p>
<p><strong>We strongly recommend updating your application and its dependencies immediately.</strong> Patched versions are available for React (<code>react-server-dom-webpack</code>, <code>react-server-dom-parcel</code>, and <code>react-server-dom-turbopack</code> <code>19.0.6</code>, <code>19.1.7</code>, and <code>19.2.6</code>) and Next.js (<code>15.5.16</code> and <code>16.2.5</code>).</p>
<h4 id="waf-protections">WAF protections</h4>
<p>Cloudflare WAF rules deployed in response to prior React Server Component CVEs (<a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a> and <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a>) already provide coverage for the newly disclosed denial-of-service vulnerabilities. These rules are enabled by default with a Block action for all customers using the Cloudflare Managed Ruleset, including Free plan customers using the Free Managed Ruleset.</p>
<table>
<thead>
<tr>
<th>Ruleset</th>
<th>Rule description</th>
<th>Rule ID</th>
<th>Default action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a></td>
<td><code>2694f1610c0b471393b21aef102ec699</code></td>
<td>Block</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a></td>
<td><code>aaede80b4d414dc89c443cea61680354</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>The existing rules detect the underlying attack patterns generically. As a result, they apply to the new <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> denial-of-service vulnerability in Server Components and the corresponding Next.js advisory <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>.</p>
<p>Cloudflare is investigating whether WAF rules can be safely and effectively deployed for three of the high-severity advisories: <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>, <a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a>, and <a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a>. If it is possible to create a managed WAF rule that mitigates these CVEs and does not potentially break application behavior, Cloudflare will add additional managed WAF rules. These rules will be announced through the <a href="/waf/change-log/changelog/">WAF changelog</a>. Because these vulnerabilities were shared with Cloudflare with minimal advance notice, we are still investigating what WAF mitigations are possible.</p>
<p>Several of the disclosed vulnerabilities are not possible to block in WAF. We strongly recommend updating your applications so they are not purely reliant on WAF mitigations.</p>
<p>Customers on Pro, Business, or Enterprise plans should ensure that <a href="/waf/get-started/#1-deploy-the-cloudflare-managed-ruleset">Managed Rules are enabled</a>.</p>
<h4 id="next-js-adapters">Next.js adapters</h4>
<p><strong>Vinext:</strong> <a href="https://github.com/cloudflare/vinext">Vinext</a> is a Vite plugin that reimplements the Next.js API surface. Vinext's latest release is not vulnerable to any of the disclosed CVEs. Vinext's architecture differs from stock Next.js in ways that sidestep the affected code paths. For example, it does not implement the PPR resume protocol, does not expose Pages Router data-route endpoints, and strips internal headers such as <code>x-nextjs-data</code> at request boundaries. As an extra layer of defense, we added a React <code>19.2.6</code> or later requirement when running <code>vinext init</code> (<a href="https://github.com/cloudflare/vinext/pull/1118">PR #1118</a>, <a href="https://github.com/cloudflare/vinext/pull/1112">PR #1112</a>) to prevent accidentally running a vulnerable version of React with Vinext.</p>
<p><strong>OpenNext on Cloudflare:</strong> OpenNext is an adapter that lets you deploy Next.js apps to the Cloudflare Workers platform. OpenNext itself is not directly vulnerable to the React denial-of-service CVE, but users must update the Next.js version in their application. The OpenNext team has updated the adapter to further harden against these vectors and released a new version of the Cloudflare adapter. Test fixtures and examples have been updated to use patched versions (<a href="https://github.com/opennextjs/opennextjs-cloudflare/pull/1255">PR #1255</a>).</p>
<h4 id="summary-of-disclosed-vulnerabilities">Summary of disclosed vulnerabilities</h4>
<table>
<thead>
<tr>
<th>Advisory</th>
<th>Severity</th>
<th>Issue</th>
<th>WAF status</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a></td>
<td>High</td>
<td>Denial of service in Server Components</td>
<td><strong>WAF rules in place:</strong> <code>2694f1610c0b471393b21aef102ec699</code>, <code>aaede80b4d414dc89c443cea61680354</code><br/>Cloudflare is investigating additional managed WAF coverage</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a></td>
<td>High</td>
<td>Middleware bypass via segment-prefetch routes</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a></td>
<td>High</td>
<td>Denial of service via connection exhaustion in Cache Components</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv"><code>GHSA-492v-c6pp-mqqv</code></a></td>
<td>High</td>
<td>Middleware bypass via dynamic route parameter injection</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r"><code>GHSA-c4j6-fc7j-m34r</code></a></td>
<td>High</td>
<td>SSRF via WebSocket upgrades</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5"><code>GHSA-36qx-fr4f-26g5</code></a></td>
<td>High</td>
<td>Middleware bypass in Pages Router i18n</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q"><code>GHSA-ffhc-5mcf-pf4q</code></a></td>
<td>Moderate</td>
<td>XSS via CSP nonces</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h"><code>GHSA-gx5p-jg67-6x7h</code></a></td>
<td>Moderate</td>
<td>XSS in <code>beforeInteractive</code> scripts</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh"><code>GHSA-h64f-5h5j-jqjh</code></a></td>
<td>Moderate</td>
<td>Denial of service in Image Optimization API</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7"><code>GHSA-wfc6-r584-vfw7</code></a></td>
<td>Moderate</td>
<td>Cache poisoning in RSC responses</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949"><code>GHSA-vfv6-92ff-j949</code></a></td>
<td>Low</td>
<td>Cache poisoning via RSC cache-busting collisions</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq"><code>GHSA-3g8h-86w9-wvmq</code></a></td>
<td>Low</td>
<td>Middleware redirect cache poisoning</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
</tbody>
</table>
</div></article></div>
