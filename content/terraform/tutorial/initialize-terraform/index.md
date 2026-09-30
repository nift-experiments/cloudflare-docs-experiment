<p>This tutorial shows you how to get started with Terraform. You just signed up your domain (<code>example.com</code>) on Cloudflare to manage everything in Terraform and now you will create a DNS record pointing <code>www.example.com</code> to a web server at <code>203.0.113.10</code>.</p>
<p>Before you begin, ensure you have:</p>
<ul>
<li><a href="/terraform/installing/">Installed Terraform</a></li>
<li><a href="/fundamentals/api/get-started/create-token/">Created an API Token</a> with permissions to edit resources for this tutorial</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14759.md")
</aside>
<h2 id="1-create-your-configuration"><ol>
<li>Create your configuration</li>
</ol></h2>
<p>Create a file named <code>main.tf</code>, filling in your own values for the <a href="/fundamentals/api/get-started/create-token/">API token</a>, <a href="/fundamentals/account/find-account-and-zone-ids/">zone ID</a>, <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>, and <a href="/fundamentals/manage-domains/add-site/">domain</a>:</p>
<pre><code class="language-bash">terraform {&#10;  required_providers {&#10;    cloudflare = {&#10;      source  = &quot;cloudflare/cloudflare&quot;&#10;      version = &quot;~&gt; 5&quot;&#10;    }&#10;  }&#10;}&#10;&#10;provider &quot;cloudflare&quot; {&#10;  api_token = &quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;}&#10;&#10;variable &quot;zone_id&quot; {&#10;  default = &quot;&lt;YOUR_ZONE_ID&gt;&quot;&#10;}&#10;&#10;variable &quot;account_id&quot; {&#10;  default = &quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;}&#10;&#10;variable &quot;domain&quot; {&#10;  default = &quot;&lt;YOUR_DOMAIN&gt;&quot;&#10;}&#10;&#10;resource &quot;cloudflare_dns_record&quot; &quot;www&quot; {&#10;  zone_id = &quot;&lt;YOUR_ZONE_ID&gt;&quot;&#10;  name    = &quot;www&quot;&#10;  content = &quot;203.0.113.10&quot;&#10;  type    = &quot;A&quot;&#10;  ttl     = 1&#10;  proxied = true&#10;  comment = &quot;Domain verification record&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14758.md")
</aside>
<h2 id="2-initialize-and-plan"><ol start="2">
<li>Initialize and plan</li>
</ol></h2>
<p>Initialize Terraform to download the Cloudflare provider:</p>
<pre><code class="language-sh">terraform init&#10;</code></pre>
<p>Review what will be created:</p>
<pre><code class="language-sh">terraform plan&#10;</code></pre>
<pre><code class="language-sh">&#10;Terraform used the selected providers to generate the following execution plan. Resource actions are&#10;indicated with the following symbols:&#10;  &#43; create&#10;&#10;Terraform will perform the following actions:&#10;&#10;  &#35; cloudflare_dns_record.www will be created&#10;  &#43; resource &quot;cloudflare_dns_record&quot; &quot;www&quot; {&#10;      &#43; comment             = &quot;Domain verification record&quot;&#10;      &#43; comment_modified_on = (known after apply)&#10;      &#43; content             = &quot;203.0.113.10&quot;&#10;      &#43; created_on          = (known after apply)&#10;      &#43; id                  = (known after apply)&#10;      &#43; meta                = (known after apply)&#10;      &#43; modified_on         = (known after apply)&#10;      &#43; name                = &quot;www&quot;&#10;      &#43; proxiable           = (known after apply)&#10;      &#43; proxied             = true&#10;      &#43; settings            = (known after apply)&#10;      &#43; tags                = (known after apply)&#10;      &#43; tags_modified_on    = (known after apply)&#10;      &#43; ttl                 = 1&#10;      &#43; type                = &quot;A&quot;&#10;      &#43; zone_id             = &quot;&lt;YOUR_ZONE_ID&gt;&quot;&#10;    }&#10;&#10;Plan: 1 to add, 0 to change, 0 to destroy.&#10;</code></pre>
<h2 id="3-apply-and-verify"><ol start="3">
<li>Apply and verify</li>
</ol></h2>
<p>Apply your configuration:</p>
<pre><code class="language-sh">terraform apply&#10;</code></pre>
<p>Type <code>yes</code> when prompted.</p>
<pre><code class="language-sh">Terraform used the selected providers to generate the following execution plan. Resource actions are&#10;indicated with the following symbols:&#10;  &#43; create&#10;&#10;Terraform will perform the following actions:&#10;&#10;  &#35; cloudflare_dns_record.www will be created&#10;  &#43; resource &quot;cloudflare_dns_record&quot; &quot;www&quot; {&#10;      &#43; comment             = &quot;Domain verification record&quot;&#10;      &#43; comment_modified_on = (known after apply)&#10;      &#43; content             = &quot;203.0.113.10&quot;&#10;      &#43; created_on          = (known after apply)&#10;      &#43; id                  = (known after apply)&#10;      &#43; meta                = (known after apply)&#10;      &#43; modified_on         = (known after apply)&#10;      &#43; name                = &quot;www&quot;&#10;      &#43; proxiable           = (known after apply)&#10;      &#43; proxied             = true&#10;      &#43; settings            = (known after apply)&#10;      &#43; tags                = (known after apply)&#10;      &#43; tags_modified_on    = (known after apply)&#10;      &#43; ttl                 = 1&#10;      &#43; type                = &quot;A&quot;&#10;      &#43; zone_id             = &quot;&lt;YOUR_ZONE_ID&gt;&quot;&#10;    }&#10;&#10;Plan: 1 to add, 0 to change, 0 to destroy.&#10;&#10;Do you want to perform these actions?&#10;  Terraform will perform the actions described above.&#10;  Only &#x27;yes&#x27; will be accepted to approve.&#10;&#10;  Enter a value: yes&#10;&#10;cloudflare_dns_record.www: Creating...&#10;cloudflare_dns_record.www: Creation complete after 0s&#10;&#10;Apply complete! Resources: 1 added, 0 changed, 0 destroyed.&#10;</code></pre>
<p>After creation, verify the DNS record:</p>
<pre><code class="language-sh">dig www.example.com&#10;</code></pre>
<p>Test the web server response:</p>
<pre><code class="language-sh">curl https://www.example.com&#10;</code></pre>
<pre><code class="language-sh">Hello, this is 203.0.113.10!&#10;</code></pre>
<p>To see the full results returned from the API call:</p>
<pre><code class="language-sh">terraform show&#10;</code></pre>
<p>You can also check the Cloudflare dashboard and go to the <strong>DNS</strong> &gt; <strong>Records</strong> page.</p>
<div class="nb-dash-button"></div>
