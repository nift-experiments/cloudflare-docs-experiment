---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/
  description: Learn how to programmatically trigger builds, manage triggers, and monitor your Workers Builds using the API.
  full_title: Builds API reference · Cloudflare Workers docs
  head_html: <title>Builds API reference · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to programmatically trigger builds, manage triggers, and monitor your Workers Builds using the API."><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/index.md"><meta property="og:title" content="Builds API reference · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to programmatically trigger builds, manage triggers, and monitor your Workers Builds using the API."><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/#page","headline":"Builds API reference \u00b7 Cloudflare Workers docs","description":"Learn how to programmatically trigger builds, manage triggers, and monitor your Workers Builds using the API.","url":"https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/builds/api-reference/
  schema: 1
---
<p>This guide shows you how to use the <a href="/api/resources/workers_builds/">Workers Builds REST API</a> to programmatically trigger builds, manage triggers, and monitor build status. The examples use <code>curl</code> commands that you can run directly in your terminal or adapt to your preferred programming language. Some examples pipe output through <a href="https://jqlang.org/"><code>jq</code></a> to filter JSON responses — install it if you do not have it already.</p>
<h2 id="before-you-start">Before you start</h2>
<h3 id="1-create-an-api-token-with-the-correct-permissions"><ol>
<li>Create an API token with the correct permissions</li>
</ol></h3>
<p>To use the Builds API, you need an API token to authenticate your requests. The Builds API requires a <strong>user-scoped</strong> API token. Account-scoped tokens are not supported and will return &quot;Invalid token&quot; errors.</p>
<p>Create your token at <a href="https://dash.cloudflare.com/profile/api-tokens">dash.cloudflare.com/profile/api-tokens</a> with the following permissions:</p>
<table>
<thead>
<tr>
<th>Permission</th>
<th>Access level</th>
<th>Why you need it</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers Builds Configuration</td>
<td>Edit</td>
<td>Trigger builds, manage triggers, configure environment variables</td>
</tr>
<tr>
<td>Workers Scripts</td>
<td>Read</td>
<td>Only needed for <a href="#step-1-get-your-worker-tag">one endpoint</a> to retrieve your Worker's tag (documented as <a href="#2-worker-tags-documented-as-external_script_id"><code>external_script_id</code></a>)</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16786.md")
</aside>
<h3 id="2-worker-tags-documented-as-external-script-id"><ol start="2">
<li>Worker tags (documented as external_script_id)</li>
</ol></h3>
<p>The Builds API identifies Workers by their <strong>tag</strong>, an immutable UUID assigned by Cloudflare. In API responses and parameters, this value appears as <code>external_script_id</code>.</p>
<table>
<thead>
<tr>
<th>Identifier</th>
<th>Example</th>
<th>Where it comes from</th>
</tr>
</thead>
<tbody>
<tr>
<td>Worker name (<code>id</code>)</td>
<td><code>my-worker</code></td>
<td>The name you gave your Worker</td>
</tr>
<tr>
<td>Worker tag (<code>external_script_id</code>)</td>
<td><code>1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d</code></td>
<td>Immutable UUID assigned by Cloudflare</td>
</tr>
</tbody>
</table>
<p>Every Builds API endpoint that references a Worker requires the <strong>tag</strong>, not the name.</p>
<h3 id="3-what-is-a-trigger"><ol start="3">
<li>What is a trigger?</li>
</ol></h3>
<p>A <strong>trigger</strong> is a configuration that defines how your Worker gets built and deployed. It specifies the build command, deploy command, environment variables, and which branches should trigger builds. Each Worker has up to <strong>two triggers</strong>: one for production (runs on your <a href="/workers/ci-cd/builds/build-branches/#change-production-branch">production branch</a>) and one for preview (runs on all other branches). To set up triggers, refer to <a href="#set-up-workers-builds-from-scratch">Set up Workers Builds from scratch</a>.</p>
<p><strong>Trigger fields:</strong></p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>trigger_name</code></td>
<td>string</td>
<td>Display name for the trigger</td>
</tr>
<tr>
<td><code>build_token_uuid</code></td>
<td>string</td>
<td>UUID of the build token used to deploy your Worker. Find this in your Worker's <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>API token</strong> section, or via the <a href="/api/resources/workers_builds/subresources/build_tokens/methods/list/"><code>GET /builds/tokens</code></a> endpoint.</td>
</tr>
<tr>
<td><code>build_command</code></td>
<td>string</td>
<td>Command to build your project (for example, <code>npm run build</code>)</td>
</tr>
<tr>
<td><code>deploy_command</code></td>
<td>string</td>
<td>Command to deploy your Worker (for example, <code>npx wrangler deploy</code>)</td>
</tr>
<tr>
<td><code>root_directory</code></td>
<td>string</td>
<td>Path to your project root</td>
</tr>
<tr>
<td><code>branch_includes</code></td>
<td>array</td>
<td>Branch patterns that trigger builds (for example, <code>[&quot;main&quot;]</code> or <code>[&quot;*&quot;]</code>)</td>
</tr>
<tr>
<td><code>branch_excludes</code></td>
<td>array</td>
<td>Branch patterns to exclude</td>
</tr>
<tr>
<td><code>path_includes</code></td>
<td>array</td>
<td>File path patterns that trigger builds</td>
</tr>
<tr>
<td><code>path_excludes</code></td>
<td>array</td>
<td>File path patterns to ignore</td>
</tr>
<tr>
<td><code>build_caching_enabled</code></td>
<td>boolean</td>
<td>Enable or disable build caching</td>
</tr>
<tr>
<td><code>environment_variables</code></td>
<td>object</td>
<td>Build-time variables specific to this trigger</td>
</tr>
</tbody>
</table>
<h2 id="workflow-overview">Workflow overview</h2>
<p>Most Builds API operations follow this pattern: first get your Worker's tag, then get the trigger UUID, then perform build operations.</p>
<p><img src="/assets/upstream/images/workers/builds/workflow-overview.svg" alt="Workflow overview: get Worker tag, then get trigger UUID, then perform build operations." /></p>
<table>
<thead>
<tr>
<th>Step</th>
<th>Action</th>
<th>Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Get Worker tag</td>
<td><code>GET /workers/scripts</code></td>
</tr>
<tr>
<td>2</td>
<td>Get trigger UUID</td>
<td><code>GET /builds/workers/:worker_tag/triggers</code></td>
</tr>
<tr>
<td>3a</td>
<td>Trigger a build</td>
<td><code>POST /builds/triggers/:trigger_uuid/builds</code></td>
</tr>
<tr>
<td>3b</td>
<td>List builds</td>
<td><code>GET /builds/workers/:worker_tag/builds</code></td>
</tr>
<tr>
<td>3c</td>
<td>Get build logs</td>
<td><code>GET /builds/builds/:build_uuid/logs</code></td>
</tr>
<tr>
<td>3d</td>
<td>Cancel a build</td>
<td><code>PUT /builds/builds/:build_uuid/cancel</code></td>
</tr>
</tbody>
</table>
<h2 id="step-1-get-your-worker-tag">Step 1: Get your Worker tag</h2>
<p>Call the <a href="/api/resources/workers/subresources/scripts/methods/list/">Workers Scripts API</a> to list all your Workers and find the <code>tag</code> for the Worker you want to work with:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  | jq &#x27;.result[] | {name: .id, tag: .tag}&#x27;&#10;</code></pre>
<p>Example output:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;name&quot;: &quot;my-worker&quot;,&#10;  &quot;tag&quot;: &quot;1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d&quot;&#10;}&#10;{&#10;  &quot;name&quot;: &quot;another-worker&quot;,&#10;  &quot;tag&quot;: &quot;8a1b2c3d4e5f67890abcdef123456789&quot;&#10;}&#10;</code></pre>
<p>Save the <code>tag</code> value for your Worker. You will use it in all subsequent API calls.</p>
<h2 id="step-2-get-your-trigger-uuid">Step 2: Get your trigger UUID</h2>
<p>Use the <a href="/api/resources/workers_builds/subresources/triggers/methods/list/"><code>GET /builds/workers/{tag}/triggers</code></a> endpoint to list triggers for your Worker:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/workers/{worker_tag}/triggers&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  | jq &#x27;.result[] | {trigger_uuid, trigger_name, branch_includes, branch_excludes}&#x27;&#10;</code></pre>
<p>Example output:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;trigger_uuid&quot;: &quot;f47ac10b-58cc-4372-a567-0e02b2c3d479&quot;,&#10;  &quot;trigger_name&quot;: &quot;Deploy production&quot;,&#10;  &quot;branch_includes&quot;: [&quot;main&quot;],&#10;  &quot;branch_excludes&quot;: []&#10;}&#10;{&#10;  &quot;trigger_uuid&quot;: &quot;a1b2c3d4-e5f6-7890-abcd-ef1234567890&quot;,&#10;  &quot;trigger_name&quot;: &quot;Deploy non-production branches&quot;,&#10;  &quot;branch_includes&quot;: [&quot;*&quot;],&#10;  &quot;branch_excludes&quot;: [&quot;main&quot;]&#10;}&#10;</code></pre>
<p>Save the <code>trigger_uuid</code> for the trigger you want to work with. Remember, you will have at most two triggers: one for your production branch (for example, <code>main</code>) that deploys to your live Worker, and optionally one for all other branches that creates preview deployments.</p>
<h2 id="step-3-work-with-builds">Step 3: Work with builds</h2>
<p>Now that you have the Worker tag and trigger UUID, you can trigger builds, list build history, and get logs.</p>
<h3 id="trigger-a-manual-build">Trigger a manual build</h3>
<p>Use the <a href="/api/resources/workers_builds/subresources/builds/methods/create/"><code>POST /builds/triggers/{uuid}/builds</code></a> endpoint with the <code>trigger_uuid</code> from <a href="#step-2-get-your-trigger-uuid">Step 2</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{trigger_uuid}/builds&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request POST \&#10;  &#45;-data &#x27;{&quot;branch&quot;: &quot;main&quot;}&#x27;&#10;</code></pre>
<p>You must specify <code>branch</code>, <code>commit_hash</code>, or both:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>branch</code></td>
<td>Git branch name to build (for example, <code>main</code>)</td>
</tr>
<tr>
<td><code>commit_hash</code></td>
<td>Specific commit SHA to build. If provided without <code>branch</code>, builds the commit on its current branch.</td>
</tr>
</tbody>
</table>
<p>The response includes the <code>build_uuid</code> which you can use to monitor the build.</p>
<h3 id="list-builds-for-a-worker">List builds for a Worker</h3>
<p>Use the <a href="/api/resources/workers_builds/subresources/builds/methods/list/"><code>GET /builds/workers/{tag}/builds</code></a> endpoint with the <code>worker_tag</code> from <a href="#step-1-get-your-worker-tag">Step 1</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/workers/{worker_tag}/builds&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  | jq &#x27;.result[] | {build_uuid, status, branch, created_at}&#x27;&#10;</code></pre>
<p>The response includes <code>build_uuid</code> for each build, which you need for getting logs or canceling builds.</p>
<h3 id="get-build-logs">Get build logs</h3>
<p>Use the <a href="/api/resources/workers_builds/subresources/builds/methods/get_logs/"><code>GET /builds/builds/{uuid}/logs</code></a> endpoint. Get the <code>build_uuid</code> from:</p>
<ul>
<li><a href="#list-builds-for-a-worker">List builds</a></li>
<li>The response when <a href="#trigger-a-manual-build">triggering a build</a></li>
<li><a href="/api/resources/workers_builds/subresources/builds/methods/get_latest_by_script_ids/">Get latest builds by script IDs</a></li>
<li>The last segment of the URL on your build details page in the dashboard</li>
</ul>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/builds/{build_uuid}/logs&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h3 id="cancel-a-running-build">Cancel a running build</h3>
<p>Use the <a href="/api/resources/workers_builds/subresources/builds/methods/cancel/"><code>PUT /builds/builds/{uuid}/cancel</code></a> endpoint. Get the <code>build_uuid</code> from:</p>
<ul>
<li><a href="#list-builds-for-a-worker">List builds</a></li>
<li>The response when <a href="#trigger-a-manual-build">triggering a build</a></li>
<li><a href="/api/resources/workers_builds/subresources/builds/methods/get_latest_by_script_ids/">Get latest builds by script IDs</a></li>
<li>The last segment of the URL on your build details page in the dashboard</li>
</ul>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/builds/{build_uuid}/cancel&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-request PUT&#10;</code></pre>
<h2 id="update-trigger-configuration">Update trigger configuration</h2>
<p>Use the <a href="/api/resources/workers_builds/subresources/triggers/methods/update/"><code>PATCH /builds/triggers/{uuid}</code></a> endpoint with the <code>trigger_uuid</code> from <a href="#step-2-get-your-trigger-uuid">Step 2</a>. You can update any of the trigger fields described in <a href="#3-what-is-a-trigger">What is a trigger?</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{trigger_uuid}&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request PATCH \&#10;  &#45;-data &#x27;{&#10;    &quot;build_command&quot;: &quot;npm run build:prod&quot;,&#10;    &quot;deploy_command&quot;: &quot;npx wrangler deploy&quot;&#10;  }&#x27;&#10;</code></pre>
<h2 id="manage-build-environment-variables">Manage build environment variables</h2>
<p>Environment variables are set per trigger, meaning you can have different values for production and preview builds. For example, you might set <code>NODE_ENV=production</code> on your production trigger and <code>NODE_ENV=development</code> on your preview trigger. Refer to the <a href="/api/resources/workers_builds/subresources/triggers/subresources/environment_variables/">environment variables API reference</a> for full endpoint details.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16787.md")
</aside>
<h3 id="list-environment-variables">List environment variables</h3>
<p>Use the <code>trigger_uuid</code> from <a href="#step-2-get-your-trigger-uuid">Step 2</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h3 id="set-environment-variables">Set environment variables</h3>
<p>You can set different variables for each trigger. For example, to set production environment variables:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{production_trigger_uuid}/environment_variables&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request PATCH \&#10;  &#45;-data &#x27;{&#10;    &quot;NODE_ENV&quot;: {&quot;value&quot;: &quot;production&quot;, &quot;is_secret&quot;: false},&#10;    &quot;API_KEY&quot;: {&quot;value&quot;: &quot;prod-secret-key&quot;, &quot;is_secret&quot;: true}&#10;  }&#x27;&#10;</code></pre>
<p>And different values for preview builds:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{preview_trigger_uuid}/environment_variables&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request PATCH \&#10;  &#45;-data &#x27;{&#10;    &quot;NODE_ENV&quot;: {&quot;value&quot;: &quot;development&quot;, &quot;is_secret&quot;: false},&#10;    &quot;API_KEY&quot;: {&quot;value&quot;: &quot;dev-secret-key&quot;, &quot;is_secret&quot;: true}&#10;  }&#x27;&#10;</code></pre>
<p>Set <code>is_secret</code> to <code>false</code> for plain values and <code>true</code> for sensitive values that should be masked in logs.</p>
<h3 id="delete-an-environment-variable">Delete an environment variable</h3>
<p>Use the <code>trigger_uuid</code> from <a href="#step-2-get-your-trigger-uuid">Step 2</a>. The <code>variable_key</code> is the key name you set (for example, <code>NODE_ENV</code>).</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables/{variable_key}&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-request DELETE&#10;</code></pre>
<h2 id="purge-build-cache">Purge build cache</h2>
<p>Use the <a href="/api/resources/workers_builds/subresources/triggers/methods/purge_build_cache/"><code>POST /builds/triggers/{uuid}/purge_build_cache</code></a> endpoint with the <code>trigger_uuid</code> from <a href="#step-2-get-your-trigger-uuid">Step 2</a>. This clears cached dependencies and build artifacts for that trigger.</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{trigger_uuid}/purge_build_cache&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-request POST&#10;</code></pre>
<h2 id="examples">Examples</h2>
<p>The following examples show common use cases for the Builds API.</p>
<h3 id="set-up-workers-builds-from-scratch">Set up Workers Builds from scratch</h3>
<p>This example walks through the complete process of connecting a GitHub repository to a Worker and setting up automated builds using only the API.</p>
<p><img src="/assets/upstream/images/workers/builds/setup-from-scratch.svg" alt="Setup flow: get GitHub IDs, create repo connection, get Worker tag, create triggers, set env variables, trigger first build." /></p>
<table>
<thead>
<tr>
<th>Step</th>
<th>Action</th>
<th>Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Get GitHub account/repo IDs</td>
<td><code>GET api.github.com/users/...</code> and <code>GET api.github.com/repos/...</code></td>
</tr>
<tr>
<td>2</td>
<td>Create repo connection</td>
<td><code>PUT /builds/repos/connections</code></td>
</tr>
<tr>
<td>3</td>
<td>Get Worker tag</td>
<td><code>GET /workers/scripts</code></td>
</tr>
<tr>
<td>4</td>
<td>Get build token UUID</td>
<td><code>GET /builds/tokens</code></td>
</tr>
<tr>
<td>5a</td>
<td>Create production trigger</td>
<td><code>POST /builds/triggers</code></td>
</tr>
<tr>
<td>5b</td>
<td>Create preview trigger</td>
<td><code>POST /builds/triggers</code></td>
</tr>
<tr>
<td>6</td>
<td>Set environment variables</td>
<td><code>PATCH /builds/triggers/:trigger_uuid/environment_variables</code></td>
</tr>
<tr>
<td>7</td>
<td>Trigger first build</td>
<td><code>POST /builds/triggers/:trigger_uuid/builds</code></td>
</tr>
</tbody>
</table>
<h4 id="prerequisites">Prerequisites</h4>
<p>Before using the API, you must first install the Cloudflare GitHub App through the dashboard:</p>
<ol>
<li>Go to <strong>Workers &amp; Pages</strong> in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
<li>Select any Worker and go to <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Connect</strong>.</li>
<li>Select <strong>GitHub</strong> and authorize the Cloudflare GitHub App for your account or organization.</li>
</ol>
<p>This one-time setup creates the connection between your GitHub account and Cloudflare. Once complete, you can use the API for everything else.</p>
<h4 id="step-1-get-your-github-account-information">Step 1: Get your GitHub account information</h4>
<p>After installing the GitHub App, you need your GitHub account ID and repository ID. You can find these from an existing trigger or from the GitHub API.</p>
<p>From GitHub's API:</p>
<pre tabindex="0"><code class="language-bash">&#35; Get your GitHub user/org ID&#10;curl -s &quot;https://api.github.com/users/&lt;GITHUB_USERNAME&gt;&quot; | jq &#x27;.id&#x27;&#10;&#10;&#35; Get a repository ID&#10;curl -s &quot;https://api.github.com/repos/&lt;GITHUB_USERNAME&gt;/&lt;REPO_NAME&gt;&quot; | jq &#x27;.id&#x27;&#10;</code></pre>
<h4 id="step-2-create-a-repository-connection">Step 2: Create a repository connection</h4>
<p>Create a connection between your GitHub repository and Cloudflare:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/repos/connections&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request PUT \&#10;  &#45;-data &#x27;{&#10;    &quot;provider_type&quot;: &quot;github&quot;,&#10;    &quot;provider_account_id&quot;: &quot;&lt;GITHUB_USER_ID&gt;&quot;,&#10;    &quot;provider_account_name&quot;: &quot;&lt;GITHUB_USERNAME&gt;&quot;,&#10;    &quot;repo_id&quot;: &quot;&lt;GITHUB_REPO_ID&gt;&quot;,&#10;    &quot;repo_name&quot;: &quot;&lt;REPO_NAME&gt;&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Save the <code>repo_connection_uuid</code> from the response.</p>
<h4 id="step-3-get-your-worker-tag">Step 3: Get your Worker tag</h4>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  | jq &#x27;.result[] | {name: .id, tag: .tag}&#x27;&#10;</code></pre>
<h4 id="step-4-get-your-build-token-uuid">Step 4: Get your build token UUID</h4>
<p>A build token authorizes the build system to deploy your Worker. To get your build token UUID:</p>
<ol>
<li>Go to your Worker in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
<li>Navigate to <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>API token</strong>.</li>
<li>Select an existing build token or create a new one.</li>
</ol>
<p>You can also list your build tokens via the API:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/tokens&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  | jq &#x27;.result[] | {build_token_uuid, build_token_name}&#x27;&#10;</code></pre>
<p>Save the <code>build_token_uuid</code> for the next step.</p>
<h4 id="step-5-create-a-production-trigger">Step 5: Create a production trigger</h4>
<p>Create a trigger that deploys when you push to <code>main</code>:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request POST \&#10;  &#45;-data &#x27;{&#10;    &quot;external_script_id&quot;: &quot;&lt;WORKER_TAG&gt;&quot;,&#10;    &quot;repo_connection_uuid&quot;: &quot;&lt;REPO_CONNECTION_UUID&gt;&quot;,&#10;    &quot;build_token_uuid&quot;: &quot;&lt;BUILD_TOKEN_UUID&gt;&quot;,&#10;    &quot;trigger_name&quot;: &quot;Deploy production&quot;,&#10;    &quot;build_command&quot;: &quot;npm run build&quot;,&#10;    &quot;deploy_command&quot;: &quot;npx wrangler deploy&quot;,&#10;    &quot;root_directory&quot;: &quot;/&quot;,&#10;    &quot;branch_includes&quot;: [&quot;main&quot;],&#10;    &quot;branch_excludes&quot;: [],&#10;    &quot;path_includes&quot;: [&quot;*&quot;],&#10;    &quot;path_excludes&quot;: []&#10;  }&#x27;&#10;</code></pre>
<h4 id="step-6-create-a-preview-trigger-optional">Step 6: Create a preview trigger (optional)</h4>
<p>Create a second trigger for preview deployments on all other branches:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request POST \&#10;  &#45;-data &#x27;{&#10;    &quot;external_script_id&quot;: &quot;&lt;WORKER_TAG&gt;&quot;,&#10;    &quot;repo_connection_uuid&quot;: &quot;&lt;REPO_CONNECTION_UUID&gt;&quot;,&#10;    &quot;build_token_uuid&quot;: &quot;&lt;BUILD_TOKEN_UUID&gt;&quot;,&#10;    &quot;trigger_name&quot;: &quot;Deploy preview branches&quot;,&#10;    &quot;build_command&quot;: &quot;npm run build&quot;,&#10;    &quot;deploy_command&quot;: &quot;npx wrangler versions upload&quot;,&#10;    &quot;root_directory&quot;: &quot;/&quot;,&#10;    &quot;branch_includes&quot;: [&quot;*&quot;],&#10;    &quot;branch_excludes&quot;: [&quot;main&quot;],&#10;    &quot;path_includes&quot;: [&quot;*&quot;],&#10;    &quot;path_excludes&quot;: []&#10;  }&#x27;&#10;</code></pre>
<p>Note the different <code>deploy_command</code>: production uses <code>wrangler deploy</code> while preview uses <code>wrangler versions upload</code> to create preview URLs without affecting the live deployment.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16785.md")
</aside>
<h4 id="step-7-set-environment-variables-for-each-trigger">Step 7: Set environment variables for each trigger</h4>
<p>Set production environment variables:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{production_trigger_uuid}/environment_variables&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request PATCH \&#10;  &#45;-data &#x27;{&#10;    &quot;NODE_ENV&quot;: {&quot;value&quot;: &quot;production&quot;, &quot;is_secret&quot;: false}&#10;  }&#x27;&#10;</code></pre>
<p>Set preview environment variables:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{preview_trigger_uuid}/environment_variables&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request PATCH \&#10;  &#45;-data &#x27;{&#10;    &quot;NODE_ENV&quot;: {&quot;value&quot;: &quot;development&quot;, &quot;is_secret&quot;: false}&#10;  }&#x27;&#10;</code></pre>
<h4 id="step-8-trigger-your-first-build">Step 8: Trigger your first build</h4>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{production_trigger_uuid}/builds&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request POST \&#10;  &#45;-data &#x27;{&quot;branch&quot;: &quot;main&quot;}&#x27;&#10;</code></pre>
<p>Your Worker is now connected to GitHub. Future pushes to <code>main</code> will automatically trigger production deployments, and pushes to other branches will create preview deployments.</p>
<h3 id="redeploy-current-deployment">Redeploy current deployment</h3>
<p>Redeploy your current active deployment to refresh build-time data. This is useful when you need to rebuild without code changes.</p>
<p><img src="/assets/upstream/images/workers/builds/redeploy-flow.svg" alt="Redeploy flow: get active deployment, find the build for that version, retrigger with same branch and commit." /></p>
<table>
<thead>
<tr>
<th>Step</th>
<th>Action</th>
<th>Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Get active deployment</td>
<td><code>GET /workers/scripts/:worker_name/deployments</code></td>
</tr>
<tr>
<td>2</td>
<td>Find the build for that version</td>
<td><code>GET /builds/builds?version_ids=:version_id</code></td>
</tr>
<tr>
<td>3</td>
<td>Retrigger with same branch/commit</td>
<td><code>POST /builds/triggers/:trigger_uuid/builds</code></td>
</tr>
</tbody>
</table>
<p><strong>Step 1: Get the active deployment's version ID</strong></p>
<p>Use the <a href="/api/resources/workers/subresources/scripts/subresources/deployments/methods/list/"><code>GET /workers/scripts/{script_name}/deployments</code></a> endpoint with the <code>worker_name</code> from <a href="#step-1-get-your-worker-tag">Step 1</a>:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{worker_name}/deployments&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  | jq &#x27;.result.deployments[0].versions[0].version_id&#x27;&#10;</code></pre>
<p>Save the <code>version_id</code> from the output.</p>
<p><strong>Step 2: Find the build for that version</strong></p>
<p>Use the <a href="/api/resources/workers_builds/subresources/builds/methods/get_by_version_ids/"><code>GET /builds/builds</code></a> endpoint with the <code>version_id</code> from the previous step:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/builds?version_ids={version_id}&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  | jq &#x27;.result.builds&#x27;&#10;</code></pre>
<p>From the response, note the <code>trigger.trigger_uuid</code>, <code>build_trigger_metadata.branch</code>, and <code>build_trigger_metadata.commit_hash</code>.</p>
<p><strong>Step 3: Retrigger with the same branch and commit</strong></p>
<p>Use the <a href="/api/resources/workers_builds/subresources/builds/methods/create/"><code>POST /builds/triggers/{uuid}/builds</code></a> endpoint with the values from the previous step:</p>
<pre tabindex="0"><code class="language-bash">curl -s &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/builds/triggers/{trigger_uuid}/builds&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request POST \&#10;  &#45;-data &#x27;{&#10;    &quot;branch&quot;: &quot;{branch}&quot;,&#10;    &quot;commit_hash&quot;: &quot;{commit_hash}&quot;&#10;  }&#x27;&#10;&#10;Passing both `branch` and `commit_hash` pins the build to that exact commit on that branch.&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="resource-not-found-error">&quot;Resource not found&quot; error</h3>
<p>You are likely using the Worker name instead of the Worker tag. The Builds API requires the <code>tag</code> (a UUID like <code>1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d</code>), not the Worker name. Refer to <a href="#step-1-get-your-worker-tag">Step 1</a> to get your Worker tag.</p>
<p>For other build errors, refer to <a href="/workers/ci-cd/builds/troubleshoot/">Troubleshooting builds</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/api/resources/workers_builds/">Workers Builds REST API reference</a> - Complete endpoint documentation</li>
<li><a href="/api/resources/workers/subresources/scripts/">Workers Scripts REST API reference</a> - For retrieving Worker tags</li>
<li><a href="/workers/ci-cd/builds/">Workers Builds overview</a> - Dashboard setup and configuration</li>
<li><a href="/workers/ci-cd/builds/configuration/">Build configuration</a> - Build settings and options</li>
<li><a href="/fundamentals/api/get-started/create-token/">Create API token</a> - How to create tokens with the correct permissions</li>
</ul>
