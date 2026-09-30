<p>A link is a reference to another page, part of a page, or external resource. Hyperlinks are useful, but if overdone, they can distract the reader. Follow these guidelines for link text and placement.</p>
<h2 id="types-of-links">Types of links</h2>
<p>There are 3 types of links:</p>
<ul>
<li><strong>External</strong>: To other resources, such as <a href="http://www.cloudflare.com">www.cloudflare.com</a>.</li>
<li><strong>Internal</strong>: To other pages in the docs, such as <a href="/workers/">Workers</a>.</li>
<li><strong>Anchor</strong>: To specific parts of other pages in our docs, such as <a href="/dns/proxy-status/#proxied-records">Proxied records</a>.</li>
</ul>
<h2 id="create-links">Create links</h2>
<p>Use the path to the product when creating a link.</p>
<ul>
<li><strong>Do</strong>:
<ul>
<li><code>This is a link for Cloudflare WAN's [Get started](/cloudflare-wan/get-started/)</code></li>
</ul>
</li>
<li><strong>Don't:</strong>
<ul>
<li><code>This is a link for Cloudflare WAN's [Get started](https://developers.cloudflare.com/cloudflare-wan/get-started/)</code></li>
</ul>
</li>
</ul>
<p><strong>Also not supported:</strong></p>
<ul>
<li>Relative links: <code>A link to [`DurableObjectNamespace::get`](./namespace)</code></li>
<li>Using the file extension in links: <code>This is a link for Cloudflare WAN's [Get started](/cloudflare-wan/get-started.mdx/)</code></li>
</ul>
<h2 id="standard-text">Standard text</h2>
<p>As much as possible, use text that follows one of these patterns:</p>
<ul>
<li><code>For more information, refer to [&lt;PAGE_TITLE&gt;](LINK).</code></li>
<li><code>To &lt;DO_SOMETHING&gt;, refer to [&lt;SECTION_TITLE&gt;](LINK).</code></li>
</ul>
<p>Do not use the following constructions:</p>
<ul>
<li><code>Learn more about...</code></li>
<li><code>To read more....</code></li>
<li><code>For more information, refer the [Merge requests](LINK) page.</code></li>
<li><code>For more information, refer the [Merge requests](LINK) documentation.</code></li>
</ul>
<h2 id="descriptive-link-text">Descriptive link text</h2>
<p>The more descriptive your link text, the easier it is for people to navigate your site and for Google to understand what you are linking to.</p>
<p>Practically, this means you should avoid link text like <code>here</code>, <code>this page</code>, or <code>read more</code>.</p>
<p>For example, instead of:</p>
<ul>
<li><code>For more information, refer to [this page](LINK).</code></li>
<li><code>For more information, go [here](LINK).</code></li>
</ul>
<p>Use:</p>
<ul>
<li><code>For more information, refer to [set up Cloudflare](LINK).</code></li>
</ul>
<p>Follow these additional guidelines for inline paragraph links:</p>
<ul>
<li>Use the actual title of the target page, or an abbreviated version of that title. This helps readers confirm they reached the page they intended to visit.</li>
<li>Use unique link text. Speech recognition software does not handle duplicated link text well.</li>
<li>Use in-paragraph links only when they are internal to Cloudflare's websites and the material relates directly to what is being described. Consider whether the linked content helps the reader make a decision or accomplish something before continuing to read.</li>
<li>Avoid directional language.</li>
</ul>
<h2 id="dashboard-link-text">Dashboard link text</h2>
<p>When directing users to the Cloudflare dashboard, use the following convention:</p>
<pre><code class="language-text">1. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/login) and select your account and domain.&#10;2. Go to **DNS** &gt; **Records**.&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<p>Use a <em>Related resources</em> section at the end of your document for:</p>
<ul>
<li>Internal links that loosely relate to the topic or offer a chance for deeper learning</li>
<li>All external links (not residing in Cloudflare's websites)</li>
<li>Internal and external links that represent the next logical steps to follow</li>
</ul>
<p>External links placed in-paragraph are strongly discouraged because Cloudflare has no control over them. For example, if a link no longer resolves, our content feels less reliable. By shifting all external links to the end of the document, the impact of a broken link is less dramatic.</p>
<h2 id="cross-linking-requirements">Cross-linking requirements</h2>
<p>Cross-links between related pages create a navigable knowledge graph. When an AI system encounters a concept page, it can follow links to find step-by-step instructions, troubleshooting guidance, or reference data and cite the most relevant page for a user's query. Search engines use the same link structure to understand topic relationships.</p>
<p>Every page with a <code>pcx_content_type</code> should include links to related pages in its <strong>Related resources</strong> section. Use the following table to determine which content types to link to from each page.</p>
<table>
<thead>
<tr>
<th>Content type</th>
<th>Must link to</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concept</td>
<td>Related how-to or get-started page; related reference page</td>
</tr>
<tr>
<td>How-to</td>
<td>Prerequisite concept page; relevant configuration page; troubleshooting page</td>
</tr>
<tr>
<td>Get started</td>
<td>Next-level how-to pages; product overview page</td>
</tr>
<tr>
<td>Troubleshooting</td>
<td>Related how-to page; relevant configuration page</td>
</tr>
<tr>
<td>Configuration</td>
<td>Parent how-to or get-started page; relevant concept page</td>
</tr>
<tr>
<td>Reference</td>
<td>Related concept page; how-to pages that use the reference</td>
</tr>
<tr>
<td>Tutorial</td>
<td>Related product overview; prerequisite get-started page</td>
</tr>
</tbody>
</table>
<p>Links should be bidirectional. If a concept page links to a how-to, the how-to should link back to the concept page. This ensures that users (and AI systems) can traverse between pages in either direction.</p>
<h3 id="example">Example</h3>
<p>A concept page about DNS records should link to related how-to, troubleshooting, and reference pages:</p>
<pre><code class="language-markdown">&#35;# Related resources&#10;&#10;&#45; To create or modify DNS records, refer to [Manage DNS records](/dns/manage-dns-records/how-to/create-dns-records/).&#10;&#45; For common DNS issues, refer to [Troubleshoot DNS records](/dns/troubleshooting/).&#10;&#45; For a complete list of supported record types, refer to [DNS record types](/dns/manage-dns-records/reference/dns-record-types/).&#10;</code></pre>
<p>The corresponding how-to page should link back:</p>
<pre><code class="language-markdown">&#35;# Related resources&#10;&#10;&#45; To learn how DNS records work, refer to [DNS records](/dns/manage-dns-records/).&#10;&#45; For record type details, refer to [DNS record types](/dns/manage-dns-records/reference/dns-record-types/).&#10;&#45; For common DNS issues, refer to [Troubleshoot DNS records](/dns/troubleshooting/).&#10;</code></pre>
<h3 id="when-links-do-not-exist">When links do not exist</h3>
<p>Not every content type will have a matching page for every row in the table. Link to what exists. If a related page does not exist yet, do not create a placeholder link. Instead, consider whether the missing page represents a gap in the doc set that should be addressed.</p>
<h2 id="links-for-instructions-in-documentation">Links for instructions in documentation</h2>
<p>Place links for example requests and API calls in code blocks.</p>
<p>Use placeholders in links with account- or user-specific information, and explain what to replace the referential text with.</p>
<ul>
<li>For example, for the link &quot;<code>https://api.cloudflare.com/client/v4/accounts/a0b1c2d3/rulesets</code>&quot; use &quot;<code>https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNTID&gt;/rulesets</code>&quot; and add text to say &quot;replace <code>&lt;ACCOUNTID&gt;</code> with your Account ID&quot; or similar.</li>
</ul>
<p>Refer to <a href="/style-guide/style-and-grammar/formatting/code-conventions-and-format/">angle brackets</a> in Code conventions and formatting.</p>
<h2 id="maintenance">Maintenance</h2>
<p>For more details on how we handle link maintenance, refer to <a href="/style-guide/how-we-docs/links/">Link maintenance</a>.</p>
