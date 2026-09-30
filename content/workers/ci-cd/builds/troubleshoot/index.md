<p>This guide explains how to identify and resolve build errors, as well as troubleshoot common issues in the Workers Builds deployment process.</p>
<p>To view your build history, go to your Worker project in the Cloudflare dashboard, select <strong>Deployment</strong>, select <strong>View Build History</strong> at the bottom of the page, and select the build you want to view. To retry a build, select the ellipses next to the build and select <strong>Retry build</strong>. Alternatively, you can select <strong>Retry build</strong> on the Build Details page.</p>
<h2 id="known-issues-or-limitations">Known issues or limitations</h2>
<p>Here are some common build errors that may surface in the build logs or general issues and how you can resolve them.</p>
<h3 id="workers-name-requirement">Workers name requirement</h3>
<p><code>✘ [ERROR] The name in your Wrangler configuration file (&lt;Worker name&gt;) must match the name of your Worker. Please update the name field in your Wrangler configuration file.</code></p>
<p>When connecting a Git repository to your Workers project, the specified name for the Worker on the Cloudflare dashboard must match the <code>name</code> argument in the Wrangler configuration file located in the specified root directory. If it does not match, update the name field in your Wrangler configuration file to match the name of the Worker on the dashboard.</p>
<p>The build system uses the <code>name</code> argument in the Wrangler configuration file to determine which Worker to deploy to Cloudflare's global network. This requirement ensures consistency between the Worker's name on the dashboard and the deployed Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16765.md")
</aside>
<h3 id="missing-wrangler-configuration-file">Missing Wrangler configuration file</h3>
<p><code>✘ [ERROR] Missing entry-point: The entry-point should be specified via the command line (e.g. wrangler deploy path/to/script) or the main config field.</code></p>
<p>If you see this error, a Wrangler configuration file is likely missing from the root directory. Navigate to <strong>Settings</strong> &gt; <strong>Build</strong> &gt; <strong>Build Configuration</strong> to update the root directory, or add a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to the specified directory.</p>
<h3 id="incorrect-account-id">Incorrect account_id</h3>
<p><code>Could not route to /client/v4/accounts/&lt;Account ID&gt;/workers/services/&lt;Worker name&gt;, perhaps your object identifier is invalid? [code: 7003]</code></p>
<p>If you see this error, the Wrangler configuration file likely has an <code>account_id</code> for a different account. Remove the <code>account_id</code> argument or update it with your account's <code>account_id</code>, available in <strong>Workers &amp; Pages Overview</strong> under <strong>Account Details</strong>.</p>
<h3 id="stale-api-token">Stale API token</h3>
<p><code> Failed: The build token selected for this build has been deleted or rolled and cannot be used for this build. Please update your build token in the Worker Builds settings and retry the build.</code></p>
<p>The API Token dropdown in Build Configuration settings may show stale tokens that were edited, deleted, or rolled. If you encounter an error due to a stale token, create a new API Token and select it for the build.</p>
<h3 id="build-timed-out">Build timed out</h3>
<p><code>Build was timed out</code></p>
<p>There is a maximum build duration of 20 minutes. If a build exceeds this time, then the build will be terminated and the above error log is shown. For more details, see <a href="/workers/ci-cd/builds/limits-and-pricing/">Workers Builds limits</a>.</p>
<h3 id="git-integration-issues">Git integration issues</h3>
<p>If you are running into errors associated with your Git integration, you can try removing access to your <a href="/workers/ci-cd/builds/git-integration/github-integration/#removing-access">GitHub</a> or <a href="/workers/ci-cd/builds/git-integration/gitlab-integration/#removing-access">GitLab</a> integration from Cloudflare, then reinstalling the <a href="/workers/ci-cd/builds/git-integration/github-integration/#reinstall-a-git-integration">GitHub</a> or <a href="/workers/ci-cd/builds/git-integration/gitlab-integration/#reinstall-a-git-integration">GitLab</a> integration.</p>
<h2 id="for-additional-support">For additional support</h2>
<p>If you discover additional issues or would like to provide feedback, reach out to us in the <a href="https://discord.com/channels/595317990191398933/1052656806058528849">Cloudflare Developers Discord</a>.</p>
