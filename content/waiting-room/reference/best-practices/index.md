<p>Follow these best practices to avoid potential issues and improve the visitor experience.</p>
<h2 id="total-active-users">Total active users</h2>
<p>When specifying the <strong>Total active users</strong> in your <a href="/waiting-room/reference/configuration-settings/">configuration settings</a>, set the value to <code>75%</code> of your origin's traffic capacity.</p>
<h2 id="page-path">Page path</h2>
<p>When setting the waiting room <strong>Path</strong> in your <a href="/waiting-room/reference/configuration-settings/">configuration settings</a>, pay attention to potential subpaths. Waiting rooms are enabled on all subpaths, meaning you might be sending more traffic to your waiting room than anticipated.</p>
<p>Additionally, if you have multiple waiting rooms, the waiting room with the most specific subpath takes precedence.</p>
<h2 id="update-during-active-queueing">Update during active queueing</h2>
<h3 id="waiting-room-template">Waiting room template</h3>
<p>If you want to provide your users with updated information or expectations when they are queueing, Cloudflare recommends that you update your <a href="/waiting-room/how-to/customize-waiting-room/">waiting room template</a>. All changes will be visible to your users in close to real time.</p>
<h3 id="configuration-settings">Configuration settings</h3>
<p>When users are actively queueing, only make changes to your <a href="/waiting-room/reference/configuration-settings/">configuration settings</a> when necessary. These changes may impact the estimated wait time shown to end users, which might lead to user confusion.</p>
<h3 id="queueing-method">Queueing method</h3>
<p>Though you can change your <a href="/waiting-room/reference/queueing-methods/">queueing method</a>, it may affect users if your waiting room is actively queueing:</p>
<ul>
<li><strong>From FIFO to Random</strong>: Users will no longer be ordered based on their cookie timestamp, which may affect the displayed wait time.</li>
<li><strong>From Random to FIFO</strong>: Users will be ordered based on their cookie timestamp, meaning any new users move to the end of the FIFO queue.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15742.md")
</aside>
<h2 id="waiting-room-and-seo">Waiting Room and SEO</h2>
<p>SEO crawlers may end up in a queue during active queueing. When this happens, your sites search results and SEO may be impacted. To avoid this, you can enable SEO Crawler Bypassing from the Waiting Room dashboard or via API. SEO Crawler Bypassing ensures that trusted SEO Crawlers, verified by Bot Management, are never placed in your waiting rooms. By not being queued, SEO crawlers are always able to crawl your site, which helps maintain your SEO and search results in major search engines.</p>
<p>By enabling this service, you understand that these verified crawlers are completely bypassing your waiting rooms. No waiting room settings or features will apply to this traffic.</p>
