<p>When you set up Email security (formerly Area 1) using an <a href="/email-security/deployment/inline/">inline deployment</a>, you need to tell your existing email providers to accept messages coming from Email security's egress IP addresses.</p>
<p>Refer to this page for reference on what IP subnet mask ranges to use.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="additional-information-for-o365">Additional information for O365</h3>
@markup("md", "content/.markup/bodies/8530.md")
</aside>
<h2 id="united-states">United States</h2>
<p>For customers in the United States, enter the following IP addresses:</p>
<h3 id="ipv4">IPv4</h3>
<pre><code class="language-txt">52.11.209.211&#10;52.89.255.11&#10;52.0.67.109&#10;54.173.50.115&#10;104.30.32.0/19&#10;158.51.64.0/26&#10;158.51.65.0/26&#10;134.195.26.0/23&#10;</code></pre>
<h3 id="ipv6">IPv6</h3>
<pre><code class="language-txt">2405:8100:c400::/38&#10;</code></pre>
<h2 id="europe">Europe</h2>
<p>For customers in Europe, add all our US IP addresses. Additionally, you need to add the following IP addresses for our European data centers:</p>
<pre><code class="language-txt">52.58.35.43&#10;35.157.195.63&#10;</code></pre>
<h2 id="india">India</h2>
<p>For customers in India, add all our US IP addresses.</p>
<h2 id="australia-new-zealand">Australia / New Zealand</h2>
<p>For customers in Australia and New Zealand, add all our US IP addresses.</p>
<h2 id="office-365-24-addresses">Office 365 <code>/24</code> addresses</h2>
<p>Use these IPv4 addresses for Office 365, instead of the <code>/19</code> and <code>/23</code> subnets:</p>
<pre><code class="language-txt">104.30.32.0/24&#10;104.30.33.0/24&#10;104.30.34.0/24&#10;104.30.35.0/24&#10;104.30.36.0/24&#10;104.30.37.0/24&#10;104.30.38.0/24&#10;104.30.39.0/24&#10;104.30.40.0/24&#10;104.30.41.0/24&#10;104.30.42.0/24&#10;104.30.43.0/24&#10;104.30.44.0/24&#10;104.30.45.0/24&#10;104.30.46.0/24&#10;104.30.47.0/24&#10;104.30.48.0/24&#10;104.30.49.0/24&#10;104.30.50.0/24&#10;104.30.51.0/24&#10;104.30.52.0/24&#10;104.30.53.0/24&#10;104.30.54.0/24&#10;104.30.55.0/24&#10;104.30.56.0/24&#10;104.30.57.0/24&#10;104.30.58.0/24&#10;104.30.59.0/24&#10;104.30.60.0/24&#10;104.30.61.0/24&#10;104.30.62.0/24&#10;104.30.63.0/24&#10;134.195.26.0/24&#10;134.195.27.0/24&#10;</code></pre>
