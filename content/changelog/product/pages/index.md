<h1 id="changelog">Changelog</h1>

<h2 id="pages-now-skips-superseded-queued-builds"><a href="/changelog/post/2026-08-11-skip-superseded-builds/">Pages now skips superseded queued builds</a></h2>
<p><em>2026-08-11</em></p>
<p>Pages now automatically skips a queued build when a newer build for the same project, branch, and deployment target is also queued.</p>


<h2 id="increased-pages-file-limit-to-100-000-for-paid-plans"><a href="/changelog/post/2026-01-23-pages-file-limit-increase/">Increased Pages file limit to 100,000 for paid plans</a></h2>
<p><em>2026-01-23</em></p>
<p>Paid plans can now have up to 100,000 files per Pages site, increased from the previous limit of 20,000 files.</p>
<p>To enable this increased limit, set the environment variable <code>PAGES_WRANGLER_MAJOR_VERSION=4</code> in your Pages project settings.</p>
<p>The Free plan remains at 20,000 files per site.</p>
<p>For more details, refer to the <a href="/pages/platform/limits/#files">Pages limits documentation</a>.</p>


<h2 id="cloudflare-pages-builds-now-provide-node-js-v22-by-default"><a href="/changelog/post/2025-05-30-pages-build-image-v3/">Cloudflare Pages builds now provide Node.js v22 by default</a></h2>
<p><em>2025-05-30T00:00:00+00:00</em></p>
<p>When you use the built-in build system that is part of <a href="/pages/">Cloudflare Pages</a>, the <a href="/pages/configuration/build-image/">Build Image</a> now includes Node.js v22. Previously, Node.js v18 was provided by default, and Node.js v18 is now end-of-life (EOL).</p>
<p>If you are creating a new Pages project, the new V3 build image that includes Node.js v22 will be used by default. If you have an existing Pages project, you can update to the latest build image by navigating to Settings &gt; Build &amp; deployments &gt; Build system version in the Cloudflare dashboard for a specific Pages project.</p>
<p>Note that you can always specify a particular version of Node.js or other built-in dependencies by <a href="/pages/configuration/build-image/#override-default-versions">setting an environment variable</a>.</p>
<p>For more, refer to the <a href="/pages/configuration/build-image">developer docs for Cloudflare Pages builds</a></p>


<h2 id="new-managed-waf-rule-for-next-js-cve-2025-29927"><a href="/changelog/post/2025-03-22-next-js-vulnerability-waf/">New Managed WAF rule for Next.js CVE-2025-29927.</a></h2>
<p><em>2025-03-22</em></p>
<p><strong>Update: Mon Mar 24th, 11PM UTC</strong>: Next.js has made further changes to address a smaller vulnerability introduced in the patches made to its middleware handling. Users should upgrade to Next.js versions <code>15.2.4</code>, <code>14.2.26</code>, <code>13.5.10</code> or <code>12.3.6</code>. <strong>If you are unable to immediately upgrade or are running an older version of Next.js, you can enable the WAF rule described in this changelog as a mitigation</strong>.</p>
<p><strong>Update: Mon Mar 24th, 8PM UTC</strong>: Next.js has now <a href="https://github.com/advisories/GHSA-f82v-jwr5-mffw">backported the patch for this vulnerability</a> to cover Next.js v12 and v13. Users on those versions will need to patch to <code>13.5.9</code> and <code>12.3.5</code> (respectively) to mitigate the vulnerability.</p>
<p><strong>Update: Sat Mar 22nd, 4PM UTC</strong>: We have changed this WAF rule to opt-in only, as sites that use auth middleware with third-party auth vendors were observing failing requests.</p>
<p><strong>We strongly recommend updating your version of Next.js (if eligible)</strong> to the patched versions, as your app will otherwise be vulnerable to an authentication bypass attack regardless of auth provider.</p>
<h4 id="2025-03-22-next-js-vulnerability-waf-enable-the-managed-rule-strongly-recommended">Enable the Managed Rule (strongly recommended)</h4>
<p>This rule is opt-in only for sites on the Pro plan or above in the <a href="/waf/managed-rules/">WAF managed ruleset</a>.</p>
<p>To enable the rule:</p>
<ol>
<li>Head to Security &gt; WAF &gt; Managed rules in the Cloudflare dashboard for the zone (website) you want to protect.</li>
<li>Click the three dots next to <strong>Cloudflare Managed Ruleset</strong> and choose <strong>Edit</strong></li>
<li>Scroll down and choose <strong>Browse Rules</strong></li>
<li>Search for <strong>CVE-2025-29927</strong> (ruleId: <code>34583778093748cc83ff7b38f472013e</code>)</li>
<li>Change the <strong>Status</strong> to <strong>Enabled</strong> and the <strong>Action</strong> to <strong>Block</strong>. You can optionally set the rule to Log, to validate potential impact before enabling it. Log will not block requests.</li>
<li>Click <strong>Next</strong></li>
<li>Scroll down and choose <strong>Save</strong></li>
</ol>
<p>This will enable the WAF rule and block requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version.</p>
<h4 id="2025-03-22-next-js-vulnerability-waf-create-a-waf-rule-manual">Create a WAF rule (manual)</h4>
<p>For users on the Free plan, or who want to define a more specific rule, you can create a <a href="/waf/custom-rules/create-dashboard/">Custom WAF rule</a> to block requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version.</p>
<p>To create a custom rule:</p>
<ol>
<li>Head to Security &gt; WAF &gt; Custom rules in the Cloudflare dashboard for the zone (website) you want to protect.</li>
<li>Give the rule a name - e.g. <code>next-js-CVE-2025-29927</code></li>
<li>Set the matching parameters for the rule match any request where the <code>x-middleware-subrequest</code> header <code>exists</code> per the rule expression below.</li>
</ol>
<pre><code class="language-sh">(len(http.request.headers[&quot;x-middleware-subrequest&quot;]) &gt; 0)&#10;</code></pre>
<ol start="4">
<li>Set the action to 'block'. If you want to observe the impact before blocking requests, set the action to 'log' (and edit the rule later).</li>
<li><strong>Deploy</strong> the rule.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/workers/waf-rule-cve-2025-29927.png" alt="Next.js CVE-2025-29927 WAF rule" /></p>
<h4 id="2025-03-22-next-js-vulnerability-waf-next-js-cve-2025-29927">Next.js CVE-2025-29927</h4>
<p>We've made a WAF (Web Application Firewall) rule available to all sites on Cloudflare to protect against the <a href="https://github.com/advisories/GHSA-f82v-jwr5-mffw">Next.js authentication bypass vulnerability</a> (<code>CVE-2025-29927</code>) published on March 21st, 2025.</p>
<p><strong>Note</strong>: This rule is not enabled by default as it blocked requests across sites for specific authentication middleware.</p>
<ul>
<li>This managed rule protects sites using Next.js on Workers and Pages, as well as sites using Cloudflare to protect Next.js applications hosted elsewhere.</li>
<li>This rule has been made available (but not enabled by default) to all sites as part of our <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">WAF Managed Ruleset</a> and blocks requests that attempt to bypass authentication in Next.js applications.</li>
<li>The vulnerability affects almost all Next.js versions, and has been fully patched in Next.js <code>14.2.26</code> and <code>15.2.4</code>. Earlier, interim releases did not fully patch this vulnerability.</li>
<li><strong>Users on older versions of Next.js (<code>11.1.4</code> to <code>13.5.6</code>) did not originally have a patch available</strong>, but this the patch for this vulnerability and a subsequent additional patch have been backported to Next.js versions <code>12.3.6</code> and <code>13.5.10</code> as of Monday, March 24th. Users on Next.js v11 will need to deploy the stated workaround or enable the WAF rule.</li>
</ul>
<p>The managed WAF rule mitigates this by blocking <em>external</em> user requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version, but we recommend users using Next.js 14 and 15 upgrade to the patched versions of Next.js as an additional mitigation.</p>


