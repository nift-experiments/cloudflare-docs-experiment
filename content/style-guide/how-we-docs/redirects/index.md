<p>As your content changes (and it will change), <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14605.md")
</div> preserve continuity for your users and (friendly) bots.
<p>The most obvious part of this is the user experience. If you click a link in the dashboard or use a bookmarked URL, you trust that it's taking you to the right place. Not a <code>404</code> page or the wrong page, but the right page. Redirects help direct users to the right place.</p>
<p>The same applies to the automated experience. If you move a page without redirects, you are losing the historical search authority that Google and other search engines use to rank your page.</p>
<hr />
<h2 id="how-we-add-redirects">How we add redirects</h2>
<h3 id="cloudflare-workers-primary">Cloudflare Workers (primary)</h3>
<p>Our primary method takes advantage of <a href="/workers/static-assets/redirects/">Workers Static Assets</a>, defining redirects in a <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/public/__redirects">plain text file</a> in our GitHub repo.</p>
<p>This setup allows us to use the same workflow for redirects as for any other documentation change. We implement a redirect in the same pull request as the content change and can test these changes in our preview branches. For maintenance, we try to keep these redirects <a href="#organize-your-redirects">organized</a> by product and then — within each product — organized alphabetically.</p>
<p>We also love the flexibility provided by the <a href="/workers/static-assets/redirects/#advanced-redirects">Pages syntax</a>.</p>
<h3 id="bulk-redirects-secondary">Bulk redirects (secondary)</h3>
<p>In certain situations, we also use <a href="/rules/url-forwarding/bulk-redirects/">Bulk redirects</a>. We use this strategy sparing because having redirects in multiple places increases the cognitive load and potential confusion of making a change.</p>
<p>Normally, bulk redirects only come up when another team is adding a large number of individual redirects to our site, such as when all of our previous <code>support.cloudflare.com</code> content was migrated and needed individualized redirects per locale.</p>
<p>We use this method when the contributors are outside of our team and when the total number of redirects is so large that it would clutter our <code>__redirects</code> file and count against our <a href="/workers/static-assets/redirects/#surpass-_redirects-limits">limit for redirects</a>.</p>
<hr />
<h2 id="when-we-add-redirects">When we add redirects</h2>
<p>Our team adds redirects in two situations: during the course of normal content and as needed based on data.</p>
<h3 id="during-content-work">During content work</h3>
<p>During normal content work, you want to add redirects when you do the following to a page:</p>
<ul>
<li>Change any part of the URL (filename, folder).</li>
<li>Delete the page.</li>
</ul>
<p>We have some automation to help <a href="#potential-redirects">flag needed redirects</a>.</p>
<h3 id="based-on-data">Based on data</h3>
<p>Another time to add redirects is when you see a lot of <code>404</code> response codes on certain paths of your docs site. These <code>404</code> responses might be due to a missing redirect or mistyped link.</p>
<p>We identify these status codes either through our <a href="/analytics/account-and-zone-analytics/zone-analytics/">Cloudflare analytics</a> (ad hoc) or <a href="/logs/logpush/">Logpush job</a> (more thorough, quarterly).</p>
<hr />
<h2 id="how-we-automate-redirects">How we automate redirects</h2>
<p>We have two automations in GitHub to help with redirects.</p>
<h3 id="infinite-redirects">Infinite redirects</h3>
<p>An infinite redirect is when two pages keep redirecting to each other, trapping users in an infitnite loop that will crash their browser.</p>
<p>Because that's just a terrible experience, we explicitly check for that as part of our <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/.github/workflows/ci.yml#L62-L63">required <code>CI</code> GitHub action</a>.</p>
<p>We trigger this check <em>after</em> we build our site. What it does it then call <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/bin/validate-redirects.ts"><code>validate-redirects.ts</code></a>, which fails on:</p>
<ul>
<li>Infinite redirects</li>
<li>Duplicate redirects</li>
<li>Redirect targets with anchor links in them</li>
</ul>
<details class="nb-details"><summary>validate-redirects.ts</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14606.md")
</div></details>
<h3 id="potential-redirects">Potential redirects</h3>
<p>Contributors often struggle to know when they should add redirects. We try to help them by <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/.github/workflows/comment-changed-filenames.yml">adding a comment</a> to any pull requests that modify or delete content file paths.</p>
<p><img src="/assets/upstream/images/style-guide/how-we-docs/redirects-github.png" alt="GitHub Actions redirect comment" /></p>
<hr />
<h2 id="other-guidance">Other guidance</h2>
<h3 id="organize-your-redirects">Organize your redirects</h3>
<p>As much as you can, try to organize your redirects into logical groups (products, alphabetical order). This process helps prevent duplicate redirects, as well as identifying specific ones you might be looking for.</p>
<p>In our <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/public/__redirects"><code>__redirects</code> file</a>, we use extensive comments, separating different product areas. We also try, as much as we can, to keep the redirects in alphabetical order within a section.</p>
<p>We used to apply a similar principle to <a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirect lists</a> (when that was our primary method). We created lists that grouped together similar products and labeled them as such, so it was easier to find which redirect you were looking for.</p>
<h3 id="know-what-you-can-redirect">Know what you can redirect</h3>
<p>At the server level, you can trigger a redirect on a URL path (<code>/page/</code>), but not a fragment (<code>/page/#fragment</code>).</p>
<p>You can redirect a page to a fragment, however (<code>/page1/</code> to <code>/page2/#fragment</code>).</p>
<h3 id="avoid-redirect-chains">Avoid redirect chains</h3>
<p>If possible, have all redirects send your users directly to their destination instead of chaining together redirects.</p>
<p>Otherwise, you can have the following situation:</p>
<pre><code class="language-txt">Page 1 --Redirect-&gt; Page 2 --Redirect-&gt; Page 3 --Redirect-&gt; Page 4&#10;</code></pre>
<p>Redirect chains are bad because they:</p>
<ul>
<li>Slow down the user experience.</li>
<li>Increase the likelihood of unintentional outcomes (infinite redirects, missing redirects, incorrect redirects).</li>
</ul>
<p>A way to avoid this outcome is by continually updating the destinations of previous redirects. For example, let's say you changed the name of this page to <code>/style-guide/how-we-docs/redirect-guidance/</code>.</p>
<p>In the pull request to update your redirects file, you would want to update the existing redirect as well as adding a new redirect:</p>
<pre><code class="language-diff">&#45; /style-guide/redirects/ /style-guide/how-we-docs/redirects/ 301&#10;&#43; /style-guide/redirects/ /style-guide/how-we-docs/redirect-guidance/ 301&#10;&#43; /style-guide/how-we-docs/redirects/ /style-guide/how-we-docs/redirect-guidance/ 301&#10;</code></pre>
