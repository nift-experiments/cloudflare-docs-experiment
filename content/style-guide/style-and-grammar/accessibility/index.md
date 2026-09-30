---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/style-and-grammar/accessibility/
  description: Write accessible documentation that works for everyone, including readers who use assistive technologies such as screen readers.
  full_title: Accessibility guidelines · Cloudflare Style Guide
  head_html: <title>Accessibility guidelines · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Write accessible documentation that works for everyone, including readers who use assistive technologies such as screen readers."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/style-and-grammar/accessibility/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/style-and-grammar/accessibility/index.md"><meta property="og:title" content="Accessibility guidelines · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write accessible documentation that works for everyone, including readers who use assistive technologies such as screen readers."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/style-and-grammar/accessibility/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/style-and-grammar/accessibility/#page","headline":"Accessibility guidelines \u00b7 Cloudflare Style Guide","description":"Write accessible documentation that works for everyone, including readers who use assistive technologies such as screen readers.","url":"https://developers.cloudflare.com/style-guide/style-and-grammar/accessibility/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/style-and-grammar/accessibility/
  schema: 1
---
<p>Create documentation that is accessible to all users, including disabled users. Following accessibility best practices ensures that everyone can access, understand, and use the Cloudflare docs effectively.</p>
<p>These guidelines align with Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards and focus on aspects relevant to documentation.</p>
<hr />
<h2 id="page-structure-and-navigation">Page structure and navigation</h2>
<h3 id="provide-informative-unique-page-titles">Provide informative, unique page titles</h3>
<p>Each page must have a descriptive title that clearly identifies its content and distinguishes it from other pages.</p>
<ul>
<li>Put the most specific information first in the title.</li>
<li>Make titles concise but descriptive.</li>
<li>Avoid generic titles like &quot;Overview&quot; or &quot;Introduction&quot; without context.</li>
</ul>
<table>
<thead>
<tr>
<th>Do</th>
<th>Do not</th>
</tr>
</thead>
<tbody>
<tr>
<td>Configure SSL/TLS encryption modes</td>
<td>SSL Settings</td>
</tr>
<tr>
<td>Troubleshoot DNS resolution errors</td>
<td>Troubleshooting</td>
</tr>
</tbody>
</table>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/page-titled">2.4.2 Page Titled (Level A)</a></p>
<hr />
<h3 id="use-headings-to-convey-meaning-and-structure">Use headings to convey meaning and structure</h3>
<p>Headings provide a hierarchical structure that helps all users navigate and understand content. Screen reader users rely on headings to navigate pages efficiently.</p>
<ul>
<li>Use headings in sequential order. Do not skip levels.</li>
<li>Make headings descriptive of the content that follows.</li>
<li>Use only one H1 per page (the page title).</li>
<li>Do not use headings for visual styling purposes only.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14604.md")
</aside>
<table>
<thead>
<tr>
<th>Do</th>
<th>Do not</th>
</tr>
</thead>
<tbody>
<tr>
<td>Use H2 for main sections, H3 for subsections</td>
<td>Skip from H2 to H4</td>
</tr>
<tr>
<td><strong>Configure DNS records</strong> (describes the section)</td>
<td><strong>Important</strong> (vague heading)</td>
</tr>
</tbody>
</table>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels">2.4.6 Headings and Labels (Level AA)</a></p>
<hr />
<h3 id="ensure-logical-reading-order">Ensure logical reading order</h3>
<p>Content must be presented in a meaningful sequence that makes sense when read linearly.</p>
<ul>
<li>Structure content so it flows logically from top to bottom.</li>
<li>Ensure code examples appear after their explanatory text.</li>
<li>Place prerequisite information before procedural steps.</li>
</ul>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/meaningful-sequence">1.3.2 Meaningful Sequence (Level A)</a></p>
<hr />
<h2 id="links-and-navigation">Links and navigation</h2>
<h3 id="write-descriptive-link-text">Write descriptive link text</h3>
<p>Link text must clearly describe the destination or purpose of the link. Avoid ambiguous phrases that provide no context.</p>
<ul>
<li>Use the title of the destination page as link text when possible.</li>
<li>Describe what the user will find when they follow the link.</li>
<li>Avoid generic phrases like &quot;click here&quot;, &quot;read more&quot;, or &quot;this page&quot;.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14603.md")
</aside>
<table>
<thead>
<tr>
<th>Do</th>
<th>Do not</th>
</tr>
</thead>
<tbody>
<tr>
<td>For common issues, refer to the <a href="/dns/troubleshooting/">DNS troubleshooting guide</a>.</td>
<td>For common issues, click <a href="/dns/troubleshooting/">here</a>.</td>
</tr>
<tr>
<td>Learn more about <a href="/ssl/edge-certificates/">configuring SSL certificates</a>.</td>
<td><a href="/ssl/edge-certificates/">Read more</a> about SSL.</td>
</tr>
<tr>
<td>Download the <a href="/workers/wrangler/install-and-update/">Wrangler CLI installation guide</a> (PDF, 2MB).</td>
<td><a href="/workers/wrangler/install-and-update/">Click here</a> to download.</td>
</tr>
</tbody>
</table>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context">2.4.4 Link Purpose (In Context) (Level A)</a></p>
<hr />
<h3 id="avoid-directional-language">Avoid directional language</h3>
<p>Do not use directional or spatial language that relies on visual layout, as this creates barriers for screen reader users and does not always work across different devices.</p>
<ul>
<li>Avoid terms like &quot;above&quot;, &quot;below&quot;, &quot;left&quot;, &quot;right&quot;, &quot;top&quot;, &quot;bottom&quot; unless it is necessary to describe the location of an element.</li>
<li>Reference specific elements by name instead of location.</li>
<li>Use section headings or labels to identify content.</li>
</ul>
<table>
<thead>
<tr>
<th>Do</th>
<th>Do not</th>
</tr>
</thead>
<tbody>
<tr>
<td>In the <strong>DNS</strong> section, select your domain.</td>
<td>On the right side of the screen, select your domain.</td>
</tr>
<tr>
<td>Refer to the <strong>Prerequisites</strong> section for requirements.</td>
<td>See the information above for requirements.</td>
</tr>
<tr>
<td>Select the <strong>Add rule</strong> button.</td>
<td>Click the button below.</td>
</tr>
</tbody>
</table>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/sensory-characteristics">1.3.3 Sensory Characteristics (Level A)</a></p>
<hr />
<h2 id="images-and-multimedia">Images and multimedia</h2>
<h3 id="write-meaningful-alt-text-for-images">Write meaningful alt text for images</h3>
<p>All images that convey information must have alternative text that describes the content or function of the image.</p>
<ul>
<li>Describe what the image shows and why it matters.</li>
<li>Keep alt text concise but informative (typically under 150 characters).</li>
<li>For complex diagrams, provide a longer description in the surrounding text.</li>
<li>Use empty alt text (empty brackets <code>![]</code>) only for purely decorative images.</li>
<li>Do not include phrases like &quot;image of&quot; or &quot;picture of&quot; in alt text.</li>
<li>Avoid keyword stuffing for SEO purposes.</li>
<li>Do not repeat captions or adjacent text in the alt text.</li>
<li>For functional images (like buttons or links), describe the action, not the appearance.</li>
</ul>
<table>
<thead>
<tr>
<th>Image type</th>
<th>Alt text approach</th>
</tr>
</thead>
<tbody>
<tr>
<td>Screenshot showing a specific UI element</td>
<td>Describe what the screenshot shows and its purpose</td>
</tr>
<tr>
<td>Diagram illustrating a concept</td>
<td>Summarize the key information conveyed</td>
</tr>
<tr>
<td>Logo or icon with adjacent text</td>
<td>Use empty alt text to avoid redundancy</td>
</tr>
<tr>
<td>Decorative image</td>
<td>Use empty alt text (empty brackets <code>![]</code>)</td>
</tr>
</tbody>
</table>
<p><strong>Examples</strong>:</p>
<table>
<thead>
<tr>
<th>Do</th>
<th>Do not</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>![Cloudflare dashboard showing the DNS records page with an A record highlighted](path/to/image.png)</code></td>
<td><code>![Screenshot](path/to/image.png)</code></td>
</tr>
<tr>
<td><code>![Network diagram showing traffic flow from client through Cloudflare to origin server](diagram.svg)</code></td>
<td><code>![Diagram of network](diagram.svg)</code></td>
</tr>
<tr>
<td><code>![](path/to/decorative-image.png)</code> (for decorative images)</td>
<td><code>![Blue line decoration](path/to/decorative-image.png)</code></td>
</tr>
<tr>
<td><code>![Diagram of a DNS request going to a DNS resolver](dns-diagram.svg)</code></td>
<td><code>![DNS, DNS resolver, DNS request, how DNS works](dns-diagram.svg)</code> (keywords)</td>
</tr>
<tr>
<td><code>![Submit button](submit-icon.png)</code></td>
<td><code>![Blue rectangular button](submit-icon.png)</code> (describes appearance)</td>
</tr>
</tbody>
</table>
<p><strong>WCAG Reference</strong> <a href="https://www.w3.org/WAI/WCAG21/Understanding/non-text-content">1.1.1 Non-text Content (Level A)</a></p>
<p><strong>Additional resources</strong>:</p>
<ul>
<li><a href="https://www.w3.org/WAI/tutorials/images/">W3C Images Tutorial</a></li>
</ul>
<hr />
<h3 id="provide-captions-and-transcripts-for-multimedia">Provide captions and transcripts for multimedia</h3>
<p>All video and audio content must include captions and transcripts to ensure accessibility for users who are deaf or hard of hearing.</p>
<ul>
<li><strong>Captions:</strong> Provide synchronized captions for all video content that includes audio.</li>
<li><strong>Transcripts:</strong> Provide text transcripts for audio-only content (such as podcasts).</li>
<li><strong>Audio descriptions:</strong> For videos where visual information is essential, provide audio descriptions of important visual content.</li>
</ul>
<p>Captions and transcripts must include:</p>
<ul>
<li>All spoken dialogue and narration.</li>
<li>Speaker identification when multiple speakers are present.</li>
<li>Important sound effects (for example, &quot;door closes&quot; or &quot;alert notification&quot;).</li>
<li>Musical cues when relevant to understanding the content.</li>
</ul>
<p><strong>WCAG reference</strong>:</p>
<ul>
<li><a href="https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded">1.2.2 Captions (Prerecorded) (Level A)</a></li>
<li><a href="https://www.w3.org/WAI/WCAG21/Understanding/audio-description-or-media-alternative-prerecorded">1.2.3 Audio Description or Media Alternative (Level A)</a></li>
</ul>
<hr />
<h2 id="content-clarity-and-readability">Content clarity and readability</h2>
<h3 id="keep-content-clear-and-concise">Keep content clear and concise</h3>
<p>Use simple, straightforward language that is easy to understand. This benefits all users, including those with cognitive disabilities, non-native English speakers, and users with limited technical knowledge.</p>
<ul>
<li>Write in short, clear sentences (aim for 8-12 words per sentence when possible).</li>
<li>Break content into short paragraphs (3-4 sentences maximum).</li>
<li>Use simple words instead of complex alternatives.</li>
<li>Avoid jargon, idioms, and colloquialisms.</li>
<li>Use active voice and present tense.</li>
</ul>
<table>
<thead>
<tr>
<th>Do</th>
<th>Do not</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare protects your website from DDoS attacks.</td>
<td>Cloudflare provides comprehensive protection mechanisms to mitigate distributed denial-of-service attack vectors.</td>
</tr>
<tr>
<td>Complete these steps to configure your settings.</td>
<td>In order to facilitate the configuration of your settings, it is necessary to complete the following steps.</td>
</tr>
</tbody>
</table>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/reading-level">3.1.5 Reading Level (Level AAA)</a></p>
<hr />
<h3 id="expand-acronyms-and-abbreviations">Expand acronyms and abbreviations</h3>
<p>Define all acronyms and abbreviations on first use to ensure clarity for all readers.</p>
<ul>
<li>Spell out the full term on first use, followed by the acronym in parentheses.</li>
<li>Use the acronym consistently throughout the rest of the document.</li>
<li>Consider providing a glossary for documents with many technical terms.</li>
</ul>
<table>
<thead>
<tr>
<th>Do</th>
<th>Do not</th>
</tr>
</thead>
<tbody>
<tr>
<td>Web Content Accessibility Guidelines (WCAG) provide standards for accessible web content.</td>
<td>WCAG provides standards for accessible web content.</td>
</tr>
<tr>
<td>A Distributed Denial of Service (DDoS) attack overwhelms servers with traffic.</td>
<td>A DDoS attack overwhelms servers with traffic.</td>
</tr>
</tbody>
</table>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/abbreviations">3.1.4 Abbreviations (Level AAA)</a></p>
<hr />
<h3 id="define-technical-terms">Define technical terms</h3>
<p>When using technical terms that may be unfamiliar to your audience, provide clear definitions, use the <a href="/style-guide/build-the-page/components/glossary-definition/"><code>GlossaryDefinition</code> component</a>, or link to the relevant glossary.</p>
<ul>
<li>Define terms inline when first introduced.</li>
<li>Link to detailed explanations in a glossary or separate page.</li>
<li>Consider your audience's technical level when determining which terms need definition.</li>
</ul>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/unusual-words">3.1.3 Unusual Words (Level AAA)</a></p>
<hr />
<h3 id="use-lists-for-multiple-items">Use lists for multiple items</h3>
<p>Present multiple related items as bulleted or numbered lists rather than in paragraph form. Lists are easier to scan and understand.</p>
<ul>
<li>Use numbered lists for sequential steps or ordered items.</li>
<li>Use bulleted lists for non-sequential items.</li>
<li>Keep list items parallel in structure.</li>
<li>Introduce lists with a clear lead-in sentence.</li>
</ul>
<hr />
<h2 id="instructions-and-user-guidance">Instructions and user guidance</h2>
<h3 id="provide-clear-instructions">Provide clear instructions</h3>
<p>Ensure that all instructions, guidance, and error messages are clear, specific, and easy to understand.</p>
<ul>
<li>Describe input requirements explicitly (for example, date formats and character limits).</li>
<li>Provide examples when helpful.</li>
<li>Use clear, specific error messages that explain what went wrong and how to fix it.</li>
<li>Avoid unnecessarily technical language in user-facing messages.</li>
</ul>
<table>
<thead>
<tr>
<th>Do</th>
<th>Do not</th>
</tr>
</thead>
<tbody>
<tr>
<td>Enter a valid email address (for example, <a href="mailto:user@example.com">user@example.com</a>).</td>
<td>Enter email.</td>
</tr>
<tr>
<td>Password must be at least 12 characters and include one number.</td>
<td>Invalid password.</td>
</tr>
<tr>
<td>The API key format is incorrect. Ensure it is 32 characters and contains only alphanumeric characters.</td>
<td>Error: Invalid key.</td>
</tr>
</tbody>
</table>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions">3.3.2 Labels or Instructions (Level A)</a></p>
<hr />
<h3 id="do-not-rely-on-color-alone-in-diagrams">Do not rely on color alone in diagrams</h3>
<p>When creating Mermaid diagrams or other visual content, do not use color as the only way to convey information or distinguish elements.</p>
<ul>
<li>Use labels, patterns, or shapes in addition to color.</li>
<li>Ensure text within diagrams has sufficient contrast.</li>
<li>Add descriptive text near the diagram to explain key elements.</li>
</ul>
<table>
<thead>
<tr>
<th>Do</th>
<th>Do not</th>
</tr>
</thead>
<tbody>
<tr>
<td>Use different shapes and labels for different node types</td>
<td>Use only color to differentiate node types</td>
</tr>
<tr>
<td>Add a legend that describes elements by name, not just by color</td>
<td>Refer to &quot;the green box&quot; without additional context</td>
</tr>
</tbody>
</table>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/use-of-color">1.4.1 Use of Color (Level A)</a></p>
<hr />
<h2 id="tables-and-data-presentation">Tables and data presentation</h2>
<h3 id="use-tables-for-tabular-data-only">Use tables for tabular data only</h3>
<p>Use tables only to present data that has a logical relationship between rows and columns. Do not use tables for layout purposes.</p>
<ul>
<li>Include clear, descriptive headers for all columns and rows.</li>
<li>Keep tables simple when possible.</li>
<li>For complex tables, consider breaking them into multiple simpler tables.</li>
<li></li>
</ul>
<p>Introduce tables with a complete sentence that describes the purpose of the table because not all screen readers preannounce tables. The introductory sentence can end with a colon or a period; usually a colon if it immediately precedes the table, and usually a period if there's more material (such as a note paragraph) between the introduction and the table.</p>
<p><strong>WCAG reference</strong>: <a href="https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships">1.3.1 Info and Relationships (Level A)</a></p>
<hr />
<h2 id="code-examples-and-technical-content">Code examples and technical content</h2>
<h3 id="make-code-examples-accessible">Make code examples accessible</h3>
<p>Ensure that code examples are accessible to screen reader users and easy to understand.</p>
<ul>
<li>Always specify the programming language for syntax highlighting.</li>
<li>Provide context before code examples explaining what the code does.</li>
<li>Use descriptive variable and function names in examples.</li>
<li>Add comments to explain complex code sections.</li>
<li>Ensure code examples follow a logical order.</li>
</ul>
<hr />
<h2 id="testing-and-validation">Testing and validation</h2>
<h3 id="test-with-assistive-technology">Test with assistive technology</h3>
<p>When possible, test documentation with assistive technologies to ensure accessibility.</p>
<ul>
<li>Use a screen reader to navigate the page.</li>
<li>Test keyboard navigation (Tab, Enter, arrow keys).</li>
<li>Verify that all interactive elements are keyboard accessible.</li>
<li>Check that focus indicators are visible.</li>
</ul>
<hr />
<h3 id="use-automated-accessibility-tools">Use automated accessibility tools</h3>
<p>Use automated tools to identify common accessibility issues, but remember that automated tools cannot catch all problems.</p>
<ul>
<li>Run automated accessibility checkers during development.</li>
<li>Manually review flagged issues.</li>
<li>Conduct manual testing for issues that tools cannot detect.</li>
</ul>
<hr />
<h2 id="additional-resources">Additional resources</h2>
<h3 id="wcag-guidelines-and-documentation">WCAG guidelines and documentation</h3>
<ul>
<li><a href="https://www.w3.org/TR/WCAG21/">Web Content Accessibility Guidelines (WCAG) 2.1</a></li>
<li><a href="https://www.w3.org/WAI/WCAG21/quickref/">How to Meet WCAG (Quick Reference)</a></li>
<li><a href="https://www.w3.org/WAI/WCAG21/Understanding/">Understanding WCAG 2.1</a></li>
<li><a href="https://www.w3.org/WAI/tips/writing/">Writing for Web Accessibility</a></li>
</ul>
