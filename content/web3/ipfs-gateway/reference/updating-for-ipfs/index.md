<p>Though it is not required, it is strongly recommended that websites hosted on IPFS use only relative links, unless linking to a different domain. This is because data can be accessed in many different (but ultimately equivalent) ways:</p>
<ul>
<li>From your custom domain: <code>https://ipfs.tech/index.html</code></li>
<li>From a gateway: <code>https://cloudflare-ipfs.com/ipns/ipfs.tech/index.html</code></li>
<li>By immutable hash: <code>https://cloudflare-ipfs.com/ipfs/QmNksJqvwHzNtAtYZVqFZFfdCVciY4ojTU2oFZQSFG9U7B/index.html</code></li>
</ul>
<p>Using only relative links within a web application supports all of these at once, and gives the most flexibility to the user. The exact method for switching to relative links, if you do not use them already, depends on the framework you use.</p>
<h2 id="angular-react-vue">Angular, React, Vue</h2>
<p>These popular JavaScript frameworks are covered in a <a href="https://medium.com/pinata/how-to-easily-host-a-website-on-ipfs-9d842b5d6a01">blog post</a> from <a href="https://pinata.cloud/">Pinata</a>. They are fixed with minor config changes.</p>
<h2 id="gatsby">Gatsby</h2>
<p>Gatsby is a JavaScript framework based on React. There is a <a href="https://www.gatsbyjs.org/packages/gatsby-plugin-ipfs/">plugin</a> for it that ensures links are relative.</p>
<h2 id="jekyll">Jekyll</h2>
<p>Add a file <code>_includes/base.html</code> with the contents:</p>
<pre><code>{% assign base = &#x27;&#x27; %}&#10;{% assign depth = page.url | split: &#x27;/&#x27; | size | minus: 1 %}&#10;{% if    depth &lt;= 1 %}{% assign base = &#x27;.&#x27; %}&#10;{% elsif depth == 2 %}{% assign base = &#x27;..&#x27; %}&#10;{% elsif depth == 3 %}{% assign base = &#x27;../..&#x27; %}&#10;{% elsif depth == 4 %}{% assign base = &#x27;../../..&#x27; %}{% endif %}&#10;</code></pre>
<p>This snippet computes the relative path back to the root of the website from the current page. Update any pages that need to link to the root by adding this at the top:</p>
<pre><code>{%- include base.html -%}&#10;</code></pre>
<p>This snippet also prefixing any links with <code>{{base}}</code>. So for example, we would change
<code>href=&quot;/css/main.css&quot;</code> to be <code>href=&quot;{{base}}/css/main.css&quot;</code></p>
<h2 id="generic">Generic</h2>
<p>For other frameworks, or if a framework was not used, there's a script called <a href="https://github.com/tmcw/make-relative">make-relative</a> that will parse the HTML of a website and automatically rewrite links and images to be relative.</p>
