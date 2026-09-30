<p>To configure Zaraz's general settings, go to the <strong>Settings</strong> page in the Cloudflare dashboard:</p>
<div class="nb-dash-button"></div>
<p>Make sure you save your changes, by selecting the <strong>Save</strong> button after making them.</p>
<h2 id="workflow">Workflow</h2>
<p>Allows you to choose between working in Real-time or Preview &amp; Publish modes. By default, Zaraz instantly publishes all changes you make in your account. Choosing Preview &amp; Publish lets you test your settings before committing to them. Refer to <a href="/zaraz/history/preview-mode/">Preview mode</a> for more information.</p>
<h2 id="web-api">Web API</h2>
<h3 id="debug-key">Debug Key</h3>
<p>The debug key is used to enable Debug Mode. Refer to <a href="/zaraz/web-api/debug-mode/">Debug mode</a> for more information.</p>
<h3 id="e-commerce-tracking">E-commerce tracking</h3>
<p>Toggle this option on to enable the Zaraz E-commerce API. Refer to <a href="/zaraz/web-api/ecommerce/">E-commerce</a> for more information.</p>
<h2 id="compatibility">Compatibility</h2>
<h3 id="data-layer-compatibility-mode">Data layer compatibility mode</h3>
<p>Cloudflare Zaraz offers backwards compatibility with the <code>dataLayer</code> function found in tag management software, used to track events and other parameters. You can toggle this option off if you do not need it. Refer to <a href="/zaraz/advanced/datalayer-compatibility/">Data layer compatibility mode</a> for more information.</p>
<h3 id="single-page-application-support">Single Page Application support</h3>
<p>When you toggle Single Page Application support off, the <code>pageview</code> trigger will only work when loading a new web page. When enabled, Zaraz's <code>pageview</code> trigger will work every time the URL changes on a single page application. This is also known as virtual page views.</p>
<h2 id="privacy">Privacy</h2>
<p>Zaraz offers privacy settings you can configure, such as:</p>
<ul>
<li>
<p><strong>Remove URL query parameters</strong>: Removes all query parameters from URLs. For example, <code>https://example.com/?q=hello</code> becomes <code>https://example.com/</code>.</p>
</li>
<li>
<p><strong>Trim IP addresses</strong>: Trims part of the IP address before passing it to server-side loaded tools, to hide it from third-parties.</p>
</li>
<li>
<p><strong>Clean User Agent strings</strong>: Clear sensitive information from the User Agent string by removing information such as operating system version, extensions installed, among others.</p>
</li>
<li>
<p><strong>Remove external referrers</strong>: Hides the page referrers URL if the hostname is different from the website's.</p>
</li>
<li>
<p><strong>Cookie domain</strong>: Choose the domain on which Zaraz will set your tools' cookies. By default, Zaraz will attempt to save the cookies on the highest-level domain possible, meaning that if your website is on <code>foo.example.com</code>, the cookies will be saved on <code>example.com</code>. You can change this behavior and configure the cookies to be saved on <code>foo.example.com</code> by entering a custom domain here.</p>
</li>
</ul>
<h2 id="injection">Injection</h2>
<h3 id="auto-inject-script">Auto-inject script</h3>
<p>This option automatically injects the script needed for Zaraz to work on your website. It is turned on by default.</p>
<p>If you turn this option off, Zaraz will stop automatically injecting its script on your domain. If you still want Zaraz functionality, you will need to add the Zaraz script manually. Refer to <a href="/zaraz/advanced/load-zaraz-manually/">Load Zaraz manually</a> for more information.</p>
<h3 id="iframe-injection">Iframe injection</h3>
<p>When toggled on, the Zaraz script will also be injected into <code>iframe</code> elements.</p>
<h2 id="endpoints">Endpoints</h2>
<p>Specify custom URLs for Zaraz's scripts. You need to use a valid pathname:</p>
<pre><code class="language-txt">/&lt;PATHNAME&gt;/&lt;FILE.JS&gt;&#10;</code></pre>
<p>This is an example of a custom pathname to host Zaraz's initialization script:</p>
<pre><code class="language-txt">/my-server/my-scripts/start.js&#10;</code></pre>
<h3 id="http-events-api">HTTP Events API</h3>
<p>Refer to <a href="/zaraz/http-events-api/">HTTP Events API</a> for more information on this endpoint.</p>
<h2 id="other">Other</h2>
<h3 id="bot-score-threshold">Bot Score Threshold</h3>
<p>Choose whether to prevent Zaraz from loading on suspected bot-initiated requests. This is based on the request's <a href="/bots/concepts/bot-score/">bot score</a> which is an estimate, and therefore cannot be guaranteed to be always accurate.</p>
<p>The options are:</p>
<ul>
<li><strong>Block none</strong>: Load Zaraz for all requests, even if those come from bots.</li>
<li><strong>Block automated only</strong>: Prevent Zaraz from loading on requests from requests in the <a href="/bots/concepts/bot-score/#bot-groupings"><strong>Automated</strong> category</a>.</li>
<li><strong>Block automated and likely automated</strong>: Prevent Zaraz from loading on requests from requests in the <a href="/bots/concepts/bot-score/#bot-groupings"><strong>Automated</strong> and <strong>Likely Automated</strong> category</a>.</li>
</ul>
<h3 id="context-enricher">Context Enricher</h3>
<p>Refer to the <a href="/zaraz/advanced/context-enricher/">Context Enricher</a> for more information on this setting.</p>
<h3 id="automatic-pageview-tracking">Automatic Pageview Tracking</h3>
<p>If disabled, Zaraz will not automatically trigger the <code>Pageview</code> action immediately upon user's visit. You can then run <code>zaraz.track(&quot;Pageview&quot;)</code> manually somewhere in the browserside scripts in order to register this event. This can be useful when integrating custom consent solutions – see <a href="/zaraz/consent-management/api/">Consent API</a>.</p>
<h3 id="logpush">Logpush</h3>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p>Send Zaraz events logs to an external storage service.</p>
<p>Refer to <a href="/zaraz/advanced/logpush/">Logpush</a> for more information on this setting.</p>
