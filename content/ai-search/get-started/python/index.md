---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/get-started/python/
  description: Create, populate, and query an AI Search instance from Python.
  full_title: Python SDK · Cloudflare AI Search docs
  head_html: <title>Python SDK · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, populate, and query an AI Search instance from Python."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/get-started/python/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/get-started/python/index.md"><meta property="og:title" content="Python SDK · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, populate, and query an AI Search instance from Python."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/get-started/python/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/get-started/python/#page","headline":"Python SDK \u00b7 Cloudflare AI Search docs","description":"Create, populate, and query an AI Search instance from Python.","url":"https://developers.cloudflare.com/ai-search/get-started/python/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/get-started/python/
  schema: 1
---
<p>This guide walks you through creating an AI Search instance, uploading content, and querying it from a Python application using the <a href="https://github.com/cloudflare/cloudflare-python">Cloudflare Python SDK</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="https://www.python.org/downloads/">Python</a> 3.8 or later.</li>
<li>Your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>.</li>
</ul>
<p>This guide uses the <code>default</code> <a href="/ai-search/concepts/namespaces/">namespace</a>, which exists automatically on every account. To group instances into your own namespace, create one with <code>client.aisearch.namespaces.create()</code>.</p>
<h2 id="1-create-an-api-token"><ol>
<li>Create an API token</li>
</ol></h2>
<p>You need an API token with <strong>AI Search:Edit</strong> and <strong>AI Search:Run</strong> permissions.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Select <strong>Create Custom Token</strong>.</li>
<li>Enter a <strong>Token name</strong>, for example <code>AI Search Python</code>.</li>
<li>Under <strong>Permissions</strong>, add two permissions:
<ul>
<li><strong>Account</strong> &gt; <strong>AI Search:Edit</strong></li>
<li><strong>Account</strong> &gt; <strong>AI Search:Run</strong></li>
</ul>
</li>
<li>Select <strong>Continue to summary</strong>, then select <strong>Create Token</strong>.</li>
<li>Copy and save the token value. This is your <code>API_TOKEN</code>.</li>
</ol>
<h2 id="2-set-up-your-python-environment"><ol start="2">
<li>Set up your Python environment</li>
</ol></h2>
<p>Create a project directory and a virtual environment to isolate your dependencies.</p>
<pre tabindex="0"><code class="language-sh">mkdir ai-search-python &amp;&amp; cd ai-search-python&#10;python3 -m venv .venv&#10;source .venv/bin/activate&#10;</code></pre>
<p>On Windows, activate the virtual environment with <code>.venv\Scripts\activate</code> instead.</p>
<h2 id="3-install-the-cloudflare-python-sdk"><ol start="3">
<li>Install the Cloudflare Python SDK</li>
</ol></h2>
<p>Install the official <code>cloudflare</code> package:</p>
<pre tabindex="0"><code class="language-sh">pip install cloudflare&#10;</code></pre>
<h2 id="4-set-your-credentials"><ol start="4">
<li>Set your credentials</li>
</ol></h2>
<p>Export your account ID and API token as environment variables.</p>
<pre tabindex="0"><code class="language-sh">export CLOUDFLARE_ACCOUNT_ID=&quot;&lt;ACCOUNT_ID&gt;&quot;&#10;export CLOUDFLARE_API_TOKEN=&quot;&lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h2 id="5-create-an-ai-search-instance"><ol start="5">
<li>Create an AI Search instance</li>
</ol></h2>
<p>Create a file named <code>quickstart.py</code>. The following code sets up a client and creates an instance named <code>my-instance</code> in the <code>default</code> namespace. Because no data source is specified, the instance uses <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a>, so you can upload files to it directly.</p>
<pre tabindex="0"><code class="language-python">import os&#10;&#10;from cloudflare import Cloudflare&#10;&#10;client = Cloudflare(api_token=os.environ[&quot;CLOUDFLARE_API_TOKEN&quot;])&#10;account_id = os.environ[&quot;CLOUDFLARE_ACCOUNT_ID&quot;]&#10;&#10;instance = client.aisearch.namespaces.instances.create(&#10;    name=&quot;default&quot;,&#10;    account_id=account_id,&#10;    id=&quot;my-instance&quot;,&#10;)&#10;&#10;print(f&quot;Created instance: {instance.id}&quot;)&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3046.md")
</aside>
<h2 id="6-upload-content"><ol start="6">
<li>Upload content</li>
</ol></h2>
<p>Add the following to <code>quickstart.py</code> to upload a document. Setting <code>wait_for_completion</code> to <code>True</code> waits for indexing before returning so the file is ready to search. If indexing is still finishing, <code>item.status</code> may be <code>running</code>; the file continues indexing in the background and becomes searchable shortly after.</p>
<pre tabindex="0"><code class="language-python">item = client.aisearch.namespaces.instances.items.upload(&#10;    id=&quot;my-instance&quot;,&#10;    account_id=account_id,&#10;    name=&quot;default&quot;,&#10;    file={&#10;        &quot;file&quot;: (&#10;            &quot;getting-started.md&quot;,&#10;            b&quot;AI Search indexes uploaded content for retrieval.&quot;,&#10;            &quot;text/markdown&quot;,&#10;        ),&#10;        &quot;wait_for_completion&quot;: True,&#10;    },&#10;)&#10;&#10;print(f&quot;Uploaded item status: {item.status}&quot;)&#10;</code></pre>
<h2 id="7-search-your-instance"><ol start="7">
<li>Search your instance</li>
</ol></h2>
<p>Add the following to <code>quickstart.py</code> to run a query against your indexed content.</p>
<pre tabindex="0"><code class="language-python">results = client.aisearch.namespaces.instances.search(&#10;    id=&quot;my-instance&quot;,&#10;    account_id=account_id,&#10;    name=&quot;default&quot;,&#10;    query=&quot;How does AI Search handle uploaded content?&quot;,&#10;)&#10;&#10;if results.chunks:&#10;    print(results.chunks[0].text)&#10;else:&#10;    print(&quot;No results yet — your content may still be indexing. Try again in a moment.&quot;)&#10;</code></pre>
<p>Run the script:</p>
<pre tabindex="0"><code class="language-sh">python quickstart.py&#10;</code></pre>
<p>If the search returns no results, the content may still be indexing. Wait a moment, then run the search again.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-rest-api-ai-search-api-search-rest-api"><a href="/ai-search/api/search/rest-api/">REST API</a></h3><p>Query AI Search using HTTP requests.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-workers-api-ai-search-get-started-workers"><a href="/ai-search/get-started/workers/">Workers API</a></h3><p>Query AI Search from within a Cloudflare Worker.</p></div>
