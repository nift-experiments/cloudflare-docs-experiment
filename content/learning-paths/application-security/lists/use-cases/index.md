<p>The most common uses cases are:</p>
<ul>
<li>When creating a rule, using a list is easier and less error-prone than adding a long list of items such as IP addresses to a rule expression.</li>
<li>When updating a set of rules that target the same group of IP addresses (or hostnames), using an IP list (or a hostname list) is easier and less error prone than editing multiple rules.</li>
<li>Lists are easier to read and more informative, particularly when you use descriptive names for your lists.</li>
</ul>
<p>When you update the content of a list, any rules that use the list are automatically updated, so you can make a single change to your list rather than modify rules individually.</p>
<p>Cloudflare stores your lists at the account level. You can use the same list in rules of different zones in your Cloudflare account.</p>
