<p>Cloudflare Web Analytics provides free, privacy-first analytics for your website without changing your DNS or using Cloudflare’s proxy. Cloudflare Web Analytics helps you understand the performance of your web pages as experienced by your site visitors.</p>
<p>All you need to enable Cloudflare Web Analytics is a Cloudflare account and a JavaScript snippet on your page to start getting information on page views and visitors. The JavaScript snippet (also known as a beacon) collects metrics using the Performance API, which is available in all major web browsers.</p>
<h2 id="enable-on-pages-project">Enable on Pages project</h2>
<p>Cloudflare Pages offers a one-click setup for Web Analytics:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Metrics** and select **Enable** under Web Analytics.
<p>Cloudflare will automatically add the JavaScript snippet to your Pages site on the next deployment.</p>
<h2 id="view-metrics">View metrics</h2>
<p>To view the metrics associated with your Pages project:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Web Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the analytics associated with your Pages project.
<p>For more details about how to use Web Analytics, refer to the <a href="/web-analytics/data-metrics/">Web Analytics documentation</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>For Cloudflare to automatically add the JavaScript snippet, your pages need to have valid HTML.</p>
<p>For example, Cloudflare would not be able to enable Web Analytics on a page like this:</p>
<pre><code class="language-html">Hello world.&#10;</code></pre>
<p>For Web Analytics to correctly insert the JavaScript snippet, you would need valid HTML output, such as:</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;title&gt;Title&lt;/title&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;&#10;		&lt;p&gt;Hello world.&lt;/p&gt;&#10;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
