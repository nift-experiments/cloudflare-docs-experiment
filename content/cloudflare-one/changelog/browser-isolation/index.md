<h2 id="2026-09-09">2026-09-09</h2>

<strong>Improved iOS tap-to-type experience for Browser Isolation</strong>

<p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> has improved the tap-to-type experience for users on iOS devices.</p>
<p>Previously, Browser Isolation displayed a full-screen overlay with the message <code>tap to type</code> when users focused a text field. The prompt now appears inline over the focused text field, reducing disruption when users enter text in isolated sessions.</p>
<p>If the focused text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the text field instead.</p>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/tap-to-type.jpg" alt="Inline tap-to-type prompt over a focused text field in Browser Isolation" /></p>
<p>iOS users should tap twice to begin entering text. This update applies automatically to Browser Isolation sessions on iOS.</p>
<p>For more information on why this interaction is required, refer to <a href="/cloudflare-one/remote-browser-isolation/known-limitations/#ios">iOS limitations</a>.</p>


<h2 id="2026-07-07">2026-07-07</h2>

<strong>Browser Isolation support for authorization proxy endpoints</strong>

<p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> now supports Gateway <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">authorization proxy endpoints</a>. You can apply <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">HTTP Isolate policies</a> to traffic routed through authorization proxy endpoints, the same way you can for traffic from the Cloudflare One Client.</p>
<p>Previously, only <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoints</a> supported Browser Isolation, and only with non-identity policies. Because authorization proxy endpoints authenticate users through an identity provider, you can now apply identity-based Isolate policies to PAC file-proxied traffic without requiring the Cloudflare One Client.</p>
<p>To get started, <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">create an authorization proxy endpoint</a> and <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">build an Isolate policy</a>.</p>


<h2 id="2026-04-10">2026-04-10</h2>

<strong>Canvas Remoting optimizes performance for productivity applications</strong>

<p>Remote Browser Isolation now supports <strong>Canvas Remoting</strong>, improving performance for HTML5 Canvas applications by sending vector draw commands instead of rasterized bitmaps.</p>
<h4 id="2026-04-10-canvas-remoting-performance-key-improvements">Key improvements</h4>
<ul>
<li><strong>10x bandwidth reduction:</strong> Microsoft Word and other Office apps use 90% less bandwidth</li>
<li><strong>Smooth performance:</strong> Google Sheets maintains consistent 30fps rendering</li>
<li><strong>Responsive terminals:</strong> Web-based development environments and AI notebooks work in real-time</li>
<li><strong>Zero configuration:</strong> Enabled by default for all Browser Isolation customers</li>
</ul>
<h4 id="2026-04-10-canvas-remoting-performance-how-it-works">How it works</h4>
<p>Instead of sending rasterized bitmaps for every Canvas update, Browser Isolation now:</p>
<ol>
<li>Captures Canvas draw commands at the source</li>
<li>Converts them to lightweight vector instructions</li>
<li>Renders Canvas content on the client</li>
</ol>
<p>This reduces bandwidth from hundreds of kilobytes per second to tens of kilobytes per second.</p>
<h4 id="2026-04-10-canvas-remoting-performance-managing-canvas-remoting">Managing Canvas Remoting</h4>
<p>To temporarily disable for troubleshooting:</p>
<ul>
<li>Right-click the isolated webpage background</li>
<li>Select <strong>Disable Canvas Remoting</strong></li>
<li>Re-enable the same way by selecting <strong>Enable Canvas Remoting</strong></li>
</ul>
<h4 id="2026-04-10-canvas-remoting-performance-limitations">Limitations</h4>
<p>Currently supports 2D Canvas contexts only. WebGL and 3D graphics applications continue using bitmap rendering. For more information, refer to <a href="/cloudflare-one/remote-browser-isolation/canvas-remoting/">Canvas Remoting</a>.</p>


<h2 id="2025-05-13">2025-05-13</h2>

<strong>SAML HTTP-POST bindings support for RBI</strong>

