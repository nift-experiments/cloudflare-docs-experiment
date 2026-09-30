<h2 id="sites-not-proxied-through-cloudflare">Sites not proxied through Cloudflare</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Web Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add a site</strong>.</li>
<li>In <strong>Set up hostname</strong>, write your website's hostname.</li>
<li>Select the message box that appears to choose the hostname you have input and select <strong>Done</strong>.</li>
<li>Copy the JS snippet from <strong>Manage site</strong>. This is also where you can later edit the hostname you have just added.</li>
<li>(Optional) Select <strong>View Analytics sites</strong> to go back on the Web Analytics interface. If you prefer to continue setting up Web Analytics website, continue reading.</li>
<li>Add the JS snippet to any of your website’s HTML pages before the ending body tag.</li>
</ol>
<p>Web analytics is now set up on your website, but it may take a few minutes for Web Analytics data to appear.</p>
<p>Repeat steps 3-7 for all the websites you want to track with Web Analytics by selecting <strong>Add a site</strong> from Web Analytics. In <strong>Web Analytics Sites</strong>, select <strong>Manage site</strong> inside each website's card to adjust Web Analytics for your site at any time.</p>
<p>For more information on how many sites you can track, refer to <a href="/web-analytics/limits/">Limits</a>.</p>
<hr />
<h2 id="sites-proxied-through-cloudflare">Sites proxied through Cloudflare</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Web Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add a site</strong>.</li>
<li>Select a hostname from the drop-down menu &gt; <strong>Done</strong>.</li>
</ol>
<p>Your website is now using Web Analytics through the automatic setup, which is enabled by default.</p>
<p>You always have the option to go to <strong>Manage Site</strong> and change the automatic setup to one of the following:</p>
<ul>
<li><strong>Enable, excluding visitor data in the EU</strong> - The JS Snippet will not be injected for visitors from the EU.</li>
<li><strong>Enable with JS Snippet installation</strong> - The JS Snippet needs to be installed manually.</li>
<li><strong>Disable</strong> - The JS Snippet will not be injected and has been disabled.</li>
</ul>
<p>Repeat these steps for all of the websites you want to track with Web Analytics. Web Analytics is enabled by default for sites proxied through Cloudflare that previously used Browser Insights. Adjust Web Analytics for your site at any time by selecting <strong>Manage site</strong> from Web Analytics.</p>
<p>For more information on how many sites you can track, refer to <a href="/web-analytics/limits/">Limits</a>.</p>
<p>For more information on how to configure which sites or pages you track with Web Analytics, refer to <a href="/web-analytics/configuration-options/rules/">Rules</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15776.md")
</aside>
<hr />
<h2 id="pages-projects">Pages projects</h2>
<p>Cloudflare Pages offers a one-click setup for Web Analytics:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Metrics** and select **Enable** under Web Analytics.
<p>Cloudflare will automatically add the JavaScript snippet to your Pages site on the next deployment.</p>
