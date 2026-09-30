<p>You can load Zaraz on domains that are not proxied through Cloudflare. However, you will need to create a separate domain, or subdomain, proxied by Cloudflare (also <a href="https://community.cloudflare.com/t/step-3-enabling-the-orange-cloud/52715">known as orange-clouded</a> domains), and load the script from it:</p>
<ol>
<li>Create a new subdomain like <code>my-subdomain.example.com</code> and proxy it through Cloudflare. Refer to <a href="https://community.cloudflare.com/t/step-3-enabling-the-orange-cloud/52715">Enabling the Orange Cloud</a> for more information.</li>
<li>Add the following script to your main website’s HTML, immediately before the <code>&lt;/head&gt;</code> tag closes:</li>
</ol>
<pre><code class="language-html">&lt;script src=&quot;https://my-subdomain.example.com/cdn-cgi/zaraz/i.js&quot;&gt;&lt;/script&gt;&#10;</code></pre>
