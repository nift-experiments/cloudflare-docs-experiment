<p>URL normalization modifies separators, encoded elements, and literal bytes in incoming URLs so that they conform to a consistent formatting standard.</p>
<p>For example, consider a WAF custom rule that blocks requests whose URLs match <code>www.example.com/hello</code>. The rule would not block a request containing an encoded element — <code>www.example.com/%68ello</code>. Normalizing incoming URLs on the Cloudflare global network helps simplify rules expressions containing URLs.</p>
<p>The two available types of URL normalization are:</p>
<ul>
<li><a href="#rfc-3986-normalization">RFC 3986 normalization</a></li>
<li><a href="#cloudflare-normalization">Cloudflare normalization</a></li>
</ul>
<p>The location where URL normalization will occur depends on the <a href="/rules/normalization/settings/">configured settings</a>.</p>
<p>For examples of the different settings and their impact on request URLs, refer to the <a href="/rules/normalization/examples/">URL normalization examples</a>.</p>
<h2 id="rfc-3986-normalization">RFC 3986 normalization</h2>
<p>The URL normalization performed according to <a href="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986</a> is as follows:</p>
<ul>
<li>The following unreserved characters are <a href="https://tools.ietf.org/html/rfc3986#section-2.1">percent decoded</a> (converted from their <code>%XX</code> encoded form back to the original character):
<ul>
<li>Alphabetical characters: <code>a</code>-<code>z</code>, <code>A</code>-<code>Z</code> (decoded from <code>%41</code>-<code>%5A</code> and <code>%61</code>-<code>%7A</code>)</li>
<li>Digit characters: <code>0</code>-<code>9</code> (decoded from <code>%30</code>-<code>%39</code>)</li>
<li>hyphen <code>-</code> (<code>%2D</code>), period <code>.</code> (<code>%2E</code>), underscore <code>_</code> (<code>%5F</code>), and tilde <code>~</code> (<code>%7E</code>)</li>
</ul>
</li>
<li>These reserved characters are not encoded or decoded: <code>: / ? # [ ] @ ! $ &amp; ' ( ) * + , ; =</code></li>
<li>Other characters, for example literal byte values, are percent encoded.</li>
<li>Percent encoded representations are converted to upper case.</li>
<li>URL paths are normalized according to the <a href="https://tools.ietf.org/html/rfc3986#section-5.2.4">Remove Dot Segments</a> protocol.</li>
</ul>
<h2 id="cloudflare-normalization">Cloudflare normalization</h2>
<p>When using the Cloudflare URL normalization, some extra normalization techniques will be applied to URLs of incoming requests, in the following order:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12974.md")
</div>
