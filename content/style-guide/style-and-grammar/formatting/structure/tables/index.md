---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/tables/
  description: Format tables consistently in documentation.
  full_title: Tables · Cloudflare Style Guide
  head_html: <title>Tables · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Format tables consistently in documentation."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/tables/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/tables/index.md"><meta property="og:title" content="Tables · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Format tables consistently in documentation."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/tables/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/tables/#page","headline":"Tables \u00b7 Cloudflare Style Guide","description":"Format tables consistently in documentation.","url":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/tables/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/style-and-grammar/formatting/structure/tables/
  schema: 1
---
<p>Using tables to simplify content and data provides a comprehensive way to arrange design, structure, outlines, pattern, or order. It is a great tool for comparisons, breakdowns, lists, functions, and descriptions.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14683.md")
</aside>
<p>Here are some tips when creating tables:</p>
<ul>
<li>Label column headers.</li>
<li>Label row headers if appropriate.</li>
<li>Avoid merged cells. Merged cells break screen reader navigation and make content harder for AI systems to parse.</li>
<li>Avoid too much text. Limit each cell to one sentence of content.</li>
<li>Aim for parallelism within the column.</li>
<li>Keep tables as simple and as small as possible.</li>
<li>Sort rows in a logical order. If no logical order exists, use alphabetical order.</li>
<li></li>
</ul>
<p>Introduce tables with a complete sentence that describes the purpose of the table because not all screen readers preannounce tables. The introductory sentence can end with a colon or a period; usually a colon if it immediately precedes the table, and usually a period if there's more material (such as a note paragraph) between the introduction and the table.</p>
<h2 id="introductory-sentences">Introductory sentences</h2>
<p>Introduce tables with a complete sentence that describes the purpose of the table because not all screen readers preannounce tables. The introductory sentence can end with a colon or a period; usually a colon if it immediately precedes the table, and usually a period if there's more material (such as a note paragraph) between the introduction and the table.</p>
<p>When referring to a table, use a phrase like &quot;the following table&quot; or &quot;the preceding table.&quot; Do not place a table in the middle of a sentence.</p>
<h2 id="column-headings">Column headings</h2>
<ul>
<li>Use sentence case.</li>
<li>Write concise headings that clearly describe the column content.</li>
<li>Do not end column headings with punctuation, including periods, ellipses, or colons.</li>
<li>Use the <code>th</code> element for column headings in HTML tables. Include the <code>scope</code> attribute for accessibility.</li>
</ul>
<pre tabindex="0"><code class="language-html">&lt;thead&gt;&#10;	&lt;tr&gt;&#10;		&lt;th scope=&quot;col&quot;&gt;Name&lt;/th&gt;&#10;		&lt;th scope=&quot;col&quot;&gt;Description&lt;/th&gt;&#10;	&lt;/tr&gt;&#10;&lt;/thead&gt;&#10;</code></pre>
<h2 id="table-placement">Table placement</h2>
<ul>
<li>Place each table directly after the sentence that introduces it.</li>
<li>Do not place a table in the middle of a numbered procedure. Place the table immediately after the relevant step.</li>
<li>If a table has footnotes, place them immediately after the table.</li>
</ul>
<h2 id="table-captions">Table captions</h2>
<p>If a page contains only one table, it does not need a caption. Place the table adjacent to the text that refers to it.</p>
<p>If a page contains more than one table in close proximity, add a caption to each table. Start the caption with a number in the form <strong>Table NUMBER.</strong> followed by a brief description. Use sentence case. Do not place a period at the end of the caption.</p>
<p>When referring to a captioned table from text, refer to it by number — for example, &quot;as shown in table 2.&quot; Do not capitalize &quot;table&quot; unless it starts a sentence.</p>
<p>In Markdown, place the caption as a bold line immediately before the table:</p>
<pre tabindex="0"><code class="language-markdown">&#42;*Table 1.** Supported DNS record types&#10;&#10;<table>&#10;&#10;<thead>&#10;<tr>&#10;<th>Type</th>&#10;<th>Description</th>&#10;</tr>&#10;</thead>&#10;<tbody>&#10;<tr>&#10;<td>A</td>&#10;<td>Maps a domain to an IPv4 address</td>&#10;</tr>&#10;<tr>&#10;<td>AAAA</td>&#10;<td>Maps a domain to an IPv6 address</td>&#10;</tr>&#10;</tbody>&#10;&#10;</table>&#10;</code></pre>
<p>In HTML, use the <code>caption</code> element as the first child of the <code>table</code> element:</p>
<pre tabindex="0"><code class="language-html">&lt;table&gt;&#10;	&lt;caption&gt;&#10;		&lt;b&gt;Table 1.&lt;/b&gt;&#10;		Supported DNS record types&#10;	&lt;/caption&gt;&#10;	&lt;thead&gt;&#10;		&lt;tr&gt;&#10;			&lt;th scope=&quot;col&quot;&gt;Type&lt;/th&gt;&#10;			&lt;th scope=&quot;col&quot;&gt;Description&lt;/th&gt;&#10;		&lt;/tr&gt;&#10;	&lt;/thead&gt;&#10;	&lt;tbody&gt;&#10;		&lt;tr&gt;&#10;			&lt;td&gt;A&lt;/td&gt;&#10;			&lt;td&gt;Maps a domain to an IPv4 address&lt;/td&gt;&#10;		&lt;/tr&gt;&#10;	&lt;/tbody&gt;&#10;&lt;/table&gt;&#10;</code></pre>
<h2 id="when-to-use-tables">When to use tables</h2>
<p>The purpose of a table is to provide a scannable content experience. Tables display pieces of information that have some sort of relationship.</p>
<p>Use tables for:</p>
<ul>
<li>Simple mappings of data and values</li>
<li>Categories of things with examples</li>
<li>Collections of things with different attributes</li>
<li>Dates and descriptions, like a changelog</li>
<li>A list of products with attributes</li>
</ul>
<h2 id="when-not-to-use-tables">When not to use tables</h2>
<p>Do not use tables to format a page.</p>
<p>If your information does not fit within these guidelines, consider another method of presentation:</p>
<ul>
<li>Lists</li>
<li>Subsections</li>
<li><a href="/style-guide/build-the-page/components/tabs/">Tabs</a></li>
<li><a href="/style-guide/build-the-page/components/details/">Details</a></li>
</ul>
<h2 id="markdown-examples">Markdown examples</h2>
<p><strong>Add a table</strong></p>
<p>To add a table, use three or more hyphens (---) to create each column’s header, and use pipes (|) to separate each column. For compatibility, you should also add a pipe on either end of the row.</p>
<pre tabindex="0"><code>| Syntax      | Description |&#10;| ----------- | ----------- |&#10;| Header      | Title       |&#10;| Paragraph   | Text        |&#10;</code></pre>
<p>The rendered output looks like this:</p>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Header</td>
<td>Title</td>
</tr>
<tr>
<td>Paragraph</td>
<td>Text</td>
</tr>
</tbody>
</table>
<p>Tip: Creating tables with hyphens and pipes can be tedious. To speed up the process, try using the <a href="https://www.tablesgenerator.com/markdown_tables">Markdown Tables Generator</a>.</p>
<h2 id="alignment">Alignment</h2>
<p>You can align text in the columns to the left, right, or center by adding a colon (:) to the left, right, or on both side of the hyphens within the header row.</p>
<pre tabindex="0"><code>| Syntax      | Description | Test Text     |&#10;| :---        |    :----:   |          ---: |&#10;| Header      | Title       | Here is this  |&#10;| Paragraph   | Text        | And more      |&#10;</code></pre>
<p>The rendered output looks like this:</p>
<table>
<thead>
<tr>
<th align="left">Syntax</th>
<th align="center">Description</th>
<th align="right">Test Text</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Header</td>
<td align="center">Title</td>
<td align="right">Here is this</td>
</tr>
<tr>
<td align="left">Paragraph</td>
<td align="center">Text</td>
<td align="right">And more</td>
</tr>
</tbody>
</table>
<h2 id="formatting-text-in-tables">Formatting text in tables</h2>
<p>You can format the text within tables. For example, you can add links, code, and emphasis.</p>
<p>You can’t add headings, blockquotes, lists, horizontal rules, images, or HTML tags.</p>
<h2 id="escaping-pipe-characters-in-tables">Escaping pipe characters in tables</h2>
<p>You can display a pipe (|) character in a table by using its HTML character code (&quot;|&quot;).</p>
<h2 id="html-examples">HTML examples</h2>
<p>For complex tables, consider using HTML. The following example is created with HTML:</p>
<table>
<thead>
<tr>
<th style="width:50%">Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><code>http.cookie</code><br />`String`</td>
<td>
         <p>Represents the entire cookie as a string.</p>
         <p>
         Example value:
