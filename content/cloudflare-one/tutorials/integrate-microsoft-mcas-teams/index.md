---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/integrate-microsoft-mcas-teams/
  description: With an MCAS API call, you can manage a URL category that contains the blocked URLs. Use the output to create a Hostname List that can be used by Gateway HTTP policies to block them.
  full_title: Integrate Microsoft MCAS with Cloudflare Zero Trust · Cloudflare One docs
  head_html: <title>Integrate Microsoft MCAS with Cloudflare Zero Trust · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="With an MCAS API call, you can manage a URL category that contains the blocked URLs. Use the output to create a Hostname List that can be used by Gateway HTTP policies to block them."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/integrate-microsoft-mcas-teams/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/integrate-microsoft-mcas-teams/index.md"><meta property="og:title" content="Integrate Microsoft MCAS with Cloudflare Zero Trust · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="With an MCAS API call, you can manage a URL category that contains the blocked URLs. Use the output to create a Hostname List that can be used by Gateway HTTP policies to block them."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/integrate-microsoft-mcas-teams/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/integrate-microsoft-mcas-teams/#page","headline":"Integrate Microsoft MCAS with Cloudflare Zero Trust \u00b7 Cloudflare One docs","description":"With an MCAS API call, you can manage a URL category that contains the blocked URLs. Use the output to create a Hostname List that can be used by Gateway HTTP policies to block them.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/integrate-microsoft-mcas-teams/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/integrate-microsoft-mcas-teams/
  schema: 1
---
<p>Many security teams rely on Microsoft MCAS (Microsoft Cloud App Security), Microsoft's CASB solution, to identify and block threats on the Internet, as well as allow or block access to cloud applications. This tutorial covers how to integrate MCAS with Cloudflare Zero Trust, and create Gateway HTTP policies to ensure visibility and control over data.</p>
<p>Microsoft provides an MCAS API endpoint to allow queries to see which applications have been marked as blocked or allowed. With an MCAS API call, you can manage a URL category that contains the blocked URLs returned by the API query, and use the output to create a Hostname List that can be used by Gateway HTTP policies to block them.</p>
<p><strong>Time to complete:</strong></p>
<p>20 minutes</p>
<h2 id="basic-configuration">Basic configuration</h2>
<p>In your Microsoft account, you first need to create an API token and URL endpoint to use to query the URLs blocked by MCAS.
Follow the guide for <a href="https://learn.microsoft.com/defender-cloud-apps/api-authentication">Managing API tokens for Microsoft Cloud App Security</a> to generate a new API token and a custom API URL for the API endpoint.</p>
<h2 id="using-the-api-to-query-banned-applications">Using the API to query banned applications</h2>
<p>Once you have the API token and API URL, use curl to get the list of banned applications from Microsoft MCAS:</p>
<pre tabindex="0"><code class="language-sh">curl -v &quot;https://&lt;MCAS API URL&gt;/api/discovery_block_scripts/?format=120&amp;type=banned&quot; -H &quot;Authorization: Token &lt;API token&gt;&quot;&#10;</code></pre>
<p>This will return a list of banned hostnames. In this case, Angie's List is the banned application.</p>
<p><img src="/assets/upstream/images/cloudflare-one/microsoft-mcas/mcas-domains.png" alt="Banned hostnames" /></p>
<h3 id="processing-the-output">Processing the output</h3>
<p>As you can see, the banned hostnames are preceded by a <code>.</code>. To use this output for a Zero Trust List, we need to do some text processing.</p>
<ol>
<li>Run the curl API call and direct the output to a file, in this case <code>mcas.txt</code>:</li>
</ol>
<pre tabindex="0"><code class="language-sh">curl -v &quot;https://&lt;MCAS API URL&gt;/api/discovery_block_scripts/?format=120&amp;type=banned&quot; -H &quot;Authorization: Token &lt;API token&gt;&quot; &gt; mcas.txt&#10;</code></pre>
<ol start="2">
<li>Remove the leading <code>.</code>, for example by running <code>sed</code> from the CLI:</li>
</ol>
<pre tabindex="0"><code class="language-sh">sed -i &#x27;s/^.//&#x27; mcas.txt&#10;</code></pre>
<ol start="3">
<li>
<p>This will give you the list of hostnames without leading <code>.</code>.</p>
</li>
<li>
<p>Replace the file's <code>.txt</code> extension with <code>.csv</code>. The file can now be imported into Cloudflare Zero Trust as a Hostname list.</p>
</li>
</ol>
<h2 id="using-the-api-to-query-allowed-applications">Using the API to query allowed applications</h2>
<p>If you would like to get a list of all of the MCAS allowed applications, you can use the same API query, but instead of using <code>type=banned</code>, use <code>type=allowed</code>. This will return a much larger list.</p>
<pre tabindex="0"><code class="language-sh">curl -v &quot;https://&lt;MCAS API URL&gt;/api/discovery_block_scripts/?format=120&amp;type=allowed&quot; -H &quot;Authorization: Token &lt;API token&gt;&quot;&#10;</code></pre>
<h2 id="adding-a-hostname-list-in-cloudflare-one">Adding a hostname list in Cloudflare One</h2>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Reusable components</strong> &gt; <strong>Lists</strong></li>
<li>Select <strong>Upload CSV</strong>. Even though the hostname list is not in CSV format, it will work with no issues.</li>
<li>Add a name for the list, specify <em>Hostnames</em> as the list type, and give it a description.</li>
<li>Drag and drop your MCAS output file created via the API call, or you can select <strong>Select a file</strong>.</li>
<li>Select <strong>Create</strong>. You will see the list of hostnames that have been added to the list.</li>
<li>Save the list.</li>
</ol>
<p>Your list is now ready to be referenced by Gateway HTTP policies.</p>
<h2 id="creating-an-http-policy">Creating an HTTP policy</h2>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>HTTP</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Create the following policy.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>in list</td>
<td>&lt;NEW_HOSTNAME_LIST&gt;</td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>Now when trying to visit one of the MCAS defined sites, the user will be blocked.</p>
<p><img src="/assets/upstream/images/cloudflare-one/microsoft-mcas/mcas-block-page.png" alt="Access Restricted" /></p>
