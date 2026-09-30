---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/
  description: Use the legacy Wrangler `migrations` array to create, rename, delete, or transfer Durable Object classes.
  full_title: Durable Object class migrations (legacy) · Cloudflare Durable Objects docs
  head_html: <title>Durable Object class migrations (legacy) · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the legacy Wrangler `migrations` array to create, rename, delete, or transfer Durable Object classes."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/index.md"><meta property="og:title" content="Durable Object class migrations (legacy) · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the legacy Wrangler `migrations` array to create, rename, delete, or transfer Durable Object classes."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/#page","headline":"Durable Object class migrations (legacy) \u00b7 Cloudflare Durable Objects docs","description":"Use the legacy Wrangler migrations array to create, rename, delete, or transfer Durable Object classes.","url":"https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/reference/durable-object-class-migrations-legacy/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prefer-declarative-exports-for-new-workers">Prefer declarative exports for new Workers</h3>
@markup("md", "content/.markup/bodies/8134.md")
</aside>
<p>A migration is a mapping process from a class name to a runtime state. This process communicates the changes to the Workers runtime and provides the runtime with instructions on how to deal with those changes.</p>
<p>To apply a migration, you need to:</p>
<ol>
<li>Edit your Wrangler configuration file (refer to <a href="#migration-wrangler-configuration">Migration Wrangler configuration</a>).</li>
<li>Re-deploy your Worker using <code>npx wrangler deploy</code>.</li>
</ol>
<p>You must initiate a migration process when you:</p>
<ul>
<li>Create a new <span class="nb-glossary-tooltip" title="Durable Object class">Durable Object class</span>.</li>
<li>Rename a Durable Object class.</li>
<li>Delete a Durable Object class.</li>
<li>Transfer an existing Durable Objects class.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8133.md")
</aside>
<h2 id="create-migration">Create migration</h2>
<p>The most common migration performed is a new class migration, which informs the runtime that a new Durable Object class is being uploaded. This is also the migration you need when creating your first Durable Object class.</p>
<p>To apply a Create migration:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8137.md")
</div>
<details class="nb-details"><summary>Create migration example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8139.md")
</div></details>
<h3 id="create-durable-object-class-with-key-value-storage">Create Durable Object class with key-value storage</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommended-sqlite-backed-durable-objects">Recommended SQLite-backed Durable Objects</h3>
@markup("md", "content/.markup/bodies/8132.md")
</aside>
<p>Use <code>new_classes</code> on the migration in your Worker's Wrangler file to create a Durable Object class with the key-value storage backend:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8140.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8131.md")
</aside>
<h2 id="delete-migration">Delete migration</h2>
<p>Running a Delete migration will delete all Durable Objects associated with the deleted class, including all of their stored data.</p>
<ul>
<li>Do not run a Delete migration on a class without first ensuring that you are not relying on the Durable Objects within that Worker anymore, that is, first remove the binding from the Worker.</li>
<li>Copy any important data to some other location before deleting.</li>
<li>You do not have to run a Delete migration on a class that was renamed or transferred.</li>
</ul>
<p>To apply a Delete migration:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8142.md")
</div>
<details class="nb-details"><summary>Delete migration example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8144.md")
</div></details>
<h2 id="rename-migration">Rename migration</h2>
<p>Rename migrations are used to transfer stored Durable Objects between two Durable Object classes in the same Worker code file.</p>
<p>To apply a Rename migration:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8146.md")
</div>
<details class="nb-details"><summary>Rename migration example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8148.md")
</div></details>
<h2 id="transfer-migration">Transfer migration</h2>
<p>Transfer migrations are used to transfer stored Durable Objects between two Durable Object classes in different Worker code files.</p>
<p>If you want to transfer stored Durable Objects between two Durable Object classes in the same Worker code file, use <a href="#rename-migration">Rename migrations</a> instead.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8130.md")
</aside>
<p>To apply a Transfer migration:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8150.md")
</div>
<details class="nb-details"><summary>Transfer migration example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8152.md")
</div></details>
<h2 id="migration-wrangler-configuration">Migration Wrangler configuration</h2>
<ul>
<li>
<p>Migrations are performed through the <code>[[migrations]]</code> configurations key in your <code>wrangler.toml</code> file or <code>migrations</code> key in your <code>wrangler.jsonc</code> file.</p>
</li>
<li>
<p>Migrations require a migration tag, which is defined by the <code>tag</code> property in each migration entry.</p>
</li>
<li>
<p>Migration tags are treated like unique names and are used to determine which migrations have already been applied. Once a given Worker code has a migration tag set on it, all future Worker code deployments must include a migration tag.</p>
</li>
<li>
<p>The migration list is an ordered array of tables, specified as a key in your Wrangler configuration file.</p>
</li>
<li>
<p>You can define the migration for each environment, as well as at the top level.</p>
<ul>
<li>Top-level migration is specified at the top-level <code>migrations</code> key in the Wrangler configuration file.</li>
<li>Environment-level migration is specified by a <code>migrations</code> key inside the <code>env</code> key of the Wrangler configuration file (<code>[env.&lt;environment_name&gt;.migrations]</code>).
<ul>
<li>Example Wrangler file:</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-jsonc">{&#10;  // top-level default migrations&#10;  &quot;migrations&quot;: [&#10;    { &quot;tag&quot;: &quot;v1&quot;, &quot;new_sqlite_classes&quot;: [&quot;MyDurableObject&quot;] },&#10;  ],&#10;  &quot;env&quot;: {&#10;    &quot;staging&quot;: {&#10;      // migration override for staging&#10;      &quot;migrations&quot;: [&#10;        { &quot;tag&quot;: &quot;v1-staging&quot;, &quot;new_sqlite_classes&quot;: [&quot;MyDurableObject&quot;] },&#10;      ],&#10;    },&#10;  },&#10;}&#10;</code></pre>
<ul>
<li>
<p>If a migration is only specified at the top-level, but not at the environment-level, the environment will inherit the top-level migration.</p>
</li>
<li>
<p>Migrations at the environment-level override migrations at the top level.</p>
</li>
<li>
<p>All migrations are applied at deployment. Each migration can only be applied once per <a href="/durable-objects/reference/environments/">environment</a>.</p>
</li>
<li>
<p>Each migration in the list can have multiple directives, and multiple migrations can be specified as your project grows in complexity.</p>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/8129.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8128.md")
</aside>
<p>You cannot enable a SQLite storage backend on an existing, deployed Durable Object class, so setting <code>new_sqlite_classes</code> on later migrations will fail with an error. Automatic migration of deployed classes from their key-value storage backend to SQLite storage backend will be available in the future.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-1">Important</h3>
@markup("md", "content/.markup/bodies/8127.md")
</aside>
