<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">Pipelines pricing announced</h2>
<div class="changelog-badges"><span>pipelines</span></div><div class="changelog-body"><p><a href="/pipelines/">Cloudflare Pipelines</a> is a streaming data platform that ingests events, transforms them with SQL, and writes to <a href="/r2/">R2</a> as JSON, Parquet, or <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables. Pipelines now has published pricing based on two usage dimensions: the volume of data processed by SQL transforms and the volume of data delivered to sinks. Ingress into a Pipeline stream is free.</p>
<p><strong>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for Pipelines usage.</strong></p>
<p>Pipelines pricing model is designed to charge per GB based on what you use:</p>
<ul>
<li><strong>Streams (ingress)</strong>: Free, regardless of volume.</li>
<li><strong>SQL transforms</strong>: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).</li>
<li><strong>Sinks</strong>: $0.03 / GB for JSON, $0.06 / GB for Parquet or Iceberg output.</li>
</ul>
<p>Workers Free plans include 1 GB / month for each dimension. Workers Paid plans include 50 GB / month.</p>
<p>For full pricing details and billing examples, refer to <a href="/pipelines/platform/pricing/">Pipelines pricing</a>.</p>
</div></article></div>
