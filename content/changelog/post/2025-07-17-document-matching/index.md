<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 17, 2025</time><h2 id="post-title">New detection entry type: Document Matching for DLP</h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now create <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#document-entries">document-based</a> detection entries in DLP by uploading example documents. Cloudflare will encrypt your documents and create a unique fingerprint of the file. This fingerprint is then used to identify similar documents or snippets within your organization's traffic and stored files.</p>
<p><img src="/assets/upstream/images/changelog/dlp/document-match.png" alt="DLP" /></p>
<p><strong>Key features and benefits:</strong></p>
<ul>
<li>
<p><strong>Upload documents, forms, or templates:</strong> Easily upload .docx and .txt files (up to 10 MB) that contain sensitive information you want to protect.</p>
</li>
<li>
<p><strong>Granular control with similarity percentage:</strong> Define a minimum similarity percentage (0-100%) that a document must meet to trigger a detection, reducing false positives.</p>
</li>
<li>
<p><strong>Comprehensive coverage:</strong> Apply these document-based detection entries in:</p>
<ul>
<li>
<p><strong>Gateway policies:</strong> To inspect network traffic for sensitive documents as they are uploaded or shared.</p>
</li>
<li>
<p><strong>CASB (Cloud Access Security Broker):</strong> To scan files stored in cloud applications for sensitive documents at rest.</p>
</li>
</ul>
</li>
<li>
<p><strong>Identify sensitive data:</strong> This new detection entry type is ideal for identifying sensitive data within completed forms, templates, or even small snippets of a larger document, helping you prevent data exfiltration and ensure compliance.</p>
</li>
</ul>
<p>Once uploaded and processed, you can add this new document entry into a DLP profile and policies to enhance your data protection strategy.</p>
</div></article></div>
