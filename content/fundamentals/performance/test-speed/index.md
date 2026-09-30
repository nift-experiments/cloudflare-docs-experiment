<p>Cloudflare offers several tools to test the speed of your website, as well as the speed of your Internet connection.</p>
<hr />
<h2 id="test-website-speed">Test website speed</h2>
<h3 id="using-cloudflare">Using Cloudflare</h3>
<p>Once your domain is <a href="/fundamentals/manage-domains/add-site/">active on Cloudflare</a>, you can run speed tests within the <a href="https://dash.cloudflare.com/?to=/:account/:zone/speed">Cloudflare dashboard</a>.</p>
<p>This speed test will provide information about critical loading times, performance with and without <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare's proxy</a>, and recommended optimizations.</p>
<p>If you experience any issues, make sure you are not blocking specific <a href="/fundamentals/reference/cloudflare-site-crawling/#other-situations">user agents</a>.</p>
<h3 id="using-third-party-tools">Using third-party tools</h3>
<p>If your domain is not yet active on Cloudflare or you want to measure the before and after improvements of using Cloudflare, Cloudflare recommends using the following third-party tools:</p>
<ul>
<li><a href="https://pagegym.com/">PageGym</a></li>
<li><a href="https://gtmetrix.com/">GTmetrix</a></li>
<li><a href="https://www.debugbear.com/test/website-speed">DebugBear</a></li>
<li><a href="https://developer.chrome.com/docs/lighthouse/">Lighthouse</a></li>
<li><a href="https://www.webpagetest.org/">WebPageTest</a></li>
</ul>
<p>If you use these third-party tools, you should do the following to test website speed:</p>
<ol>
<li><a href="/fundamentals/manage-domains/pause-cloudflare/">Pause Cloudflare</a> to remove performance and caching benefits.</li>
<li>Run a speed test.</li>
<li>Unpause Cloudflare.</li>
<li>Run a speed test<sup><a href="#footnote-1">1</a></sup>.</li>
<li>Run a second speed test to get your baseline performance with Cloudflare.</li>
</ol>
<h3 id="improve-speed">Improve speed</h3>
<p>Based on the results of these speed tests, you may want to explore other ways to <a href="/speed/">optimize your site speed</a> using Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8809.md")
</aside>
<hr />
<h2 id="test-internet-speed">Test Internet speed</h2>
<p>To test the speed of your home network connection (download, update, packet loss, ping measurements, and more), visit <a href="https://speed.cloudflare.com">speed.cloudflare.com</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">The results of your first speed test with Cloudflare will likely contain uncached results, which will provide inaccurate results.<br/><br/>One of the key ways Cloudflare speeds up your site is through [caching](/cache/), which will appear in the results of the second test.</li></ol></section>
