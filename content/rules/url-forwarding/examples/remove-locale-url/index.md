<p class="article-summary">Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format.</p>
<p>This example single redirect for zone <code>example.com</code> will redirect visitors from an old URL format that included the locale (for example, <code>/en-us/&lt;page_name&gt;</code>) to the new format <code>/&lt;page_name&gt;</code>.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13196.md")
</div>
<p>The function <a href="/ruleset-engine/rules-language/functions/#regex_replace"><code>regex_replace()</code></a> allows you to extract parts of the URL using regular expressions' capture groups. Create capture groups by putting part of the regular expression in parentheses. Then, reference a capture group using <code>${&lt;num&gt;}</code> in the replacement string, where <code>&lt;num&gt;</code> is the number of the capture group.</p>
<p>For example, the redirect rule would perform the following redirects:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>Target URL</th>
<th>Status code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com/en-us/meet-our-team</code></td>
<td><code>example.com/meet-our-team</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/pt-BR/meet-our-team</code></td>
<td><code>example.com/meet-our-team</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/en-us/calendar?view=month</code></td>
<td><code>example.com/calendar?view=month</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/meet-our-team</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
<tr>
<td><code>example.com/robots.txt</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
