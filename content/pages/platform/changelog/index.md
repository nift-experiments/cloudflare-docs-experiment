<h2 id="2025-04-18">2025-04-18</h2><strong>Action recommended - Node.js 18 end-of-life and impact on Pages Build System V2</strong><ul>
<li>If you are using <a href="/pages/configuration/build-image/">Pages Build System V2</a> for a Git-connected Pages project, note that the default Node.js version, <strong>Node.js 18</strong>, will end its LTS support on <strong>April 30, 2025</strong>.</li>
<li>Pages will not change the default Node.js version in the Build System V2 at this time, instead, we <strong>strongly recommend pinning a modern Node.js version</strong> to ensure your builds are consistent and secure.</li>
<li>You can <a href="/pages/configuration/build-image/#override-default-versions">pin any Node.js version</a> by:
<ol>
<li>Adding a <code>NODE_VERSION</code> environment variable with the desired version specified as the value.</li>
<li>Adding a <code>.node-version</code> file with the desired version specified in the file.</li>
</ol>
</li>
<li>Pinning helps avoid unexpected behavior and ensures your builds stay up-to-date with your chosen runtime. We also recommend pinning all critical tools and languages that your project relies on.</li>
</ul><h2 id="2025-02-26">2025-02-26</h2><strong>Support for pnpm 10 in build system</strong><ul>
<li>Pages build system now supports building projects that use <strong>pnpm 10</strong> as the package manager. If your build previously failed due to this unsupported version, retry your build. No config changes needed.</li>
</ul><h2 id="2024-12-19">2024-12-19</h2><strong>Cloudflare GitHub App Permissions Update</strong><ul>
<li>Cloudflare is requesting updated permissions for the <a href="https://github.com/apps/cloudflare-workers-and-pages">Cloudflare GitHub App</a> to enable features like automatically creating a repository on your GitHub account and deploying the new repository for you when getting started with a template. This feature is coming out soon to support a better onboarding experience.
<ul>
<li><strong>Requested permissions:</strong>
<ul>
<li><a href="https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-administration">Repository Administration</a> (read/write) to create repositories.</li>
<li><a href="https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-contents">Contents</a> (read/write) to push code to the created repositories.</li>
</ul>
</li>
<li><strong>Who is impacted:</strong>
<ul>
<li>Existing users will be prompted to update permissions when GitHub sends an email with subject &quot;[GitHub] Cloudflare Workers &amp; Pages is requesting updated permission&quot; on December 19th, 2024.</li>
<li>New users installing the app will see the updated permissions during the connecting repository process.</li>
</ul>
</li>
<li><strong>Action:</strong> Review and accept the permissions update to use upcoming features. <em>If you decline or take no action, you can continue connecting repositories and deploying changes via the Cloudflare GitHub App as you do today, but new features requiring these permissions will not be available.</em></li>
<li><strong>Questions?</strong> Visit <a href="https://discord.com/channels/595317990191398933/1313895851520688163">#github-permissions-update</a> in the Cloudflare Developers Discord.</li>
</ul>
</li>
</ul><h2 id="2024-10-24">2024-10-24</h2><strong>Updating Bun version to 1.1.33 in V2 build system</strong><ul>
<li>Bun version is being updated from <code>1.0.1</code> to <code>1.1.33</code> in Pages V2 build system. This is a minor version change, please see details at <a href="https://bun.sh/blog/bun-v1.1.33">Bun</a>.</li>
<li>If you wish to use a previous Bun version, you can <a href="/pages/configuration/build-image/#overriding-default-versions">override default version</a>.</li>
</ul><h2 id="2023-09-13">2023-09-13</h2><strong>Support for D1&#x27;s new storage subsystem and build error message improvements</strong><ul>
<li>Added support for D1's <a href="https://blog.cloudflare.com/d1-turning-it-up-to-11/">new storage subsystem</a>. All Git builds and deployments done with Wrangler v3.5.0 and up can use the new subsystem.</li>
<li>Builds which fail due to exceeding the <a href="https://developers.cloudflare.com/pages/platform/limits/#builds">build time limit</a> will return a proper error message indicating so rather than <code>Internal error</code>.</li>
<li>New and improved error messages for other build failures</li>
</ul><h2 id="2023-08-23">2023-08-23</h2><strong>Commit message limit increase</strong><ul>
<li>Commit messages can now be up to 384 characters before being trimmed.</li>
</ul><h2 id="2023-08-01">2023-08-01</h2><strong>Support for newer TLDs</strong><ul>
<li>Support newer TLDs such as <code>.party</code> and <code>.music</code>.</li>
</ul><h2 id="2023-07-11">2023-07-11</h2><strong>V2 build system enabled by default</strong><ul>
<li>V2 build system is now default for all new projects.</li>
</ul><h2 id="2023-07-10">2023-07-10</h2><strong>Sped up project creation</strong><ul>
<li>Sped up project creation.</li>
</ul><h2 id="2023-05-19">2023-05-19</h2><strong>Build error message improvement</strong><ul>
<li>Builds which fail due to Out of memory (OOM) will return a proper error message indicating so rather than <code>Internal error</code>.</li>
</ul><h2 id="2023-05-17">2023-05-17</h2><strong>V2 build system beta</strong><ul>
<li>The V2 build system is now available in open beta. Enable the V2 build system by going to your Pages project in the Cloudflare dashboard and selecting <strong>Settings</strong> &gt; <a href="https://dash.cloudflare.com?to=/:account/pages/view/:pages-project/settings/builds-deployments"><strong>Build &amp; deployments</strong></a> &gt; <strong>Build system version</strong>.</li>
</ul><h2 id="2023-05-16">2023-05-16</h2><strong>Support for Smart Placement</strong><ul>
<li><a href="/workers/configuration/placement/">Smart placement</a> can now be enabled for Pages within your Pages Project by going to <strong>Settings</strong> &gt; <a href="https://dash.cloudflare.com?to=/:account/pages/view/:pages-project/settings/functions"><strong>Functions</strong></a>.</li>
</ul><h2 id="2023-03-23">2023-03-23</h2><strong>Git projects can now see files uploaded</strong><ul>
<li>Files uploaded are now visible for Git projects, you can view them in the <a href="https://dash.cloudflare.com?to=/:account/pages/view/:pages-project/:pages-deployment/files">Cloudflare dashboard</a>.</li>
</ul><h2 id="2023-03-20">2023-03-20</h2><strong>Notifications for Pages are now available</strong><ul>
<li>Notifications for Pages events are now available in the <a href="https://dash.cloudflare.com?to=/:account/notifications">Cloudflare dashboard</a>. Events supported include:
<ul>
<li>Deployment started.</li>
<li>Deployment succeeded.</li>
<li>Deployment failed.</li>
</ul>
</li>
</ul><h2 id="2023-02-14">2023-02-14</h2><strong>Analytics Engine now available in Functions</strong><ul>
<li>Added support for <a href="/analytics/analytics-engine/">Analytics Engine</a>
in Functions.</li>
</ul><h2 id="2023-01-05">2023-01-05</h2><strong>Queues now available in Functions</strong><ul>
<li>Added support for <a href="/queues/">Queues</a> producer in Functions.</li>
</ul><h2 id="2022-12-15">2022-12-15</h2><strong>API messaging update</strong><p>Updated all API messaging to be more helpful.</p><h2 id="2022-12-01">2022-12-01</h2><strong>Ability to delete aliased deployments</strong><ul>
<li>Aliased deployments can now be deleted. If using the API, you will need to add the query parameter <code>force=true</code>.</li>
</ul><h2 id="2022-11-19">2022-11-19</h2><strong>Deep linking to a Pages deployment</strong><ul>
<li>You can now deep-link to a Pages deployment in the dashboard with <code>:pages-deployment</code>. An example would be <code>https://dash.cloudflare.com?to=/:account/pages/view/:pages-project/:pages-deployment</code>.</li>
</ul><h2 id="2022-11-17">2022-11-17</h2><strong>Functions GA and other updates</strong><ul>
<li>Pages functions are now GA. For more information, refer to the <a href="https://blog.cloudflare.com/pages-function-goes-ga/">blog post</a>.</li>
<li>We also made the following updates to Functions:
<ul>
<li><a href="https://dash.cloudflare.com?to=/:account/pages/view/:pages-project/analytics/production">Functions metrics</a> are now available in the dashboard.</li>
<li><a href="/pages/functions/pricing/">Functions billing</a> is now available.</li>
<li>The <a href="/workers/platform/limits/#response-limits">Unbound usage model</a> is now available for Functions.</li>
<li><a href="/pages/functions/bindings/#secrets">Secrets</a> are now available.</li>
<li>Functions tailing is now available via the <a href="https://dash.cloudflare.com?to=/:account/pages/view/:pages-project/:pages-deployment/functions">dashboard</a> or with Wrangler (<code>wrangler pages deployment tail</code>).</li>
</ul>
</li>
</ul><h2 id="2022-11-15">2022-11-15</h2><strong>Service bindings now available in Functions</strong><ul>
<li>Service bindings are now available in Functions. For more details,
refer to the <a href="/pages/functions/bindings/#service-bindings">docs</a>.</li>
</ul><h2 id="2022-11-03">2022-11-03</h2><strong>Ansi color codes in build logs</strong><p>Build log now supports ansi color codes.</p><h2 id="2022-10-05">2022-10-05</h2><strong>Deep linking to a Pages project</strong><ul>
<li>You can now deep-link to a Pages project in the dashboard with <code>:pages-project</code>. An example would be <code>https://dash.cloudflare.com?to=/:account/pages/view/:pages-project</code>.</li>
</ul><h2 id="2022-09-12">2022-09-12</h2><strong>Increased domain limits</strong><p>Previously, all plans had a maximum of 10 <a href="/pages/configuration/custom-domains/">custom domains</a> per project.</p>
<p>Now, the limits are:</p>
<ul>
<li><strong>Free</strong>: 100 custom domains.</li>
<li><strong>Pro</strong>: 250 custom domains.</li>
<li><strong>Business</strong> and <strong>Enterprise</strong>: 500 custom domains.</li>
</ul><h2 id="2022-09-08">2022-09-08</h2><strong>Support for _routes.json</strong><ul>
<li>Pages now offers support for <code>_routes.json</code>. For more details, refer
to the <a href="/pages/functions/routing/#functions-invocation-routes">documentation</a>.</li>
</ul><h2 id="2022-08-25">2022-08-25</h2><strong>Increased build log expiration time</strong><p>Build log expiration time increased from 2 weeks to 1 year.</p><h2 id="2022-08-08">2022-08-08</h2><strong>New bindings supported</strong><ul>
<li>R2 and D1 <a href="/pages/functions/bindings/">bindings</a> are now supported.</li>
</ul><h2 id="2022-07-05">2022-07-05</h2><strong>Added support for .dev.vars in wrangler pages</strong><p>Pages now supports <code>.dev.vars</code> in <code>wrangler pages</code>, which allows you to use use environmental variables during your local development without chaining <code>--env</code>s.</p>
<p>This functionality requires Wrangler v2.0.16 or higher.</p><h2 id="2022-06-13">2022-06-13</h2><strong>Added deltas to wrangler pages publish</strong><p>Pages has added deltas to <code>wrangler pages publish</code>.</p>
<p>We now keep track of the files that make up each deployment and intelligently only upload the files that we have not seen. This means that similar subsequent deployments should only need to upload a minority of files and this will hopefully make uploads even faster.</p>
<p>This functionality requires Wrangler v2.0.11 or higher.</p><h2 id="2022-06-08">2022-06-08</h2><strong>Added branch alias to PR comments</strong><ul>
<li>PR comments for Pages previews now include the branch alias.</li>
</ul>
