<p>Cloudflare Fonts is a feature designed for websites that use <a href="https://fonts.google.com/">Google Fonts</a>. It rewrites Google Fonts to be delivered from a website’s own origin, eliminating the need to rely on third-party font providers. Cloudflare Fonts is tailored to improve website performance and user privacy without the need for any code changes or self-hosting of fonts.</p>
<h2 id="how-cloudflare-fonts-works">How Cloudflare Fonts works</h2>
<p>Cloudflare Fonts works by rewriting your webpage’s HTML. It removes Google Fonts links and replaces them with inline CSS. This CSS includes links to fonts from your own Cloudflare zone rather than from Google servers. This ensures that font files are served from your domain through Cloudflare's infrastructure, optimizing performance and enhancing user privacy.</p>
<h3 id="browser-support">Browser support</h3>
<p>Cloudflare Fonts is compatible with browsers that support Unicode-range subsetting and WOFF or WOFF2 formats, including:</p>
<pre><code>Chrome 36+&#10;Edge 16+&#10;Safari 10+&#10;Firefox 44+&#10;Opera 22+&#10;IE 9+&#10;Chrome for Android 115+&#10;Safari on iOS 10+&#10;Samsung Internet 5+&#10;</code></pre>
<h2 id="get-started">Get started</h2>
<p>To enable Cloudflare Fonts for your entire domain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Speed</strong> &gt; <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Content Optimization</strong>.</li>
<li>For <strong>Cloudflare Fonts</strong>, switch the toggle to <strong>On</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13952.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>While Cloudflare Fonts offers powerful font optimization capabilities, it is important to be aware of its limitations:</p>
<ul>
<li><strong>Font transformation</strong>: Currently, Cloudflare Fonts exclusively supports Google Fonts transformation.</li>
<li><strong>APO compatibility</strong>: Cloudflare Fonts does not operate when <a href="/automatic-platform-optimization/">Automatic Platform Optimization</a> (APO) is enabled. Cloudflare APO automatically optimizes Google Fonts in a similar way.</li>
<li><strong>CSS import</strong>: Cloudflare Fonts is compatible only with the <code>&lt;link&gt;</code> setup for Google Fonts and does not support the CSS <code>@import</code> method.</li>
<li><strong>CSP headers</strong>: Cloudflare Fonts does not modify <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/13953.md")
</div> headers. Certain CSP configurations may make Cloudflare Fonts stop working, such as restrictions on inline styles through [`style-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/style-src), or restriction of fonts originating from the site's own origin via [`font-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/font-src).
- **Fallback mechanism**: In cases where Cloudflare Fonts does not support a specific page, it will gracefully fallback to using Google Fonts.