<br /><code>session=8521F670545D7865F79C3D7BEDC29CCE;-background=light</code>
         </p>
</td>
</tr>
<tr>
<td valign="top"><code>http.host</code><br />`String`</td>
<td>
         <p>Represents the hostname used in the full request URI.</p>
         <p>
         Example value:
<br /><code>www.example.org</code>
         </p>
</td>
</tr>
</tbody>
</table>
<h2 id="large-tables">Large tables</h2>
<p>Generally, avoid large tables in documentation. If you have a unique use case, wrap the table in the <code>&lt;table-wrap&gt; </code> component to make it responsive and scrollable.</p>
<table-wrap>
<table>
<thead>
<tr>
<th>Header 1</th>
<th>Header 2</th>
<th>Header 3</th>
<th>Header 4</th>
</tr>
</thead>
<tbody>
<tr>
<td>test</td>
<td>test</td>
<td>test</td>
<td>test</td>
</tr>
</tbody>
</table>
</table-wrap>
<pre tabindex="0"><code class="language-txt">&lt;table-wrap&gt;&#10;&#10;<table>&#10;&#10;<thead>&#10;<tr>&#10;<th>Header 1</th>&#10;<th>Header 2</th>&#10;<th>Header 3</th>&#10;<th>Header 4</th>&#10;</tr>&#10;</thead>&#10;<tbody>&#10;<tr>&#10;<td>test</td>&#10;<td>test</td>&#10;<td>test</td>&#10;<td>test</td>&#10;</tr>&#10;</tbody>&#10;&#10;</table>&#10;&#10;&lt;/table-wrap&gt;&#10;</code></pre>
