---
cp9:
  canonical: https://developers.cloudflare.com/d1/reference/migrations/
  description: Version your D1 database schema using SQL migration files that you create, list, and apply with Wrangler.
  full_title: Migrations · Cloudflare D1 docs
  head_html: <title>Migrations · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Version your D1 database schema using SQL migration files that you create, list, and apply with Wrangler."><link rel="canonical" href="https://developers.cloudflare.com/d1/reference/migrations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/reference/migrations/index.md"><meta property="og:title" content="Migrations · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Version your D1 database schema using SQL migration files that you create, list, and apply with Wrangler."><meta property="og:url" content="https://developers.cloudflare.com/d1/reference/migrations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/reference/migrations/#page","headline":"Migrations \u00b7 Cloudflare D1 docs","description":"Version your D1 database schema using SQL migration files that you create, list, and apply with Wrangler.","url":"https://developers.cloudflare.com/d1/reference/migrations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/reference/migrations/
  schema: 1
---
<p>Database migrations are a way of versioning your database. Each migration is stored as an <code>.sql</code> file in your <code>migrations</code> folder. The <code>migrations</code> folder is created in your project directory when you create your first migration. This enables you to store and track changes throughout database development.</p>
<h2 id="features">Features</h2>
<p>Currently, the migrations system aims to be simple yet effective. With the current implementation, you can:</p>
<ul>
<li><a href="/workers/wrangler/commands/d1/#d1-migrations-create">Create</a> an empty migration file.</li>
<li><a href="/workers/wrangler/commands/d1/#d1-migrations-list">List</a> unapplied migrations.</li>
<li><a href="/workers/wrangler/commands/d1/#d1-migrations-apply">Apply</a> remaining migrations.</li>
</ul>
<p>Every migration file in the <code>migrations</code> folder has a specified version number in the filename. Files are listed in sequential order. Every migration file is an SQL file where you can specify queries to be run.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="binding-name-vs-database-name">Binding name vs Database name</h3>
@markup("md", "content/.markup/bodies/7334.md")
</aside>
<h2 id="wrangler-customizations">Wrangler customizations</h2>
<p>By default, migrations are created in the <code>migrations/</code> folder in your Worker project directory. Creating migrations will keep a record of applied migrations in the <code>d1_migrations</code> table found in your database.</p>
<p>This location and table name can be customized in your Wrangler file, inside the D1 binding.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7335.md")
</div>
<h2 id="nested-migration-layouts">Nested migration layouts</h2>
<p>By default, <code>wrangler d1 migrations apply</code> looks for top-level <code>.sql</code> files inside <code>migrations_dir</code>. If you use an ORM such as <a href="https://orm.drizzle.team/">Drizzle</a> that writes each migration as its own subdirectory (for example, <code>migrations/0001_init/migration.sql</code>), set <code>migrations_pattern</code> to the glob that matches your layout:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7336.md")
</div>
<p>Rules for <code>migrations_pattern</code>:</p>
<ul>
<li>When set, <code>migrations_dir</code> must also be set.</li>
<li>The pattern must start with whatever <code>migrations_dir</code> is set to.</li>
<li>Each migration's name is recorded in the migrations table as the path relative to <code>migrations_dir</code> (for example, <code>0001_init/migration.sql</code>). This keeps the table portable across machines.</li>
</ul>
<p>The pattern is a standard glob — <code>*</code> matches one path segment, <code>**</code> matches any number of segments. <code>migrations/**/*.sql</code> will pick up arbitrarily deep <code>.sql</code> files.</p>
<p><code>wrangler d1 migrations create</code> only writes top-level files inside <code>migrations_dir</code>, so if your <code>migrations_pattern</code> only matches nested files (as with the Drizzle layout), generate new migrations using your ORM's command (for example, <code>drizzle-kit generate</code>) instead.</p>
<h2 id="foreign-key-constraints">Foreign key constraints</h2>
<p>When applying a migration, you may need to temporarily disable <a href="/d1/sql-api/foreign-keys/">foreign key constraints</a>. To do so, call <code>PRAGMA defer_foreign_keys = true</code> before making changes that would violate foreign keys.</p>
<p>Refer to the <a href="/d1/sql-api/foreign-keys/">foreign key documentation</a> to learn more about how to work with foreign keys and D1.</p>
