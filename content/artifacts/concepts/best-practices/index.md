---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/concepts/best-practices/
  description: Use repo, token, metadata, and namespace patterns.
  full_title: Best practices for Artifacts · Cloudflare Artifacts docs
  head_html: <title>Best practices for Artifacts · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Use repo, token, metadata, and namespace patterns."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/concepts/best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/concepts/best-practices/index.md"><meta property="og:title" content="Best practices for Artifacts · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use repo, token, metadata, and namespace patterns."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/concepts/best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/concepts/best-practices/#page","headline":"Best practices for Artifacts \u00b7 Cloudflare Artifacts docs","description":"Use repo, token, metadata, and namespace patterns.","url":"https://developers.cloudflare.com/artifacts/concepts/best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/concepts/best-practices/
  schema: 1
---
<p>Artifacts works best when you isolate work, scope access narrowly, keep metadata separate, and partition storage deliberately.</p>
<p>Use these patterns to structure repos for agents, automation, and shared systems.</p>
<h2 id="organize-repos-for-isolation">Organize repos for isolation</h2>
<h3 id="create-a-repo-per-agent-session-or-application">Create a repo per agent, session, or application</h3>
<p>Create one repo for each unit of autonomous work. If you have <code>10,000</code> agents, create <code>10,000</code> repos.</p>
<p>This keeps each agent's changes, failures, and cleanup lifecycle separate. It also avoids turning one shared repo into a hot spot for conflicts, large diffs, and accidental overwrites.</p>
<p>Use this pattern when you need to:</p>
<ul>
<li>isolate one agent's work from another agent's work</li>
<li>hand off a repo to a single session or user application</li>
<li>review, merge, archive, or delete work independently</li>
</ul>
<p>Use branches only when collaborators share the same lifecycle and need to work on the same repository. Do not use one shared repo as a queue for many autonomous agents.</p>
<h3 id="use-unique-names">Use unique names</h3>
<p>Repo names are unique within a namespace. If multiple agents need isolated copies of the same baseline repo in one namespace, do not reuse a short shared name such as <code>docs-site</code>.</p>
<p>Include stable identifiers in the repo name, such as the agent name, session ID, user ID, or workflow ID. A name like <code>${agentName}-${sessionId}-${repoName}</code> is safer than <code>${repoName}</code> because it avoids collisions and makes cleanup easier.</p>
<p>This example creates a unique repo name before creating the repo.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3321.md")
</div>
<h3 id="fork-from-a-stable-baseline">Fork from a stable baseline</h3>
<p>Start new repos from a trusted baseline when agents need the same starter files, prompts, or application structure. Forking from a reviewed repo is safer than copying files into every new repo by hand.</p>
<p>This keeps your starting point consistent and makes downstream diffs easier to review. It also lets you merge back only the results you want.</p>
<p>This example forks a reviewed baseline repo into a session-specific repo.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3322.md")
</div>
<h2 id="scope-access-narrowly">Scope access narrowly</h2>
<h3 id="mint-least-privilege-repo-tokens">Mint least-privilege repo tokens</h3>
<p>Artifacts tokens are repo-scoped. Prefer <code>read</code> tokens for cloning, indexing, review, and retrieval.</p>
<p>Use <code>write</code> tokens only for the agent or system that must push changes. Give tokens short lifetimes, and re-issue a fresh token for each agent session.</p>
<p>This example uses the <a href="/artifacts/api/workers-binding/">Workers binding</a> to mint a short-lived read token for a repo.</p>
<p>Assume the caller is already authenticated and authorized before this route returns a token.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3323.md")
</div>
<p>Use the same pattern for <code>write</code> tokens only after your Worker authorizes a session that must push changes.</p>
<p>Do not issue one long-lived write token to every agent. Mint the narrowest token you can, for the shortest time you can.</p>
<h2 id="store-harness-metadata-separately">Store harness metadata separately</h2>
<h3 id="use-git-notes-for-prompts-and-model-output">Use git notes for prompts and model output</h3>
<p>Use <a href="https://git-scm.com/docs/git-notes">git notes</a> to attach prompts, model output, run IDs, or other harness metadata to a commit without changing the commit object or working tree.</p>
<p>This lets you use Artifacts as both the versioned filesystem for agent work and the source of truth for your agent harness. Your files stay focused on the work product, while the commit notes hold the surrounding execution context.</p>
<p>This example stores the user prompt and the assistant summary on the current commit, then reads the note back.</p>
<pre tabindex="0"><code class="language-bash">git notes add -m &#x27;user: Add a best-practices section for unique repo names.&#x27; HEAD&#10;git notes append -m &#x27;assistant: Added naming guidance and a code example.&#x27; HEAD&#10;git notes show HEAD&#10;</code></pre>
<p>If you sync repos between systems, remember that notes live on separate refs. Push and fetch <code>refs/notes/*</code> with the rest of your repo data when you want that metadata to travel with the repository.</p>
<h2 id="partition-namespaces-deliberately">Partition namespaces deliberately</h2>
<h3 id="separate-environments-teams-and-high-rate-workloads">Separate environments, teams, and high-rate workloads</h3>
<p>Use namespaces to separate operating boundaries. Repo separation isolates units of work, while namespace separation isolates ownership, environments, and traffic patterns.</p>
<p>Do not keep every repo in one default namespace once usage grows. Split namespaces when you need clearer ownership or more room to scale within the <a href="/artifacts/platform/limits/">request rate limits</a> for each namespace.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Example namespaces</th>
<th>Why</th>
</tr>
</thead>
<tbody>
<tr>
<td>Environments</td>
<td><code>staging</code>, <code>prod</code></td>
<td>Keep test traffic and production traffic separate.</td>
</tr>
<tr>
<td>Team boundaries</td>
<td><code>sales</code>, <code>finance</code>, <code>devtools</code></td>
<td>Keep ownership, access, and cleanup policies distinct.</td>
</tr>
<tr>
<td>Traffic isolation</td>
<td><code>agents-batch</code>, <code>agents-realtime</code></td>
<td>Prevent one workload from consuming the limits of another workload.</td>
</tr>
</tbody>
</table>
<p>When one namespace becomes hot, shard new repos into additional namespaces instead of continuing to grow a single shared namespace.</p>
