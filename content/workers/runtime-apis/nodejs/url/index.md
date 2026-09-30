<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17129.md")
</aside>
<h2 id="domaintoascii">domainToASCII</h2>
<p>Returns the Punycode ASCII serialization of the domain. If domain is an invalid domain, the empty string is returned.</p>
<pre><code class="language-js">import { domainToASCII } from &quot;node:url&quot;;&#10;&#10;console.log(domainToASCII(&quot;español.com&quot;));&#10;// Prints xn--espaol-zwa.com&#10;console.log(domainToASCII(&quot;中文.com&quot;));&#10;// Prints xn--fiq228c.com&#10;console.log(domainToASCII(&quot;xn--iñvalid.com&quot;));&#10;// Prints an empty string&#10;</code></pre>
<h2 id="domaintounicode">domainToUnicode</h2>
<p>Returns the Unicode serialization of the domain. If domain is an invalid domain, the empty string is returned.</p>
<p>It performs the inverse operation to <code>domainToASCII()</code>.</p>
<pre><code class="language-js">import { domainToUnicode } from &quot;node:url&quot;;&#10;&#10;console.log(domainToUnicode(&quot;xn--espaol-zwa.com&quot;));&#10;// Prints español.com&#10;console.log(domainToUnicode(&quot;xn--fiq228c.com&quot;));&#10;// Prints 中文.com&#10;console.log(domainToUnicode(&quot;xn--iñvalid.com&quot;));&#10;// Prints an empty string&#10;</code></pre>
