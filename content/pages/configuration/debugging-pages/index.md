<p>When setting up your Pages project, you may encounter various errors that prevent you from successfully deploying your site. This guide gives an overview of some common errors and solutions.</p>
<h2 id="check-your-build-log">Check your build log</h2>
<p>You can review build errors in your Pages build log. To access your build log:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Pages project.</li>
<li>Go to <strong>Deployments</strong> &gt; <strong>View details</strong> &gt; <strong>Build log</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/pages/platform/pages-build-log.png" alt="After logging in to the Cloudflare dashboard, access the build log by following the instructions above" /></p>
<p>Possible errors in your build log are included in the following sections.</p>
<h3 id="initializing-build-environment">Initializing build environment</h3>
<p>Possible errors in this step could be caused by improper installation during Git integration.</p>
<p>To fix this in GitHub:</p>
<ol>
<li>Log in to your GitHub account.</li>
<li>Go to <strong>Settings</strong> from your user icon &gt; find <strong>Applications</strong> under Integrations.</li>
<li>Find <strong>Cloudflare Pages</strong> &gt; <strong>Configure</strong> &gt; scroll down and select <strong>Uninstall</strong>.</li>
<li>Re-authorize your GitHub user/organization on the Cloudflare dashboard.</li>
</ol>
<p>To fix this in GitLab:</p>
<ol>
<li>Log in to your GitLab account.</li>
<li>Go to <strong>Preferences</strong> from your user icon &gt; <strong>Applications</strong>.</li>
<li>Find <strong>Cloudflare Pages</strong> &gt; scroll down and select <strong>Revoke</strong>.</li>
</ol>
<p>Be aware that you need a role of <strong>Maintainer</strong> or above to successfully link your repository, otherwise the build will fail.</p>
<h3 id="cloning-git-repository">Cloning git repository</h3>
<p>Possible errors in this step could be caused by lack of Git Large File Storage (LFS). Check your LFS usage by referring to the <a href="https://docs.github.com/en/billing/managing-billing-for-git-large-file-storage/viewing-your-git-large-file-storage-usage">GitHub</a> and <a href="https://docs.gitlab.com/ee/topics/git/lfs/">GitLab</a> documentation.</p>
<p>Make sure to also review your submodule configuration by going to the <code>.gitmodules</code> file in your root directory. This file needs to contain both a <code>path</code> and a <code>url</code> property.</p>
<p>Example of a valid configuration:</p>
<pre><code class="language-js">[submodule &quot;example&quot;]&#10;	path = example/path&#10;	url = git://github.com/example/repo.git&#10;</code></pre>
<p>Example of an invalid configuration:</p>
<pre><code class="language-js">[submodule &quot;example&quot;]&#10;	path = example/path&#10;</code></pre>
<p>or</p>
<pre><code class="language-js">[submodule &quot;example&quot;]&#10;        url = git://github.com/example/repo.git&#10;</code></pre>
<h3 id="building-application">Building application</h3>
<p>Possible errors in this step could be caused by faulty setup in your Pages project. Review your build command, output folder and environment variables for any incorrect configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11067.md")
</aside>
<h3 id="deploying-to-cloudflare-s-global-network">Deploying to Cloudflare's global network</h3>
<p>Possible errors in this step could be caused by incorrect Pages Functions configuration. Refer to the <a href="/pages/functions/">Functions</a> documentation for more information on Functions setup.</p>
<p>If you are not using Functions or have reviewed that your Functions configuration does not contain any errors, review the <a href="https://www.cloudflarestatus.com/">Cloudflare Status site</a> for Cloudflare network issues that could be causing the build failure.</p>
<h2 id="differences-between-pages-dev-and-custom-domains">Differences between <code>pages.dev</code> and custom domains</h2>
<p>If your custom domain is proxied (<a href="/dns/proxy-status/#benefits">orange-clouded</a>) through Cloudflare, your zone's settings, like caching, will apply.</p>
<p>If you are experiencing issues with new content not being shown, go to <strong>Rules</strong> &gt; <strong>Page Rules</strong> in the Cloudflare dashboard and check for a Page Rule with <strong>Cache Everything</strong> enabled. If present, remove this rule as Pages handles its own cache.</p>
<p>If you are experiencing errors on your custom domain but not on your <code>pages.dev</code> domain, go to <strong>DNS</strong> &gt; <strong>Records</strong> in the Cloudflare dashboard and set the DNS record for your project to be <strong>DNS Only</strong> (grey cloud). If the error persists, review your zone's configuration.</p>
<h2 id="domain-stuck-in-verification">Domain stuck in verification</h2>
<p>If your <a href="/pages/configuration/custom-domains/">custom domain</a> has not moved from the <strong>Verifying</strong> stage in the Cloudflare dashboard, refer to the following debugging steps.</p>
<h3 id="blocked-http-validation">Blocked HTTP validation</h3>
<p>Pages uses HTTP validation and needs to hit an HTTP endpoint during validation. If another Cloudflare product is in the way (such as <a href="/cloudflare-one/access-controls/policies/">Access</a>, <a href="/rules/url-forwarding/">a redirect</a>, <a href="/workers/">a Worker</a>, etc.), validation cannot be completed.</p>
<p>To check this, run a <code>curl</code> command against your domain hitting <code>/.well-known/acme-challenge/randomstring</code>. For example:</p>
<pre><code class="language-sh">curl -s -o /dev/null -D - https://example.com/.well-known/acme-challenge/randomstring&#10;</code></pre>
<pre><code class="language-sh">&#10;HTTP/2 302&#10;date: Mon, 03 Apr 2023 08:37:39 GMT&#10;location: https://example.cloudflareaccess.com/cdn-cgi/access/login/example.com?kid=...&amp;redirect_url=%2F.well-known%2Facme-challenge%2F...&#10;access-control-allow-credentials: true&#10;cache-control: private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0&#10;server: cloudflare&#10;cf-ray: 7b1ffdaa8ad60693-MAN&#10;</code></pre>
<p>In the example above, you are redirecting to Cloudflare Access (as shown by the <code>Location</code> header). In this case, you need to disable Access over the domain until the domain is verified. After the domain is verified, Access can be re-enabled.</p>
<p>You will need to do the same kind of thing for Redirect Rules or a Worker example too.</p>
<p>Refer to the <a href="/ssl/edge-certificates/changing-dcv-method/troubleshooting/">Troubleshooting Domain control validation (DCV)</a> article for more details.</p>
<h3 id="missing-caa-records">Missing CAA records</h3>
<p>If nothing is blocking the HTTP validation, then you may be missing Certification Authority Authorization (CAA) records. This is likely if you have disabled <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a> or use an external provider.</p>
<p>To check this, run a <code>dig</code> on the custom domain's apex (or zone, if this is a <a href="/dns/zone-setups/subdomain-setup/">subdomain zone</a>). For example:</p>
<pre><code class="language-sh">dig CAA example.com&#10;</code></pre>
<pre><code class="language-sh">&#10;; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; CAA example.com&#10;;; global options: +cmd&#10;;; Got answer:&#10;;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 59018&#10;;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1&#10;&#10;;; OPT PSEUDOSECTION:&#10;; EDNS: version: 0, flags:; udp: 4096&#10;;; QUESTION SECTION:&#10;;example.com.		IN	CAA&#10;&#10;;; ANSWER SECTION:&#10;example.com.	300	IN	CAA	0 issue &quot;amazon.com&quot;&#10;&#10;;; Query time: 92 msec&#10;;; SERVER: 127.0.2.2#53(127.0.2.2)&#10;;; WHEN: Mon Apr 03 10:15:51 BST 2023&#10;;; MSG SIZE  rcvd: 76&#10;</code></pre>
<p>In the above example, there is only a single CAA record which is allowing Amazon to issue certificates.</p>
<p>To resolve this, you will need to add the following CAA records which allows all of the Certificate Authorities (CAs) Cloudflare uses to issue certificates:</p>
<pre><code>example.com.            300     IN      CAA     0 issue &quot;letsencrypt.org&quot;&#10;example.com.            300     IN      CAA     0 issue &quot;pki.goog; cansignhttpexchanges=yes&quot;&#10;example.com.            300     IN      CAA     0 issue &quot;ssl.com&quot;&#10;example.com.            300     IN      CAA     0 issuewild &quot;letsencrypt.org&quot;&#10;example.com.            300     IN      CAA     0 issuewild &quot;pki.goog; cansignhttpexchanges=yes&quot;&#10;example.com.            300     IN      CAA     0 issuewild &quot;ssl.com&quot;&#10;</code></pre>
<h3 id="zone-holds">Zone holds</h3>
<p>A <a href="/fundamentals/account/account-security/zone-holds/">zone hold</a> will prevent Pages from adding a custom domain for a hostname under a zone hold.</p>
<p>To add a custom domain for a hostname with a zone hold, temporarily <a href="/fundamentals/account/account-security/zone-holds/#release-zone-holds">release the zone hold</a> during the custom domain setup process.</p>
<p>Once the custom domain has been successfully completed, you may <a href="/fundamentals/account/account-security/zone-holds/#enable-zone-holds">reinstate the zone hold</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="still-having-issues">Still having issues</h3>
@markup("md", "content/.markup/bodies/11066.md")
</aside>
<h3 id="missing-index-html-on-the-root-pages-dev-url">Missing <code>index.html</code> on the root <code>pages.dev</code> URL</h3>
<p>If you see a <code>404</code> error on the root <code>pages.dev</code> URL (<code>example.pages.dev</code>), you are likely missing an <code>index.html</code> file in your project.</p>
<p>Upload an <code>index.html</code> file to resolve this issue.</p>
<h2 id="resources">Resources</h2>
<p>If you need additional guidance on build errors, contact your Cloudflare account team (Enterprise) or refer to the <a href="/support/contacting-cloudflare-support/">Support Center</a> for guidance on contacting Cloudflare Support.</p>
<p>You can also ask questions in the Pages section of the <a href="https://discord.com/invite/cloudflaredev">Cloudflare Developers Discord</a>.</p>
