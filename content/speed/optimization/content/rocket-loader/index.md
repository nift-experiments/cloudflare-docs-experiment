<p>Rocket Loader prioritizes your website's content (text, images, fonts, and more) by deferring the loading of all of your JavaScript until after rendering.</p>
<p>This type of loading (known as asynchronous loading) leads to earlier rendering of your page content. Rocket Loader handles both inline and external scripts, while maintaining order of execution. Cloudflare will detect incompatible browsers and disable Rocket Loader.</p>
<p>On pages with JavaScript, this results in a <a href="https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/">much faster loading experience</a> for your users and improves the following performance metrics:</p>
<ul>
<li>Time to First Paint (TTFP)</li>
<li>Time to First Contentful Paint (TTFCP)</li>
<li>Time to First Meaningful Paint (TTFMP)</li>
<li>Document Load</li>
</ul>
<h2 id="how-to">How to</h2>
<ul class="directory-listing"><li><a href="/speed/optimization/content/rocket-loader/enable/">Enable</a></li><li><a href="/speed/optimization/content/rocket-loader/ignore-javascripts/">Ignore JavaScripts</a></li></ul>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="limitations">Limitations</h2>
<p>Some of Cloudflare's optional features, including Rocket Loader and Email Obfuscation, use non standard tags that fail strict HTML validation via tools like <a href="https://validator.w3.org/">w3.org</a>. These failures do not correlate to issues for your site visitors.</p>
<p>If you observe JavaScript or jQuery issues for your website, <a href="/speed/optimization/content/rocket-loader/enable/">disable Rocket Loader</a> and retest your website.</p>
<p>If you have a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/13944.md")
</div> in place for your domain, you will need to [update your headers](/fundamentals/reference/policies-compliances/content-security-policies/#product-requirements) to support Rocket Loader.
<br />
