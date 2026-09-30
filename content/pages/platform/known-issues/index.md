---
cp9:
  canonical: https://developers.cloudflare.com/pages/platform/known-issues/
  description: Current bugs and limitations for Cloudflare Pages builds, deployments, and configuration.
  full_title: Known issues · Cloudflare Pages docs
  head_html: <title>Known issues · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Current bugs and limitations for Cloudflare Pages builds, deployments, and configuration."><link rel="canonical" href="https://developers.cloudflare.com/pages/platform/known-issues/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/platform/known-issues/index.md"><meta property="og:title" content="Known issues · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Current bugs and limitations for Cloudflare Pages builds, deployments, and configuration."><meta property="og:url" content="https://developers.cloudflare.com/pages/platform/known-issues/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/platform/known-issues/#page","headline":"Known issues \u00b7 Cloudflare Pages docs","description":"Current bugs and limitations for Cloudflare Pages builds, deployments, and configuration.","url":"https://developers.cloudflare.com/pages/platform/known-issues/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/platform/known-issues/
  schema: 1
---
<p>Here are some known bugs and issues with Cloudflare Pages:</p>
<h2 id="builds-and-deployment">Builds and deployment</h2>
<ul>
<li>
<p>GitHub and GitLab are currently the only supported platforms for automatic CI/CD builds. <a href="/pages/get-started/direct-upload/">Direct Upload</a> allows you to integrate your own build platform or upload from your local computer.</p>
</li>
<li>
<p>Incremental builds are currently not supported in Cloudflare Pages.</p>
</li>
<li>
<p>Uploading a <code>/functions</code> directory through the dashboard's Direct Upload option does not work (refer to <a href="/pages/get-started/direct-upload/#functions">Using Functions in Direct Upload</a>).</p>
</li>
<li>
<p>Commits/PRs from forked repositories will not create a preview. Support for this will come in the future.</p>
</li>
</ul>
<h2 id="git-configuration">Git configuration</h2>
<ul>
<li>If you deploy using the Git integration, you cannot switch to Direct Upload later. However, if you already use a Git-integrated project and do not want to trigger deployments every time you push a commit, you can <a href="/pages/configuration/git-integration/#disable-automatic-deployments">disable/pause automatic deployments</a>. Alternatively, you can delete your Pages project and create a new one pointing at a different repository if you need to update it.</li>
</ul>
<h2 id="build-configuration">Build configuration</h2>
<ul>
<li>
<p><code>*.pages.dev</code> subdomains currently cannot be changed. If you need to change your <code>*.pages.dev</code> subdomain, delete your project and create a new one.</p>
</li>
<li>
<p>Hugo builds automatically run an old version. To run the latest version of Hugo (for example, <code>0.101.0</code>), you will need to set an environment variable. Set <code>HUGO_VERSION</code> to <code>0.101.0</code> or the Hugo version of your choice.</p>
</li>
<li>
<p>By default, Cloudflare uses Node <code>12.18.0</code> in the Pages build environment. If you need to use a newer Node version, refer to the <a href="/pages/configuration/build-configuration/">Build configuration page</a> for configuration options.</p>
</li>
<li>
<p>For users migrating from Netlify, Cloudflare does not support Netlify's Forms feature. <a href="/pages/functions/">Pages Functions</a> are available as an equivalent to Netlify's Serverless Functions.</p>
</li>
</ul>
<h2 id="custom-domains">Custom Domains</h2>
<ul>
<li>
<p>It is currently not possible to add a custom domain with</p>
<ul>
<li>a wildcard, for example, <code>*.domain.com</code>.</li>
<li>a Worker already routed on that domain.</li>
</ul>
</li>
<li>
<p>It is currently not possible to add a custom domain with a Cloudflare Access policy already enabled on that domain.</p>
</li>
<li>
<p>Cloudflare's Load Balancer does not work with <code>*.pages.dev</code> projects; an <code>Error 1000: DNS points to prohibited IP</code> will appear.</p>
</li>
<li>
<p>When adding a custom domain, the domain will not verify if Cloudflare cannot validate a request for an SSL certificate on that hostname. In order for the SSL to validate, ensure Cloudflare Access or a Cloudflare Worker is allowing requests to the validation path: <code>http://{domain_name}/.well-known/acme-challenge/*</code>.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificates</a> cannot be used with Cloudflare Pages due to Cloudflare for SaaS's <a href="/ssl/reference/certificate-and-hostname-priority/">certificate prioritization</a>.</p>
</li>
</ul>
<h2 id="pages-functions">Pages Functions</h2>
<ul>
<li>
<p><a href="/pages/functions/">Functions</a> does not currently support adding/removing polyfills, so your bundler (for example, webpack) may not run.</p>
</li>
<li>
<p><code>passThroughOnException()</code> is not currently available for Advanced Mode Pages Functions (Pages Functions which use an <code>_worker.js</code> file).</p>
</li>
<li>
<p><code>passThroughOnException()</code> is not currently as resilient as it is in Workers. We currently wrap Pages Functions code in a <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch">try...catch</a> block and fallback to calling <code>env.ASSETS.fetch()</code>. This means that any critical failures (such as exceeding CPU time or exceeding memory) may still throw an error.</p>
</li>
</ul>
<h2 id="enable-access-on-your-pages-dev-domain">Enable Access on your <code>*.pages.dev</code> domain</h2>
<p>If you would like to enable <a href="https://www.cloudflare.com/teams-access/">Cloudflare Access</a>] for your preview deployments and your <code>*.pages.dev</code> domain, you must:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Enable access policy**.
4. Select **Manage** on the Access policy created for your preview deployments.
5. Under **Access** > **Applications**, select your project.
6. Select **Configure**.
7. Under **Public hostname**, in the **Subdomain** field, delete the wildcard (`*`) and select **Save**. You may need to change the **Application name** at this step to avoid an error.
<p>At this step, your <code>*.pages.dev</code> domain has been secured behind Access. To resecure your preview deployments:</p>
<ol start="8">
<li>Go back to your Pages project &gt; <strong>Settings</strong> &gt; <strong>General</strong> &gt; and reselect <strong>Enable access policy</strong>.</li>
<li>Review that two Access policies, one for your <code>*.pages.dev</code> domain and one for your preview deployments (<code>*.&lt;YOUR_SITE&gt;.pages.dev</code>), have been created.</li>
</ol>
<p>If you have a custom domain and protected your <code>*.pages.dev</code> domain behind Access, you must:</p>
<ol start="10">
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>. Select <strong>Create new application</strong> &gt; <strong>Self-hosted and private</strong>.</li>
<li>Select <strong>Add public hostname</strong> and select your custom domain from the <em>Domain</em> dropdown menu.</li>
<li>Configure your access rules to define who can reach the Access authentication page.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10874.md")
</aside>
<p>If you have an issue that you do not see listed, let the team know in the Cloudflare Workers Discord. Get your invite at <a href="https://discord.cloudflare.com">discord.cloudflare.com</a>, and share your bug report in the #pages-general channel.</p>
<h2 id="delete-a-project-with-a-high-number-of-deployments">Delete a project with a high number of deployments</h2>
<p>You may not be able to delete your Pages project if it has a high number (over 100) of deployments. The Cloudflare team is tracking this issue.</p>
<p>As a workaround, you can use <a href="/workers/wrangler/commands/pages/#pages-deployment-delete"><code>wrangler pages deployment delete</code></a> to delete deployments individually. After you delete your deployments, you will be able to delete your Pages project.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages deployment delete &lt;DEPLOYMENT_ID&gt; --project-name &lt;PROJECT_NAME&gt;&#10;</code></pre>
<p>Use the <code>--force</code> flag to skip the confirmation prompt and to force deletion of aliased deployments.</p>
<p>To delete <em>all</em> your deployments for a particular project name, you could run the following shell script:</p>
<pre tabindex="0"><code class="language-sh">prod_id=&quot;&quot;&#10;while :; do&#10;  ids=$(npx wrangler pages deployment list --project-name &lt;PROJECT_NAME&gt; --json | jq -r &#x27;.[].Id&#x27;)&#10;  to_delete=$(echo &quot;$ids&quot; | grep -v -F -x &quot;$prod_id&quot; | grep .)&#10;  [ -z &quot;$to_delete&quot; ] &amp;&amp; { echo &quot;Done. Production: $prod_id&quot;; break; }&#10;  echo &quot;Deleting $(echo &quot;$to_delete&quot; | wc -l | tr -d &#x27; &#x27;) deployments...&quot;&#10;  while IFS= read -r id; do&#10;    if ! npx wrangler pages deployment delete &quot;$id&quot; --project-name &lt;PROJECT_NAME&gt; --force 2&gt;&amp;1 | tee /tmp/wrangler-del.log | grep -q &quot;Successfully deleted&quot;; then&#10;      grep -q &quot;active production deployment&quot; /tmp/wrangler-del.log &amp;&amp; prod_id=&quot;$id&quot;&#10;    fi&#10;  done &lt;&lt;&lt; &quot;$to_delete&quot;&#10;done&#10;</code></pre>
<p>Note that this will not delete the active production deployment if one exists.</p>
<h2 id="use-pages-as-origin-in-cloudflare-load-balancer">Use Pages as Origin in Cloudflare Load Balancer</h2>
<p><a href="/load-balancing/">Cloudflare Load Balancing</a> will not work without the host header set. To use a Pages project as target, make sure to select <strong>Add host header</strong> when <a href="/load-balancing/pools/create-pool/#create-a-pool">creating a pool</a>, and set both the host header value and the endpoint address to your <code>pages.dev</code> domain.</p>
<p>Refer to <a href="/load-balancing/pools/cloudflare-pages-origin/">Use Cloudflare Pages as origin</a> for a complete tutorial.</p>