<p>Remote Browser Isolation (RBI) now supports SAML HTTP-POST bindings, enabling seamless authentication for SSO-enabled applications that rely on POST-based SAML responses from Identity Providers (IdPs) within a Remote Browser Isolation session. This update resolves a previous limitation that caused <code>405</code> errors during login and improves compatibility with multi-factor authentication (MFA) flows.</p>
<p>With expanded support for major IdPs like Okta and Azure AD, this enhancement delivers a more consistent and user-friendly experience across authentication workflows. Learn how to <a href="/cloudflare-one/remote-browser-isolation/setup/">set up Remote Browser Isolation</a>.</p>


<h2 id="2025-05-01">2025-05-01</h2>

<strong>Browser Isolation Overview page for Zero Trust</strong>

<p>A new <strong>Browser Isolation Overview</strong> page is now available in the Cloudflare Zero Trust dashboard. This centralized view simplifies the management of <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation (RBI)</a> deployments, providing:</p>
<ul>
<li><strong>Streamlined Onboarding:</strong> Easily set up and manage isolation policies from one location.</li>
<li><strong>Quick Testing:</strong> Validate <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">clientless web application isolation</a> with ease.</li>
<li><strong>Simplified Configuration:</strong> Configure <a href="/cloudflare-one/access-controls/policies/isolate-application/">isolated access applications</a> and policies efficiently.</li>
<li><strong>Centralized Monitoring:</strong> Track aggregate usage and blocked actions.</li>
</ul>
<p>This update consolidates previously disparate settings, accelerating deployment, improving visibility into isolation activity, and making it easier to ensure your protections are working effectively.</p>
<p><img src="/assets/upstream/images/changelog/browser-isolation/browser-isolation-overview.png" alt="Browser Isolation Overview" /></p>
<p>To access the new overview, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a> and find Browser Isolation in the side navigation bar.</p>


<h2 id="2025-03-04">2025-03-04</h2>

<strong>Gain visibility into user actions in Zero Trust Browser Isolation sessions</strong>

<p>We're excited to announce that new logging capabilities for <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation (RBI)</a> through <a href="/logs/logpush/logpush-job/datasets/account/">Logpush</a> are available in Beta starting today!</p>
<p>With these enhanced logs, administrators can gain visibility into end user behavior in the remote browser and track blocked data extraction attempts, along with the websites that triggered them, in an isolated session.</p>
<pre><code class="language-json">{&#10;	&quot;AccountID&quot;: &quot;$ACCOUNT_ID&quot;,&#10;	&quot;Decision&quot;: &quot;block&quot;,&#10;	&quot;DomainName&quot;: &quot;www.example.com&quot;,&#10;	&quot;Timestamp&quot;: &quot;2025-02-27T23:15:06Z&quot;,&#10;	&quot;Type&quot;: &quot;copy&quot;,&#10;	&quot;UserID&quot;: &quot;$USER_ID&quot;&#10;}&#10;</code></pre>
<p>User Actions available:</p>
<ul>
<li><strong>Copy &amp; Paste</strong></li>
<li><strong>Downloads &amp; Uploads</strong></li>
<li><strong>Printing</strong></li>
</ul>
<p>Learn more about how to get started with Logpush in our <a href="/logs/logpush/">documentation</a>.</p>


<h2 id="2024-11-21">2024-11-21</h2>

<strong>Improved non-English keyboard support</strong>

<p>You can now type in languages that use diacritics (like á or ç) and character-based scripts (such as Chinese, Japanese, and Korean) directly within the remote browser. The isolated browser now properly recognizes non-English keyboard input, eliminating the need to copy and paste content from a local browser or device.</p>


<h2 id="2024-03-21">2024-03-21</h2>
<p><strong>Removed third-party cookie dependencies</strong></p>
<p>Removed dependency on third-party cookies in the isolated browser, fixing an issue that previously caused intermittent disruptions for users maintaining multi-site, cross-tab sessions in the isolated browser.</p>