<h2 id="smart-placement-is-smarter-about-running-workers-and-pages-functions-in-the-best-locations"><a href="/changelog/post/2025-03-22-smart-placement-stablization/">Smart Placement is smarter about running Workers and Pages Functions in the best locations</a></h2>
<p><em>2025-03-22</em></p>
<p><a href="/workers/configuration/placement/">Smart Placement</a> is a unique Cloudflare feature that can make decisions to move your Worker to run in a more optimal location (such as closer to a database). Instead of always running in the default location (the one closest to where the request is received), Smart Placement uses certain “heuristics” (rules and thresholds) to decide if a different location might be faster or more efficient.</p>
<p>Previously, if these heuristics weren't consistently met, your Worker would revert to running in the default location—even after it had been optimally placed. This meant that if your Worker received minimal traffic for a period of time, the system would reset to the default location, rather than remaining in the optimal one.</p>
<p>Now, once Smart Placement has identified and assigned an optimal location, temporarily dropping below the heuristic thresholds will not force a return to default locations. For example in the previous algorithm, a drop in requests for a few days might return to default locations and heuristics would have to be met again. This was problematic for workloads that made requests to a geographically located resource every few days or longer. In this scenario, your Worker would never get placed optimally. This is no longer the case.</p>


<h2 id="retry-pages-workers-builds-directly-from-github"><a href="/changelog/post/2025-03-17-rerun-build/">Retry Pages & Workers Builds Directly from GitHub</a></h2>
<p><em>2025-03-17</em></p>
<p>You can now retry your Cloudflare Pages and Workers builds directly from GitHub. No need to switch to the Cloudflare Dashboard for a simple retry!</p>
<p>Let\u2019s say you push a commit, but your build fails due to a spurious error like a network timeout. Instead of going to the Cloudflare Dashboard to manually retry, you can now rerun the build with just a few clicks inside GitHub, keeping you inside your workflow.</p>
<p>For Pages and Workers projects connected to a GitHub repository:</p>
<ol>
<li>When a build fails, go to your GitHub repository or pull request</li>
<li>Select the failed Check Run for the build</li>
<li>Select &quot;Details&quot; on the Check Run</li>
<li>Select &quot;Rerun&quot; to trigger a retry build for that commit</li>
</ol>
<p>Learn more about <a href="/pages/configuration/git-integration/github-integration/">Pages Builds</a> and <a href="/workers/ci-cd/builds/git-integration/github-integration/">Workers Builds</a>.</p>



