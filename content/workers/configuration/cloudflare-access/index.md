<p>With Cloudflare Access, you can restrict who is authorized to access your application. You decide who is approved, and every request is checked before your Worker runs. Approved visitors are let through, while everyone else is shown a login page or blocked.</p>
<p>You can protect:</p>
<ul>
<li><strong>A single application</strong>: require sign-in on its preview URLs, production URLs, or both.</li>
<li><strong>All Workers in your account</strong>: protect every existing and newly created Worker by default.</li>
<li><strong>Specific custom domains and hostnames</strong>: restrict access at the hostname or route level.</li>
</ul>
<h2 id="before-you-start">Before you start</h2>
<p>To use Access with Workers, you need:</p>
<ul>
<li>Zero Trust enabled on your account. If Zero Trust is not turned on, complete <a href="/cloudflare-one/setup/">Zero Trust setup</a> first, then return to the Workers dashboard.</li>
<li>Permission to manage Workers and Access applications.</li>
</ul>
<h2 id="choose-what-to-protect">Choose what to protect</h2>
<table>
<thead>
<tr>
<th>I want to protect...</th>
<th>Section</th>
<th>API destination type</th>
</tr>
</thead>
<tbody>
<tr>
<td>Preview deployments for <strong>all Workers</strong></td>
<td><a href="#protect-all-workers">Protect all Workers</a></td>
<td><code>all_preview_workers</code></td>
</tr>
<tr>
<td>Production and preview deployments for <strong>all Workers</strong></td>
<td><a href="#protect-all-workers">Protect all Workers</a></td>
<td><code>all_workers</code></td>
</tr>
<tr>
<td>Preview deployments for <strong>one Worker</strong></td>
<td><a href="#protect-one-worker">Protect one Worker</a></td>
<td><code>preview_worker</code></td>
</tr>
<tr>
<td>Production and preview deployments for <strong>one Worker</strong></td>
<td><a href="#protect-one-worker">Protect one Worker</a></td>
<td><code>worker</code></td>
</tr>
<tr>
<td>A specific hostname — can be <code>workers.dev</code>, a Custom Domain, or a path</td>
<td><a href="#protect-a-specific-hostname-custom-domain-or-path">Protect a specific hostname, Custom Domain, or path</a></td>
<td>Self-hosted application domain</td>
</tr>
</tbody>
</table>
<h2 id="protect-all-workers">Protect all Workers</h2>
<p>Require sign-in on every Worker in your account, including Workers you deploy in the future. You can require sign-in on only preview deployments, or on both production and preview deployments.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16661.md")
</div></div>
<h2 id="protect-one-worker">Protect one Worker</h2>
<p>Require sign-in on a single Worker. This automatically protects every domain associated with the Worker, including its routes, Custom Domains, <code>workers.dev</code> hostname, and previews. You can require sign-in on only preview deployments, or on both production and preview deployments.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="websocket-limitation">WebSocket limitation</h3>
@markup("md", "content/.markup/bodies/16657.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16665.md")
</div></div>
<h2 id="protect-a-specific-hostname-custom-domain-or-path">Protect a specific hostname, Custom Domain, or path</h2>
<p>Use hostname-based Access when only a specific URL that routes to your Worker should require sign-in, such as a <code>workers.dev</code> hostname, a Custom Domain, a subdomain, or a path. Hostname-based Access protects only that exact URL, whereas <a href="#protect-one-worker">protecting a Worker</a> protects the entire Worker regardless of how it is accessed. For example with hostname-based Access, you can protect <code>my-worker.example.workers.dev</code>, <code>admin.example.com</code>, or a single path such as <code>example.com/login</code> to make only part of your Worker private.</p>
<p>In both the dashboard and the API, you protect a hostname or path by creating a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a> and using the hostname or path as the application domain.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16668.md")
</div></div>
<h2 id="make-a-worker-public-when-all-workers-are-protected">Make a Worker public when all Workers are protected</h2>
<p>If account-level Access protects all Workers, you can make a specific Worker public by adding a Worker-level bypass. A bypass means Access does not require sign-in for that Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16656.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16672.md")
</div></div>
<h2 id="policy-options">Policy options</h2>
<p>When you turn on Access, choose who can sign in. The same policy options are available whether you protect all Workers or one Worker.</p>
<table>
<thead>
<tr>
<th>Policy option</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare account</td>
<td>Allows members of this Cloudflare account to sign in. Use this option when access should be limited to people who already belong to the account.</td>
</tr>
<tr>
<td>Email domain</td>
<td>Allows anyone with a verified email address at the domain you enter, such as <code>example.com</code>. Use this option when access should be available to people from a company or organization, even if they are not Cloudflare account members.</td>
</tr>
</tbody>
</table>
<p>You can add one or more policies. Visitors who match any selected policy can sign in.</p>
<p>For advanced policy configuration, such as multiple identity providers, device posture rules, service tokens, complex policy ordering, or custom login or block pages, edit the Access application in Zero Trust after you create it. For the full set of options, refer to <a href="/cloudflare-one/access-controls/policies/">Access policies</a>.</p>
<h2 id="read-authenticated-user-identity-with-ctx-access">Read authenticated user identity with ctx.access</h2>
<p>When Cloudflare Access authenticates a request that directly invokes your Worker, the Worker can read the signed-in user's identity — including email, groups, device posture, and <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#user-identity">more identity fields</a> — through <code>ctx.access</code>. No extra configuration or JWT parsing is required.</p>
<p>Use this to personalize responses, enforce fine-grained permissions, or log activity per user.</p>
<p><code>ctx.access</code> is <code>undefined</code> if Access did not authenticate the request.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16673.md")
</div>
<h3 id="ctx-access-limitations"><code>ctx.access</code> limitations</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16655.md")
</aside>
<h2 id="test-ctx-access-locally">Test ctx.access locally</h2>
<p>When developing locally with <code>wrangler dev</code> or the Cloudflare Vite Plugin, you can simulate authenticated Cloudflare Access identities without deploying or going through an Access login flow.</p>
<p>Add a <code>dev</code> block inside the <code>access</code> configuration in your <code>wrangler.jsonc</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16674.md")
</div>
<ul>
<li><code>aud</code> (required) — your Access application's audience tag, available as <code>ctx.access.aud</code>. Wrangler will not start without it.</li>
<li><code>identity</code> (optional) — simulates the authenticated user's identity claims (email, name, groups, and so on) returned by <code>ctx.access.getIdentity()</code>. Include it if your Worker reads user identity. Omit it if your Worker only checks whether Access is enabled.</li>
</ul>
<p>To test as a different user, change the identity fields and restart. To test unauthenticated requests, remove the <code>dev</code> block — <code>ctx.access</code> will be <code>undefined</code>, just as it would be for a request that did not go through Access in production.</p>
<h3 id="example-worker">Example Worker</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16675.md")
</div>
<p>With this configuration, visiting <code>localhost:8787</code> would return <code>Hello, admin@example.com</code>.</p>
<h3 id="identity-fields">Identity fields</h3>
<p>The identity object accepts any fields that match the production Access identity shape. For the full list, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">Application token — User identity</a>.</p>
<h2 id="disable-access">Disable Access</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16678.md")
</div></div>
<h2 id="understand-access-hierarchy">Understand Access hierarchy</h2>
<p>A Worker can be protected by more than one Access rule. When multiple rules could apply to the same request, the most specific rule takes effect first:</p>
<ol>
<li><strong>Hostname or path-based Access</strong>: Applies first when the request matches that hostname or path, such as <code>admin.example.com</code> or <code>example.com/login</code>.</li>
<li><strong>Worker-level Access</strong>: Applies next for the selected Worker across its routes, Custom Domains, <code>workers.dev</code> hostname, and previews.</li>
<li><strong>Account-level Worker Access</strong>: Applies last as the fallback for all Workers or all Worker previews on the account.</li>
</ol>
<p>For example, if a Worker has both account-level Access and a Worker-level rule, the Worker-level rule controls that Worker. If a matching hostname or path-based Access app also exists, that hostname or path rule controls the matching URL.</p>
<p>If you remove a more specific rule, a broader rule may still protect the Worker. For example, removing Worker-level Access can reveal account-level Access underneath.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/api/resources/zero_trust/subresources/access/subresources/applications/methods/create/">Access applications API</a></li>
<li><a href="/cloudflare-one/access-controls/policies/">Access policies</a></li>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Self-hosted Access applications</a></li>
<li><a href="/workers/configuration/routing/">Routes and domains</a></li>
<li><a href="/workers/configuration/previews/">Preview URLs</a></li>
</ul>
