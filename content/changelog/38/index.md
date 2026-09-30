<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-08-14">Aug 14, 2025</time><div>
<h2 id="post-2025-08-14-workers-terraform-and-sdk-improvements"><a href="/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/">Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The recent <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script">Cloudflare Terraform Provider</a> and SDK releases (such as <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a>) bring significant improvements to the Workers developer experience. These updates focus on reliability, performance, and adding <a href="/workers/languages/python/">Python Workers</a> support.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-terraform-improvements">Terraform Improvements</h4>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-fixed-unwarranted-plan-diffs">Fixed Unwarranted Plan Diffs</h4>
<p>Resolved several issues with the <code>cloudflare_workers_script</code> resource that resulted in unwarranted plan diffs, including:</p>
<ul>
<li>Using Durable Objects migrations</li>
<li>Using some bindings such as <code>secret_text</code></li>
<li>Using smart placement</li>
</ul>
<p>A resource should never show a plan diff if there isn't an actual change. This fix reduces unnecessary noise in your Terraform plan and is available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-improved-file-management">Improved File Management</h4>
<p>You can now specify <code>content_file</code> and <code>content_sha256</code> instead of <code>content</code>. This prevents the Workers script content from being stored in the state file which greatly reduces plan diff size and noise. If your workflow synced plans remotely, this should now happen much faster since there is less data to sync. This is available in Cloudflare Terraform Provider 5.7.0.</p>
<pre><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id      = &quot;123456789&quot;&#10;  script_name     = &quot;my_worker&quot;&#10;  main_module     = &quot;worker.mjs&quot;&#10;  content_file    = &quot;worker.mjs&quot;&#10;  content_sha256  = filesha256(&quot;worker.mjs&quot;)&#10;}&#10;</code></pre>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-assets-headers-and-redirects-support">Assets Headers and Redirects Support</h4>
<p>Fixed the <code>cloudflare_workers_script</code> resource to properly support headers and redirects for Assets:</p>
<pre><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id      = &quot;123456789&quot;&#10;  script_name     = &quot;my_worker&quot;&#10;  main_module     = &quot;worker.mjs&quot;&#10;  content_file    = &quot;worker.mjs&quot;&#10;  content_sha256  = filesha256(&quot;worker.mjs&quot;)&#10;  assets = {&#10;    config = {&#10;      headers = file(&quot;_headers&quot;)&#10;      redirects = file(&quot;_redirects&quot;)&#10;    }&#10;    &#35; Completion jwt from:&#10;    &#35; https://developers.cloudflare.com/api/resources/workers/subresources/assets/subresources/upload/&#10;    jwt = &quot;jwt&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-python-workers-support">Python Workers Support</h4>
<p>Added support for uploading <a href="/workers/languages/python/">Python Workers</a> (beta) in Terraform. You can now deploy Python Workers with:</p>
<pre><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id       = &quot;123456789&quot;&#10;  script_name      = &quot;my_worker&quot;&#10;  content_file     = &quot;worker.py&quot;&#10;  content_sha256   = filesha256(&quot;worker.py&quot;)&#10;  content_type     = &quot;text/x-python&quot;&#10;}&#10;</code></pre>
<p>Available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-sdk-enhancements">SDK Enhancements</h4>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-improved-file-upload-api">Improved File Upload API</h4>
<p>Fixed an issue where Workers script versions in the SDK did not allow uploading files. This now works, and also has an improved files upload interface:</p>
<pre><code class="language-js">const scriptContent = `&#10;  export default {&#10;    async fetch(request, env, ctx) {&#10;      return new Response(&#x27;Hello World!&#x27;, { status: 200 });&#10;    }&#10;  };&#10;`;&#10;&#10;client.workers.scripts.versions.create(&#x27;my-worker&#x27;, {&#10;  account_id: &#x27;123456789&#x27;,&#10;  metadata: {&#10;    main_module: &#x27;my-worker.mjs&#x27;,&#10;  },&#10;  files: [&#10;    await toFile(&#10;      Buffer.from(scriptContent),&#10;      &#x27;my-worker.mjs&#x27;,&#10;      {&#10;        type: &quot;application/javascript+module&quot;,&#10;      }&#10;    )&#10;  ]&#10;});&#10;</code></pre>
<p>Will be available in cloudflare-typescript 4.6.0. A similar change will be available in cloudflare-python 4.4.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-fixed-updating-kv-values">Fixed updating KV values</h4>
<p>Previously when creating a KV value like this:</p>
<pre><code class="language-js">await cf.kv.namespaces.values.update(&quot;my-kv-namespace&quot;, &quot;key1&quot;, {&#10;  account_id: &quot;123456789&quot;,&#10;  metadata: &quot;my metadata&quot;,&#10;  value: JSON.stringify({&#10;    hello: &quot;world&quot;&#10;  })&#10;});&#10;</code></pre>
<p>...and recalling it in your Worker like this:</p>
<pre><code class="language-ts">const value = await c.env.KV.get&lt;{hello: string}&gt;(&quot;key1&quot;, &quot;json&quot;);&#10;</code></pre>
<p>You'd get back this: <code>{metadata:'my metadata', value:&quot;{'hello':'world'}&quot;}</code> instead of the correct value of <code>{hello: 'world'}</code></p>
<p>This is fixed in cloudflare-typescript 4.5.0 and will be fixed in cloudflare-python 4.4.0.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-13">Aug 13, 2025</time><div>
<h2 id="post-2025-08-13-ibm-cloud-logs-destination"><a href="/changelog/post/2025-08-13-ibm-cloud-logs-destination/">IBM Cloud Logs as Logpush destination</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare Logpush now supports IBM Cloud Logs as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.ibm.com/products/cloud-logs">IBM Cloud Logs</a> via <a href="/logs/logpush/">Logpush</a>. The setup can be done through the Logpush UI in the Cloudflare Dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>. The integration requires IBM Cloud Logs HTTP Source Address and an IBM API Key. The feature also allows for filtering events and selecting specific log fields.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/">Destination Configuration</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-11">Aug 11, 2025</time><div>
<h2 id="post-2025-08-11-messagechannel"><a href="/changelog/post/2025-08-11-messagechannel/">MessageChannel and MessagePort</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>A minimal implementation of the <a href="https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel">MessageChannel API</a> is now available in Workers. This means that you can use <code>MessageChannel</code> to send messages between different parts of your Worker, but not across different Workers.</p>
<p>The <code>MessageChannel</code> and <code>MessagePort</code> APIs will be available by default at the global scope
with any worker using a compatibility date of <code>2025-08-15</code> or later. It is also available
using the <code>expose_global_message_channel</code> compatibility flag, or can be explicitly disabled
using the <code>no_expose_global_message_channel</code> compatibility flag.</p>
<pre><code class="language-js">const { port1, port2 } = new MessageChannel();&#10;&#10;port2.onmessage = (event) =&gt; {&#10;	console.log(&#x27;Received message:&#x27;, event.data);&#10;};&#10;&#10;port2.postMessage(&#x27;Hello from port2!&#x27;);&#10;</code></pre>
<p>Any value that can be used with the <code>structuredClone(...)</code> API can be sent over the port.</p>
<h4 id="2025-08-11-messagechannel-differences">Differences</h4>
<p>There are a number of key limitations to the <code>MessageChannel</code> API in Workers:</p>
<ul>
<li>Transfer lists are currently not supported. This means that you will not be able to transfer
ownership of objects like <code>ArrayBuffer</code> or <code>MessagePort</code> between ports.</li>
<li>The <code>MessagePort</code> is not yet serializable. This means that you cannot send a <code>MessagePort</code> object
through the <code>postMessage</code> method or via JSRPC calls.</li>
<li>The <code>'messageerror'</code> event is only partially supported. If the <code>'onmessage'</code> handler throws an
error, the <code>'messageerror'</code> event will be triggered, however, it will not be triggered when there
are errors serializing or deserializing the message data. Instead, the error will be thrown when
the <code>postMessage</code> method is called on the sending port.</li>
<li>The <code>'close'</code> event will be emitted on both ports when one of the ports is closed, however it
will not be emitted when the Worker is terminated or when one of the ports is garbage collected.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-11">Aug 11, 2025</time><div>
<h2 id="post-2025-08-11-waf-release"><a href="/changelog/post/2025-08-11-waf-release/">WAF Release - 2025-08-11</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's update focuses on a wide range of enterprise software, from network infrastructure and security platforms to content management systems and development frameworks. Flaws include unsafe deserialization, OS command injection, SSRF, authentication bypass, and arbitrary file upload — many of which allow unauthenticated remote code execution. Notable risks include Cisco Identity Services Engine and Ivanti EPMM, where successful exploitation could grant attackers full administrative control of core network infrastructure and popular web services such as WordPress, SharePoint, and Ingress-Nginx, where security bypasses and arbitrary file uploads could lead to complete site or server compromise.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Cisco Identity Services Engine (CVE-2025-20281): Insufficient input validation in a specific API of Cisco Identity Services Engine (ISE) and ISE-PIC allows an unauthenticated, remote attacker to execute arbitrary code with root privileges on an affected device.</p>
</li>
<li>
<p>Wazuh Server (CVE-2025-24016): An unsafe deserialization vulnerability in Wazuh Server (versions 4.4.0 to 4.9.0) allows for remote code execution and privilege escalation. By injecting unsanitized data, an attacker can trigger an exception to execute arbitrary code on the server.</p>
</li>
<li>
<p>CrushFTP (CVE-2025-54309): A flaw in AS2 validation within CrushFTP allows remote attackers to gain administrative access via HTTPS on systems not using the DMZ proxy feature. This flaw can lead to unauthorized file access and potential system compromise.</p>
</li>
<li>
<p>Kentico Xperience CMS (CVE-2025-2747, CVE-2025-2748): Vulnerabilities in Kentico Xperience CMS could enable cross-site scripting (XSS), allowing attackers to inject malicious scripts into web pages. Additionally, a flaw could allow unauthenticated attackers to bypass the Staging Sync Server's authentication, potentially leading to administrative control over the CMS.</p>
</li>
<li>
<p>Node.js (CVE-2025-27210): An incomplete fix for a previous vulnerability (CVE-2025-23084) in Node.js affects the <code>path.join()</code> API method on Windows systems. The vulnerability can be triggered using reserved Windows device names such as <code>CON</code>, <code>PRN</code>, or <code>AUX</code>.</p>
</li>
<li>
<p>WordPress:Plugin:Simple File List (CVE-2025-34085, CVE-2020-36847):
This vulnerability in the Simple File List plugin for WordPress allows an unauthenticated remote attacker to upload arbitrary files to a vulnerable site. This can be exploited to achieve remote code execution on the server.<br/>
(Note: CVE-2025-34085 has been rejected as a duplicate.)</p>
</li>
<li>
<p>GeoServer (CVE-2024-29198): A Server-Side Request Forgery (SSRF) vulnerability exists in GeoServer's Demo request endpoint, which can be exploited where the Proxy Base URL has not been configured.</p>
</li>
<li>
<p>Ivanti EPMM (CVE-2025-6771): An OS command injection vulnerability in Ivanti Endpoint Manager Mobile (EPMM) before versions 12.5.0.2, 12.4.0.3, and 12.3.0.3 allows a remote, authenticated attacker with high privileges to execute arbitrary code.</p>
</li>
<li>
<p>Microsoft SharePoint (CVE-2024-38018): This is a remote code execution vulnerability affecting Microsoft SharePoint Server.</p>
</li>
<li>
<p>Manager-IO (CVE-2025-54122): A critical unauthenticated full read Server-Side Request Forgery (SSRF) vulnerability is present in the proxy handler of both Manager Desktop and Server editions up to version 25.7.18.2519. This allows an unauthenticated attacker to bypass network isolation and access internal services.</p>
</li>
<li>
<p>Ingress-Nginx (CVE-2025-1974): A vulnerability in the Ingress-Nginx controller for Kubernetes allows an attacker to bypass access control rules. An unauthenticated attacker with access to the pod network can achieve arbitrary code execution in the context of the ingress-nginx controller.</p>
</li>
<li>
<p>PaperCut NG/MF (CVE-2023-2533): A Cross-Site Request Forgery (CSRF) vulnerability has been identified in PaperCut NG/MF. Under specific conditions, an attacker could exploit this to alter security settings or execute arbitrary code if they can deceive an administrator with an active login session into clicking a malicious link.</p>
</li>
<li>
<p>SonicWall SMA (CVE-2025-40598): This vulnerability could allow an unauthenticated attacker to bypass security controls. This allows a remote, unauthenticated attacker to potentially execute arbitrary JavaScript code.</p>
</li>
<li>
<p>WordPress (CVE-2025-5394): The &quot;Alone – Charity Multipurpose Non-profit WordPress Theme&quot; for WordPress  is vulnerable to arbitrary file uploads. A missing capability check allows unauthenticated attackers to upload ZIP files containing webshells disguised as plugins, leading to remote code execution.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities span a broad range of enterprise technologies, including network access control systems, monitoring platforms, web servers, CMS platforms, cloud services, and collaboration tools. Exploitation techniques range from remote code execution and command injection to authentication bypass, SQL injection, path traversal, and configuration weaknesses.</p>
<p>A critical flaw in perimeter devices like Ivanti EPMM or SonicWall SMA could allow an unauthenticated attacker to gain remote code execution, completely breaching the primary network defense. A separate vulnerability within Cisco's Identity Services Engine could then be exploited to bypass network segmentation, granting an attacker widespread internal access. Insecure deserialization issues in platforms like Wazuh Server and CrushFTP could then be used to run malicious payloads or steal sensitive files from administrative consoles. Weaknesses in web delivery controllers like Ingress-Nginx or popular content management systems such as WordPress, SharePoint, and Kentico Xperience create vectors to bypass security controls, exfiltrate confidential data, or fully compromise servers.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ec6480c81253494b947d891e51bc8df1">51bc8df1</code>
</td>
<td>100538</td>
<td>GeoServer - SSRF - CVE:CVE-2024-29198</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b8cb07170b5e4c2b989119cac9e0b290">c9e0b290</code>
</td>
<td>100548</td>
<td>Ivanti EPMM - Remote Code Execution - CVE:CVE-2025-6771</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b3524bf5f5174b65bc892122ad93cda8">ad93cda8</code>
</td>
<td>100550</td>
<td>Microsoft SharePoint - Remote Code Execution - CVE:CVE-2024-38018</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e1369c5d629f4f10a14141381dca5738">1dca5738</code>
</td>
<td>100562</td>
<td>Manager-IO - SSRF - CVE:CVE-2025-54122</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="136f67e2b6a84f15ab9a82a52e9137e1">2e9137e1</code>
</td>
<td>100565</td>
<td>
        Cisco Identity Services Engine - Remote Code Execution -
        CVE:CVE-2025-20281
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ed759f7e44184fa398ef71785d8102e1">5d8102e1</code>
</td>
<td>100567</td>
<td>Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1974</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="71b8e7b646f94d79873213cd99105c43">99105c43</code>
</td>
<td>100569</td>
<td>PaperCut NG/MF - Remote Code Execution - CVE:CVE-2023-2533</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="2450bfbb0cfb4804b109d1c42c81dc88">2c81dc88</code>
</td>
<td>100571</td>
<td>SonicWall SMA - XSS - CVE:CVE-2025-40598</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8ce1903b67e24205a93f5fe6926c96d4">926c96d4</code>
</td>
<td>100573</td>
<td>WordPress - Dangerous File Upload - CVE:CVE-2025-5394</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7fdb3c7bc7b74703aeef4ab240ec2fda">40ec2fda</code>
</td>   
<td>100806</td>      
<td>Wazuh Server - Remote Code Execution - CVE:CVE-2025-24016</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="fe088163f51f4928a3c8d91e2401fa3b">2401fa3b</code>
</td>
<td>100824</td>
<td>CrushFTP - Remote Code Execution - CVE:CVE-2025-54309</td>
<td>Log</td>
<td>Block</td>      
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3638baed75924604987b86d874920ace">74920ace</code>
</td>
<td>100824A</td>
<td>CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 - 2</td>
<td>Log</td>
<td>Block</td>      
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="dda4f95b3a3e4ebb9e194aa5c7e63549">c7e63549</code>
</td>
<td>100825</td>
<td>AMI MegaRAC - Auth Bypass - CVE:CVE-2024-54085</td>
<td>Log</td>
<td>Block</td> 
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7dc07014cefa4ce9adf21da7b79037e6">b79037e6</code>
</td>
<td>100826</td>
<td>Kentico Xperience CMS - Auth Bypass - CVE:CVE-2025-2747</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7c7a0a37e79a4949ba840c9acaf261aa">caf261aa</code>
</td>
<td>100827</td>
<td>Kentico Xperience CMS - XSS - CVE:CVE-2025-2748</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="54dd826f578c483196ce852b6f1c2d12">6f1c2d12</code>
</td>
<td>100828</td>
<td>Node.js - Directory Traversal - CVE:CVE-2025-27210</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="a2867f7456c14213a94509a40341fccc">0341fccc</code>
</td>
<td>100829</td>
<td>
        WordPress:Plugin:Simple File List - Remote Code Execution -
        CVE:CVE-2025-34085
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="4cdb0e792d1a428a897526624cefeeda">4cefeeda</code>
</td>
<td>100829A</td>
<td>
        WordPress:Plugin:Simple File List - Remote Code Execution -
        CVE:CVE-2025-34085 - 2
</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-08">Aug 8, 2025</time><div>
<h2 id="post-2025-08-08-dot-env-in-local-dev"><a href="/changelog/post/2025-08-08-dot-env-in-local-dev/">Wrangler and the Cloudflare Vite plugin support `.env` files in local development</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Now, you can use <code>.env</code> files to provide secrets and override environment variables on the <code>env</code> object during local development with Wrangler and the Cloudflare Vite plugin.</p>
<p>Previously in local development, if you wanted to provide secrets or environment variables during local development, you had to use <code>.dev.vars</code> files.
This is still supported, but you can now also use <code>.env</code> files, which are more familiar to many developers.</p>
<h4 id="2025-08-08-dot-env-in-local-dev-using-env-files-in-local-development">Using <code>.env</code> files in local development</h4>
<p>You can create a <code>.env</code> file in your project root to define environment variables that will be used when running <code>wrangler dev</code> or <code>vite dev</code>. The <code>.env</code> file should be formatted like a <code>dotenv</code> file, such as <code>KEY=&quot;VALUE&quot;</code>:</p>
<pre><code class="language-bash">TITLE=&quot;My Worker&quot;&#10;API_TOKEN=&quot;dev-token&quot;&#10;</code></pre>
<p>When you run <code>wrangler dev</code> or <code>vite dev</code>, the environment variables defined in the <code>.env</code> file will be available in your Worker code via the <code>env</code> object:</p>
<pre><code class="language-javascript">export default {&#10;	async fetch(request, env) {&#10;		const title = env.TITLE; // &quot;My Worker&quot;&#10;		const apiToken = env.API_TOKEN; // &quot;dev-token&quot;&#10;		const response = await fetch(&#10;			`https://api.example.com/data?token=${apiToken}`,&#10;		);&#10;		return new Response(`Title: ${title} - ` + (await response.text()));&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-08-08-dot-env-in-local-dev-multiple-environments-with-env-files">Multiple environments with <code>.env</code> files</h4>
<p>If your Worker defines multiple <a href="/workers/wrangler/environments/">environments</a>, you can set different variables for each environment (ex: production or staging) by creating files named <code>.env.&lt;environment-name&gt;</code>.</p>
<p>When you use <code>wrangler &lt;command&gt; --env &lt;environment-name&gt;</code> or <code>CLOUDFLARE_ENV=&lt;environment-name&gt; vite dev</code>, the corresponding environment-specific file will also be loaded and merged with the <code>.env</code> file.</p>
<p>For example, if you want to set different environment variables for the <code>staging</code> environment, you can create a file named <code>.env.staging</code>:</p>
<pre><code class="language-bash">API_TOKEN=&quot;staging-token&quot;&#10;</code></pre>
<p>When you run <code>wrangler dev --env staging</code> or <code>CLOUDFLARE_ENV=staging vite dev</code>, the environment variables from <code>.env.staging</code> will be merged onto those from <code>.env</code>.</p>
<pre><code class="language-javascript">export default {&#10;	async fetch(request, env) {&#10;		const title = env.TITLE; // &quot;My Worker&quot; (from `.env`)&#10;		const apiToken = env.API_TOKEN; // &quot;staging-token&quot; (from `.env.staging`, overriding the value from `.env`)&#10;		const response = await fetch(&#10;			`https://api.example.com/data?token=${apiToken}`,&#10;		);&#10;		return new Response(`Title: ${title} - ` + (await response.text()));&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-08-08-dot-env-in-local-dev-find-out-more">Find out more</h4>
<p>For more information on how to use <code>.env</code> files with Wrangler and the Cloudflare Vite plugin, see the following documentation:</p>
<ul>
<li><a href="/workers/local-development/environment-variables">Environment variables and secrets</a></li>
<li><a href="https://developers.cloudflare.com/workers/wrangler">Wrangler Documentation</a></li>
<li><a href="https://developers.cloudflare.com/workers/wrangler/vite">Cloudflare Vite Plugin Documentation</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-08">Aug 8, 2025</time><div>
<h2 id="post-2025-08-08-stream-live-observability"><a href="/changelog/post/2025-08-08-stream-live-observability/">Introducing observability and metrics for Stream Live Inputs</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>New information about broadcast metrics and events is now available in
<a href="/stream/">Cloudflare Stream</a> in the Live Input details of the Dashboard.</p>
<p><img src="/assets/upstream/images/changelog/stream/2025-08-05-live-input-metrics.png" alt="Live Input details showing metrics" /></p>
<p>You can now easily understand broadcast-side health and performance with new
observability, which can help when troubleshooting common issues, particularly
for new customers who are just getting started, and platform customers who may
have limited visibility into how their end-users configure their encoders.</p>
<p>To get started, start a live stream (<a href="/stream/examples/obs-from-scratch/">just getting started?</a>), then visit the Live Input details page in Dash.</p>
<p>See our new live <a href="/stream/stream-live/troubleshooting/">Troubleshooting</a> guide
to learn what these metrics mean and how to use them to address common broadcast
issues.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-08">Aug 8, 2025</time><div>
<h2 id="post-2025-08-08-add-waituntil-cloudflare-workers"><a href="/changelog/post/2025-08-08-add-waituntil-cloudflare-workers/">Directly import `waitUntil` in Workers for easily spawning background tasks</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now import <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a> from <code>cloudflare:workers</code> to extend your Worker's execution beyond the request lifecycle from anywhere in your code.</p>
<p>Previously, <code>waitUntil</code> could only be accessed through the <a href="/workers/runtime-apis/context/">execution context</a> (<code>ctx</code>) parameter passed to your Worker's handler functions. This meant that if you needed to schedule background tasks from deeply nested functions or utility modules, you had to pass the <code>ctx</code> object through multiple function calls to access <code>waitUntil</code>.</p>
<p>Now, you can import <code>waitUntil</code> directly and use it anywhere in your Worker without needing to pass <code>ctx</code> as a parameter:</p>
<pre><code class="language-js">import { waitUntil } from &quot;cloudflare:workers&quot;;&#10;&#10;export function trackAnalytics(eventData) {&#10;	const analyticsPromise = fetch(&quot;https://analytics.example.com/track&quot;, {&#10;		method: &quot;POST&quot;,&#10;		body: JSON.stringify(eventData),&#10;	});&#10;&#10;	// Extend execution to ensure analytics tracking completes&#10;	waitUntil(analyticsPromise);&#10;}&#10;</code></pre>
<p>This is particularly useful when you want to:</p>
<ul>
<li>Schedule background tasks from utility functions or modules</li>
<li>Extend execution for analytics, logging, or cleanup operations</li>
<li>Avoid passing the execution context through multiple layers of function calls</li>
</ul>
<pre><code class="language-js">import { waitUntil } from &quot;cloudflare:workers&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// Background task that should complete even after response is sent&#10;		cleanupTempData(env.KV_NAMESPACE);&#10;		return new Response(&quot;Hello, World!&quot;);&#10;	}&#10;};&#10;&#10;function cleanupTempData(kvNamespace) {&#10;	// This function can now use waitUntil without needing ctx&#10;	const deletePromise = kvNamespace.delete(&quot;temp-key&quot;);&#10;	waitUntil(deletePromise);&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17784.md")</aside>
<p>For more information, see the <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code> documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-08">Aug 8, 2025</time><div>
<h2 id="post-2025-08-07-expanded-link-isolation"><a href="/changelog/post/2025-08-07-expanded-link-isolation/">Expanded Email Link Isolation</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.</p>
<p>For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.</p>
<p><img src="/assets/upstream/images/changelog/email-security/expanded-link-actions.jpg" alt="Expanded Email Link Isolation Configuration" /></p>
<p>To isolate all links within a message based on the disposition, select <strong>Settings</strong> &gt; <strong>Link Actions</strong> &gt; <strong>View</strong> and select <strong>Configure</strong>. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on <a href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/">Configure link actions</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-07">Aug 7, 2025</time><div>
<h2 id="post-2025-08-07-emergency-waf-release"><a href="/changelog/post/2025-08-07-emergency-waf-release/">WAF Release - 2025-08-07 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s highlight focuses on two critical vulnerabilities affecting key infrastructure and enterprise content management platforms. Both flaws present significant remote code execution risks that can be exploited with minimal or no user interaction.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Squid (≤6.3) — CVE-2025-54574: A heap buffer overflow occurs when processing Uniform Resource Names (URNs). This vulnerability may allow remote attackers to execute arbitrary code on the server. The issue has been resolved in version 6.4.</p>
</li>
<li>
<p>Adobe AEM (≤6.5.23) — CVE-2025-54253: Due to a misconfiguration, attackers can achieve remote code execution without requiring any user interaction, posing a severe threat to affected deployments.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Both vulnerabilities expose critical attack vectors that can lead to full server compromise. The Squid heap buffer overflow allows remote code execution by crafting malicious URNs, which can lead to server takeover or denial of service. Given Squid’s widespread use as a caching proxy, this flaw could be exploited to disrupt network traffic or gain footholds inside secure environments.</p>
<p>Adobe AEM’s remote code execution vulnerability enables attackers to run arbitrary code on the content management server without any user involvement. This puts sensitive content, application integrity, and the underlying infrastructure at extreme risk. Exploitation could lead to data theft, defacement, or persistent backdoor installation.</p>
<p>These findings reinforce the urgency of updating to the patched versions — Squid 6.4 and Adobe AEM 6.5.24 or later — and reviewing configurations to prevent exploitation.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="f61ed7c1e7e24c3380289e41ef7e015b">ef7e015b</code>
</td>
<td>100844</td>
<td>Adobe Experience Manager Forms - Remote Code Execution - CVE:CVE-2025-54253</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e76e65f5a3aa43f49e0684a6baec057a">baec057a</code>
</td>
<td>100840</td>
<td>Squid - Buffer Overflow - CVE:CVE-2025-54574</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-07">Aug 7, 2025</time><div>
<h2 id="post-2025-08-07-cache-no-cache"><a href="/changelog/post/2025-08-07-cache-no-cache/">Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>By setting the value of the <code>cache</code> property to <code>no-cache</code>, you can force <a href="/workers/reference/how-the-cache-works/">Cloudflare's
cache</a> to revalidate its contents with the origin when
making subrequests from <a href="/workers">Cloudflare Workers</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17783.md")</div>
<p>When <code>no-cache</code> is set, the Worker request will first look for a match in Cloudflare's cache, then:</p>
<ul>
<li>If there is a match, a conditional request is sent to the origin, regardless of whether or not the match is fresh or stale. If the resource has not changed, the
cached version is returned. If the resource has changed, it will be downloaded from the origin, updated in the cache, and returned.</li>
<li>If there is no match, Workers will make a standard request to the origin and cache the response.</li>
</ul>
<p>This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the
<a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property, which is a cross-platform standard part
of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface. Previously, if you set the <code>cache</code>
property on <code>Request</code> to <code>'no-cache'</code>, the Workers runtime threw an exception.</p>
<ul>
<li>Learn <a href="/workers/reference/how-the-cache-works/">how the Cache works with Cloudflare Workers</a></li>
<li>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Worker</li>
<li>Explore <a href="/workers/runtime-apis/">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">Bindings</a> available in Cloudflare Workers</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-06">Aug 6, 2025</time><div>
<h2 id="post-2025-08-06-zone-monitoring-improvements"><a href="/changelog/post/2025-08-06-zone-monitoring-improvements/">Improvements to Monitoring Using Zone Settings</a></h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p>Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.</p>
<p>All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.</p>
<h4 id="2025-08-06-zone-monitoring-improvements-what-you-can-expect">What you can expect:</h4>
<ul>
<li>More reliable application of zone settings to monitoring requests, including
<ul>
<li>Authenticated Origin Pulls</li>
<li>Aegis Egress IP Pools</li>
<li>Argo Smart Routing</li>
<li>HTTP/2 to Origin</li>
</ul>
</li>
<li>Improved support and bug fixes for retries, redirects, and proxied origin resolution</li>
<li>Improved performance and reliability of monitoring requests within the Cloudflare network</li>
<li>Unrelated CDN or WAF configuration changes should have no risk of impact to pool health</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-06">Aug 6, 2025</time><div>
<h2 id="post-2025-08-04-radar-ct-insights"><a href="/changelog/post/2025-08-04-radar-ct-insights/">Certificate Transparency Insights in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now introduces Certificate Transparency (CT) insights, providing visibility into certificate issuance trends based on Certificate Transparency logs currently monitored by Cloudflare.</p>
<p>The following API endpoints are now available:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ct/methods/timeseries/"><code>/ct/timeseries</code></a>: Retrieves certificate issuance time series.</li>
<li><a href="/api/resources/radar/subresources/ct/methods/summary/"><code>/ct/summary/{dimension}</code></a>: Retrieves certificate distribution by dimension.</li>
<li><a href="/api/resources/radar/subresources/ct/methods/timeseries_groups/"><code>/ct/timeseries_groups/{dimension}</code></a>: Retrieves time series of certificate distribution by dimension.</li>
<li><a href="/api/resources/radar/subresources/ct/subresources/authorities/methods/list/"><code>/ct/authorities</code></a>: Lists certification authorities.</li>
<li><a href="/api/resources/radar/subresources/ct/subresources/authorities/methods/get/"><code>/ct/authorities/{ca_slug}</code></a>: Retrieves details about a Certification Authority (CA). CA information is derived from the <a href="https://www.ccadb.org/">Common CA Database (CCADB)</a>.</li>
<li><a href="/api/resources/radar/subresources/ct/subresources/logs/methods/list/"><code>/ct/logs</code></a>: Lists CT logs.</li>
<li><a href="/api/resources/radar/subresources/ct/subresources/logs/methods/get/"><code>/ct/logs/{log_slug}</code></a>: Retrieves details about a CT log. CT log information is derived from the <a href="https://googlechrome.github.io/CertificateTransparency/log_lists.html">Google Chrome log list</a>.</li>
</ul>
<p>For the <code>summary</code> and <code>timeseries_groups</code> endpoints, the following dimensions are available (and also usable as filters):</p>
<ul>
<li><code>ca</code>: Certification Authority (certificate issuer)</li>
<li><code>ca_owner</code>: Certification Authority Owner</li>
<li><code>duration</code>: Certificate validity duration (between NotBefore and NotAfter dates)</li>
<li><code>entry_type</code>: Entry type (certificate vs. pre-certificate)</li>
<li><code>expiration_status</code>: Expiration status (valid vs. expired)</li>
<li><code>has_ips</code>: Presence of IP addresses in certificate <a href="https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/#hostname-and-wildcard-coverage">Subject Alternative Names (SANs)</a></li>
<li><code>has_wildcards</code>: Presence of wildcard DNS names in certificate SANs</li>
<li><code>log</code>: CT log name</li>
<li><code>log_api</code>: CT log API (<a href="https://datatracker.ietf.org/doc/html/rfc6962">RFC6962</a> vs. <a href="https://c2sp.org/static-ct-api">Static</a>)</li>
<li><code>log_operator</code>: CT log operator</li>
<li><code>public_key_algorithm</code>: Public key algorithm of certificate's key</li>
<li><code>signature_algorithm</code>: Signature algorithm used by CA to sign certificate</li>
<li><code>tld</code>: Top-level domain for DNS names found in certificates SANs</li>
<li><code>validation_level</code>: <a href="https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/">Validation level</a></li>
</ul>
<p>Check out the new Certificate Transparency insights in the <a href="https://radar.cloudflare.com/certificate-transparency">new Radar page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-05">Aug 5, 2025</time><div>
<h2 id="post-2025-08-05-agents-MCP-update"><a href="/changelog/post/2025-08-05-agents-MCP-update/">Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest releases of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings major improvements to MCP transport protocols support and agents connectivity. Key updates include:</p>
<h4 id="2025-08-05-agents-MCP-update-mcp-elicitation-support">MCP elicitation support</h4>
<p>MCP servers can now request user input during tool execution, enabling interactive workflows like confirmations, forms, and multi-step processes. This feature uses durable storage to preserve elicitation state even during agent hibernation, ensuring seamless user interactions across agent lifecycle events.</p>
<pre><code class="language-ts">// Request user confirmation via elicitation&#10;const confirmation = await this.elicitInput({&#10;	message: `Are you sure you want to increment the counter by ${amount}?`,&#10;	requestedSchema: {&#10;		type: &quot;object&quot;,&#10;		properties: {&#10;			confirmed: {&#10;				type: &quot;boolean&quot;,&#10;				title: &quot;Confirm increment&quot;,&#10;				description: &quot;Check to confirm the increment&quot;,&#10;			},&#10;		},&#10;		required: [&quot;confirmed&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Check out our <a href="https://github.com/whoiskatrin/agents/tree/main/examples/mcp-elicitation-demo">demo</a> to see elicitation in action.</p>
<h4 id="2025-08-05-agents-MCP-update-http-streamable-transport-for-mcp">HTTP streamable transport for MCP</h4>
<p>MCP now supports HTTP streamable transport which is recommended over SSE. This transport type offers:</p>
<ul>
<li><strong>Better performance</strong>: More efficient data streaming and reduced overhead</li>
<li><strong>Improved reliability</strong>: Enhanced connection stability and error recover- <strong>Automatic fallback</strong>: If streamable transport is not available, it gracefully falls back to SSE</li>
</ul>
<pre><code class="language-ts">export default MyMCP.serve(&quot;/mcp&quot;, {&#10;	binding: &quot;MyMCP&quot;,&#10;});&#10;</code></pre>
<p>The SDK automatically selects the best available transport method, gracefully falling back from streamable-http to SSE when needed.</p>
<h4 id="2025-08-05-agents-MCP-update-enhanced-mcp-connectivity">Enhanced MCP connectivity</h4>
<p>Significant improvements to MCP server connections and transport reliability:</p>
<ul>
<li><strong>Auto transport selection</strong>: Automatically determines the best transport method, falling back from streamable-http to SSE as needed</li>
<li><strong>Improved error handling</strong>: Better connection state management and error reporting for MCP servers</li>
<li><strong>Reliable prop updates</strong>: Centralized agent property updates ensure consistency across different contexts</li>
</ul>
<h4 id="2025-08-05-agents-MCP-update-lightweight-queue-for-fast-task-deferral">Lightweight .queue for fast task deferral</h4>
<p>You can use <code>.queue()</code> to enqueue background work — ideal for tasks like processing user messages, sending notifications etc.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	doSomethingExpensive(payload) {&#10;		// a long running process that you want to run in the background&#10;	}&#10;&#10;	queueSomething() {&#10;		await this.queue(&quot;doSomethingExpensive&quot;, somePayload); // this will NOT block further execution, and runs in the background&#10;		await this.queue(&quot;doSomethingExpensive&quot;, someOtherPayload); // the callback will NOT run until the previous callback is complete&#10;		// ... call as many times as you want&#10;	}&#10;}&#10;</code></pre>
<p>Want to try it yourself? Just define a method like processMessage in your agent, and you’re ready to scale.</p>
<h4 id="2025-08-05-agents-MCP-update-new-email-adapter">New email adapter</h4>
<p>Want to build an AI agent that can receive and respond to emails automatically? With the new email adapter and onEmail lifecycle method, now you can.</p>
<pre><code class="language-ts">export class EmailAgent extends Agent {&#10;	async onEmail(email: AgentEmail) {&#10;		const raw = await email.getRaw();&#10;		const parsed = await PostalMime.parse(raw);&#10;&#10;		// create a response based on the email contents&#10;		// and then send a reply&#10;&#10;		await this.replyToEmail(email, {&#10;			fromName: &quot;Email Agent&quot;,&#10;			body: `Thanks for your email! You&#x27;ve sent us &quot;${parsed.subject}&quot;. We&#x27;ll process it shortly.`,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>You route incoming mail like this:</p>
<pre><code class="language-ts">export default {&#10;	async email(email, env) {&#10;		await routeAgentEmail(email, env, {&#10;			resolver: createAddressBasedEmailResolver(&quot;EmailAgent&quot;),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>You can find a full example <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">here</a>.</p>
<h4 id="2025-08-05-agents-MCP-update-automatic-context-wrapping-for-custom-methods">Automatic context wrapping for custom methods</h4>
<p>Custom methods are now automatically wrapped with the agent's context, so calling <code>getCurrentAgent()</code> should work regardless of where in an agent's lifecycle it's called. Previously this would not work on RPC calls, but now just works out of the box.</p>
<pre><code class="language-ts">export class MyAgent extends Agent {&#10;	async suggestReply(message) {&#10;		// getCurrentAgent() now correctly works, even when called inside an RPC method&#10;		const { agent } = getCurrentAgent()!;&#10;		return generateText({&#10;			prompt: `Suggest a reply to: &quot;${message}&quot; from &quot;${agent.name}&quot;`,&#10;			tools: [replyWithEmoji],&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>Try it out and tell us what you build!</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-05">Aug 5, 2025</time><div>
<h2 id="post-2025-08-05-sandbox-sdk-major-update"><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We’ve shipped a major release for the <a href="https://github.com/cloudflare/sandbox-sdk">@cloudflare/sandbox</a> SDK, turning it into a full-featured, container-based execution platform that runs securely on Cloudflare Workers.</p>
<p>This update adds live streaming of output, persistent Python and JavaScript code interpreters with rich output support (charts, tables, HTML, JSON), file system access, Git operations, full background process control, and the ability to expose running services via public URLs.</p>
<p>This makes it ideal for building AI agents, CI runners, cloud REPLs, data analysis pipelines, or full developer tools — all without managing infrastructure.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-code-interpreter-python-js-ts">Code interpreter (Python, JS, TS)</h4>
<p>Create persistent code contexts with support for rich visual + structured outputs.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-createcodecontext-options">createCodeContext(options)</h4>
<p>Creates a new code execution context with persistent state.</p>
<pre><code class="language-ts">// Create a Python context&#10;const pythonCtx = await sandbox.createCodeContext({ language: &quot;python&quot; });&#10;&#10;// Create a JavaScript context&#10;const jsCtx = await sandbox.createCodeContext({ language: &quot;javascript&quot; });&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-runcode-code-options">runCode(code, options)</h4>
<p>Executes code with optional streaming callbacks.</p>
<pre><code class="language-ts">// Simple execution&#10;const execution = await sandbox.runCode(&#x27;print(&quot;Hello World&quot;)&#x27;, {&#10;	context: pythonCtx,&#10;});&#10;&#10;// With streaming callbacks&#10;await sandbox.runCode(&#10;	`&#10;for i in range(5):&#10;    print(f&quot;Step {i}&quot;)&#10;    time.sleep(1)&#10;`,&#10;	{&#10;		context: pythonCtx,&#10;		onStdout: (output) =&gt; console.log(&quot;Real-time:&quot;, output.text),&#10;		onResult: (result) =&gt; console.log(&quot;Result:&quot;, result),&#10;	},&#10;);&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-real-time-streaming-output">Real-time streaming output</h4>
<p>Returns a streaming response for real-time processing.</p>
<pre><code class="language-ts">const stream = await sandbox.runCodeStream(&#10;	&quot;import time; [print(i) for i in range(10)]&quot;,&#10;);&#10;// Process the stream as needed&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-rich-output-handling">Rich output handling</h4>
<p>Interpreter outputs are auto-formatted and returned in multiple formats:</p>
<ul>
<li>text</li>
<li>html (e.g., Pandas tables)</li>
<li>png, svg (e.g., Matplotlib charts)</li>
<li>json (structured data)</li>
<li>chart (parsed visualizations)</li>
</ul>
<pre><code class="language-ts">const result = await sandbox.runCode(&#10;	`&#10;import seaborn as sns&#10;import matplotlib.pyplot as plt&#10;&#10;data = sns.load_dataset(&quot;flights&quot;)&#10;pivot = data.pivot(&quot;month&quot;, &quot;year&quot;, &quot;passengers&quot;)&#10;sns.heatmap(pivot, annot=True, fmt=&quot;d&quot;)&#10;plt.title(&quot;Flight Passengers&quot;)&#10;plt.show()&#10;&#10;pivot.to_dict()&#10;`,&#10;	{ context: pythonCtx },&#10;);&#10;&#10;if (result.png) {&#10;	console.log(&quot;Chart output:&quot;, result.png);&#10;}&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-preview-urls-from-exposed-ports">Preview URLs from Exposed Ports</h4>
<p>Start background processes and expose them with live URLs.</p>
<pre><code class="language-ts">await sandbox.startProcess(&quot;python -m http.server 8000&quot;);&#10;const preview = await sandbox.exposePort(8000);&#10;&#10;console.log(&quot;Live preview at:&quot;, preview.url);&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-full-process-lifecycle-control">Full process lifecycle control</h4>
<p>Start, inspect, and terminate long-running background processes.</p>
<pre><code class="language-ts">const process = await sandbox.startProcess(&quot;node server.js&quot;);&#10;console.log(`Started process ${process.id} with PID ${process.pid}`);&#10;&#10;// Monitor the process&#10;const logStream = await sandbox.streamProcessLogs(process.id);&#10;for await (const log of parseSSEStream&lt;LogEvent&gt;(logStream)) {&#10;	console.log(`Server: ${log.data}`);&#10;}&#10;</code></pre>
<ul>
<li>listProcesses() - List all running processes</li>
<li>getProcess(id) - Get detailed process status</li>
<li>killProcess(id, signal) - Terminate specific processes</li>
<li>killAllProcesses() - Kill all processes</li>
<li>streamProcessLogs(id, options) - Stream logs from running processes</li>
<li>getProcessLogs(id) - Get accumulated process output</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-git-integration">Git integration</h4>
<p>Clone Git repositories directly into the sandbox.</p>
<pre><code class="language-ts">await sandbox.gitCheckout(&quot;https://github.com/user/repo&quot;, {&#10;	branch: &quot;main&quot;,&#10;	targetDir: &quot;my-project&quot;,&#10;});&#10;</code></pre>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-05">Aug 5, 2025</time><div>
<h2 id="post-2025-08-05-openai-open-models"><a href="/changelog/post/2025-08-05-openai-open-models/">OpenAI open models now available on Workers AI</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers-ai</span></div><div class="changelog-body"><p>We're thrilled to be a Day 0 partner with <a href="http://openai.com/index/introducing-gpt-oss">OpenAI</a> to bring their <a href="https://openai.com/index/gpt-oss-model-card/">latest open models</a> to Workers AI, including support for Responses API, Code Interpreter, and Web Search (coming soon).</p>
<p>Get started with the new models at <code>@cf/openai/gpt-oss-120b</code> and <code>@cf/openai/gpt-oss-20b</code>.
Check out the <a href="https://blog.cloudflare.com/openai-gpt-oss-on-workers-ai">blog</a> for more details about the new models, and the <a href="/workers-ai/models/gpt-oss-120b"><code>gpt-oss-120b</code></a> and <a href="/workers-ai/models/gpt-oss-20b"><code>gpt-oss-20b</code></a> model pages for more information about pricing and context windows.</p>
<h4 id="2025-08-05-openai-open-models-responses-api">Responses API</h4>
If you call the model through:
- Workers Binding, it will accept/return Responses API – `env.AI.run(“@cf/openai/gpt-oss-120b”)`
- REST API on `/run` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/run/@cf/openai/gpt-oss-120b`
- REST API on new `/responses` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/responses`
- REST API for OpenAI Compatible endpoint, it will return Chat Completions (coming soon) – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/chat/completions`
<pre><code>curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/ai/v1/responses \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_KEY&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;@cf/openai/gpt-oss-120b&quot;,&#10;    &quot;reasoning&quot;: {&quot;effort&quot;: &quot;medium&quot;},&#10;    &quot;input&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What are the benefits of open-source models?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;&#10;</code></pre>
<h4 id="2025-08-05-openai-open-models-code-interpreter">Code Interpreter</h4>
The model is natively trained to support stateful code execution, and we've implemented support for this feature using our [Sandbox SDK](https://github.com/cloudflare/sandbox-sdk) and [Containers](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Cloudflare's Developer Platform is uniquely positioned to support this feature, so we're very excited to bring our products together to support this new use case.
<h4 id="2025-08-05-openai-open-models-web-search-coming-soon">Web Search (coming soon)</h4>
We are working to implement Web Search for the model, where users can bring their own Exa API Key so the model can browse the Internet.
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-04">Aug 4, 2025</time><div>
<h2 id="post-2025-08-04-builds-increased-disk-size"><a href="/changelog/post/2025-08-04-builds-increased-disk-size/">Increased disk space for Workers Builds</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>As part of the ongoing open beta for <a href="/workers/ci-cd/builds/">Workers Builds</a>, we’ve increased the available disk space for builds from <strong>8 GB</strong> to <strong>20 GB</strong> for both Free and Paid plans.</p>
<p>This provides more space for larger projects, dependencies, and build artifacts while improving overall build reliability.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Free Plan</th>
<th>Paid Plans</th>
</tr>
</thead>
<tbody>
<tr>
<td>Disk Space</td>
<td>20 GB</td>
<td>20 GB</td>
</tr>
</tbody>
</table>
<p>All other <a href="/workers/ci-cd/builds/limits-and-pricing/">build limits</a> — including CPU, memory, build minutes, and timeout remain unchanged.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-04">Aug 4, 2025</time><div>
<h2 id="post-2025-08-04-waf-release"><a href="/changelog/post/2025-08-04-waf-release/">WAF Release - 2025-08-04</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's highlight focuses on a series of significant vulnerabilities identified across widely adopted web platforms, from enterprise-grade CMS to essential backend administration tools. The findings reveal multiple vectors for attack, including critical flaws that allow for full server compromise and others that enable targeted attacks against users.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Sitecore (CVE-2025-34509, CVE-2025-34510, CVE-2025-34511): A hardcoded credential allows remote attackers to access administrative APIs. Once authenticated, they can exploit an additional vulnerability to upload arbitrary files, leading to remote code execution.</p>
</li>
<li>
<p>Grafana (CVE-2025-4123): A cross-site scripting (XSS) vulnerability allows an attacker to redirect users to a malicious website, which can then execute arbitrary JavaScript in the victim's browser.</p>
</li>
<li>
<p>LaRecipe (CVE-2025-53833): Through Server-Side Template Injection, attackers can execute arbitrary commands on the server, potentially access sensitive environment variables, and escalate access depending on server configuration.</p>
</li>
<li>
<p>CentOS WebPanel (CVE-2025-48703): A command injection vulnerability could allow a remote attacker to execute arbitrary commands on the server.</p>
</li>
<li>
<p>WordPress (CVE-2023-5561): This vulnerability allows unauthenticated attackers to determine the email addresses of users who have published public posts on an affected website.</p>
</li>
<li>
<p>WordPress Plugin - WPBookit (CVE-2025-6058): A missing file type validation allows unauthenticated attackers to upload arbitrary files to the server, creating the potential for remote code execution.</p>
</li>
<li>
<p>WordPress Theme - Motors (CVE-2025-4322): Due to improper identity validation, an unauthenticated attacker can change the passwords of arbitrary users, including administrators, to gain access to their accounts.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities pose a multi-layered threat to widely adopted web technologies, ranging from enterprise-grade platforms like Sitecore to everyday solutions such as WordPress, and backend tools like CentOS WebPanel. The most severe risks originate in remote code execution (RCE) flaws found in Sitecore, CentOS WebPanel, LaRecipe, and the WPBookit plugin. These allow attackers to bypass security controls and gain deep access to the server, enabling them to steal sensitive data, deface websites, install persistent malware, or use the compromised server as a launchpad for further attacks.</p>
<p>The privilege escalation vulnerability is the Motors theme, which allows for a complete administrative account takeover on WordPress sites. This effectively hands control of the application to an attacker, who can then manipulate content, exfiltrate user data, and alter site functionality without needing to breach the server itself.</p>
<p>The Grafana cross-site scripting (XSS) flaw can be used to hijack authenticated user sessions or steal credentials, turning a trusted user's browser into an attack vector.</p>
<p>Meanwhile, the information disclosure flaw in WordPress core provides attackers with valid user emails, fueling targeted phishing campaigns that aim to secure the same account access achievable through the other exploits.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b8ab4644f8044f3485441ee052f30a13">52f30a13</code>
</td>
<td>100535A</td>
<td>Sitecore - Dangerous File Upload - CVE:CVE-2025-34510, CVE:CVE-2025-34511</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="06d1fe0bd6e44d868e6b910b5045a97f">5045a97f</code>
</td>
<td>100535</td>
<td>Sitecore - Information Disclosure - CVE:CVE-2025-34509</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="f71ce87ea6e54eab999223df579cd3e0">579cd3e0</code>
</td>
<td>100543</td>
<td>Grafana - Directory Traversal - CVE:CVE-2025-4123</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="bba3d37891a440fb8bc95b970cbd9abc">0cbd9abc</code>
</td>
<td>100545</td>
<td>WordPress - Information Disclosure - CVE:CVE-2023-5561</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="28108d25f1cf470c8e7648938f634977">8f634977</code>
</td>
<td>100820</td>
<td>CentOS WebPanel - Remote Code Execution - CVE:CVE-2025-48703</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9d69c796a61444a3aca33dc282ae64c1">82ae64c1</code>
</td>
<td>100821</td>
<td>LaRecipe - SSTI - CVE:CVE-2025-53833</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9b5c5e13d2ca4253a89769f2194f7b2d">194f7b2d</code>
</td>
<td>100822</td>
<td>WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="69d43d704b0641898141a4300bf1b661">0bf1b661</code>
</td>
<td>100823</td>
<td>WordPress:Theme:Motors - Privilege Escalation - CVE:CVE-2025-4322</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-01">Aug 1, 2025</time><div>
<h2 id="post-2025-08-01-terraform-v5.8.2-provider"><a href="/changelog/post/2025-08-01-terraform-v5.8.2-provider/">Terraform v5.8.2 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and reliability. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_custom_pages`
  - `cloudflare_page_rule`
  - `cloudflare_dns_record`
  - `cloudflare_argo_tiered_caching`
- Addressed chronic drift issues in `cloudflare_logpush_job`, `cloudflare_zero_trust_dns_location`, `cloudflare_ruleset` & `cloudflare_api_token`
- `cloudflare_zone_subscription` returns expected values `rate_plan.id` from former versions
- `cloudflare_workers_script` can now successfully be destroyed with bindings & migration for Durable Objects now recorded in tfstate 
- Ability to configure `add_headers` under `cloudflare_zero_trust_gateway_policy` 
- Other bug fixes
<p>For a more detailed look at all of the changes, see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.2">changelog</a> in GitHub.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-issues-closed">Issues Closed</h4>
- [#5666: cloudflare_ruleset example lists id which is a read-only field](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5666)
- [#5578: cloudflare_logpush_job plan always suggests changes](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5578)
- [#5552: 5.4.0: Since provider update, existing cloudflare_list_item would be recreated "created" state](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5552)
- [#5670: cloudflare_zone_subscription: uses wrong ID field in Read/Update](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5670)
- [#5548: cloudflare_api_token resource always shows changes (drift)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5548)
- [#5634: cloudflare_workers_script with bindings fails to be destroyed](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5634)
- [#5616: cloudflare_workers_script Unable to deploy worker assets](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5616)
- [#5331: cloudflare_workers_script 500 internal server error when uploading python](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5331)
- [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5704: cloudflare_workers_script randomly fails to deploy when changing compatibility_date](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5704)
- [#5439: cloudflare_workers_script (v5.2.0) ignoring content and bindings properties](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5439)
- [#5522: cloudflare_workers_script always detects changes after apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5522)
- [#5693: cloudflare_zero_trust_access_identity_provider gives recurring change on OTP pin login](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5693)
- [#5567: cloudflare_r2_custom_domain doesn't roundtrip jurisdiction properly](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5567)
- [#5179: Bad request with when creating cloudflare_api_shield_schema resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5179)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-01">Aug 1, 2025</time><div>
<h2 id="post-2025-08-01-containers-in-vite-dev"><a href="/changelog/post/2025-08-01-containers-in-vite-dev/">Develop locally with Containers and the Cloudflare Vite plugin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now configure and run <a href="/containers">Containers</a> alongside your <a href="/workers">Worker</a> during local development when using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>. Previously, you could only develop locally when using <a href="/workers/wrangler/">Wrangler</a> as your local development server.</p>
<h4 id="2025-08-01-containers-in-vite-dev-configuration">Configuration</h4>
<p>You can simply configure your Worker and your Container(s) in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17782.md")</div>
<h4 id="2025-08-01-containers-in-vite-dev-worker-code">Worker Code</h4>
<p>Once your Worker and Containers are configured, you can access the Container instances from your Worker code:</p>
<pre><code class="language-ts">import { Container, getContainer } from &quot;@cloudflare/containers&quot;;&#10;&#10;export class MyContainer extends Container {&#10;  defaultPort = 4000; // Port the container is listening on&#10;  sleepAfter = &quot;10m&quot;; // Stop the instance if requests not sent for 10 minutes&#10;}&#10;&#10;async fetch(request, env) {&#10;  const { &quot;session-id&quot;: sessionId } = await request.json();&#10;  // Get the container instance for the given session ID&#10;  const containerInstance = getContainer(env.MY_CONTAINER, sessionId)&#10;  // Pass the request to the container instance on its default port&#10;  return containerInstance.fetch(request);&#10;}&#10;</code></pre>
<h4 id="2025-08-01-containers-in-vite-dev-local-development">Local development</h4>
<p>To develop your Worker locally, start a local dev server by running</p>
<pre><code class="language-sh">vite dev&#10;</code></pre>
<p>in your terminal.</p>
<h4 id="2025-08-01-containers-in-vite-dev-resources">Resources</h4>
<p>Learn more about <a href="https://developers.cloudflare.com/containers/">Cloudflare Containers</a> or the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a> in our developer docs.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-31">Jul 31, 2025</time><div>
<h2 id="post-2025-07-31-terraform-v5-tunnels-routes"><a href="/changelog/post/2025-07-31-terraform-v5-tunnels-routes/">Terraform V5 support for tunnels and routes</a></h2>
<div class="changelog-badges"><span>cloudflare-wan</span></div><div class="changelog-body"><p>The Cloudflare Terraform provider resources for Cloudflare WAN tunnels and routes now support Terraform provider version 5. Customers using infrastructure-as-code workflows can manage their tunnel and route configuration with the latest provider version.</p>
<p>For more information, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-30">Jul 30, 2025</time><div>
<h2 id="post-2025-07-30-mt-mwan-health-check-cmb-eu"><a href="/changelog/post/2025-07-30-mt-mwan-health-check-cmb-eu/">Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.</a></h2>
<div class="changelog-badges"><span>magic-transit</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Today, we are excited to announce that all Magic Transit and Magic WAN customers with CMB EU (<a href="/data-localization/metadata-boundary/">Customer Metadata Boundary - Europe</a>) enabled in their account will be able to access GRE, IPsec, and CNI health check and traffic volume data in the Cloudflare dashboard and via API.</p>
<p>This ensures that all Magic Transit and Magic WAN customers with CMB EU enabled will be able to access all Magic Transit and Magic WAN features.</p>
<p>Specifically, these two GraphQL endpoints are now compatible with CMB EU:</p>
<ul>
<li><code>magicTransitTunnelHealthChecksAdaptiveGroups</code></li>
<li><code>magicTransitTunnelTrafficAdaptiveGroups</code></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-29">Jul 29, 2025</time><div>
<h2 id="post-2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets"><a href="/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/">Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets</a></h2>
<div class="changelog-badges"><span>workers</span><span>secrets-store</span></div><div class="changelog-body"><p>Any template which uses <a href="/workers/configuration/environment-variables/">Worker environment variables</a>, <a href="/workers/configuration/secrets/">secrets</a>, or <a href="/secrets-store/">Secrets Store secrets</a> can now be deployed using a <a href="/workers/platform/deploy-buttons/">Deploy to Cloudflare button</a>.</p>
<p>Define environment variables and secrets store bindings in your Wrangler configuration file as normal:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17781.md")</div>
<p>Add secrets to a <code>.dev.vars.example</code> or <code>.env.example</code> file:</p>
<pre><code class="language-ini">COOKIE_SIGNING_KEY=my-secret # comment&#10;</code></pre>
<p>And optionally, you can add a description for these bindings in your template's <code>package.json</code> to help users understand how to configure each value:</p>
<pre><code class="language-json">{&#10;	&quot;name&quot;: &quot;my-worker&quot;,&#10;	&quot;private&quot;: true,&#10;	&quot;cloudflare&quot;: {&#10;		&quot;bindings&quot;: {&#10;			&quot;API_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Select your company&#x27;s API key for connecting to the example service.&quot;&#10;			},&#10;			&quot;COOKIE_SIGNING_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Generate a random string using `openssl rand -hex 32`.&quot;&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>These secrets and environment variables will be presented to users in the dashboard as they deploy this template, allowing them to configure each value. Additional information about creating templates and Deploy to Cloudflare buttons can be found in <a href="/workers/platform/deploy-buttons/">our documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-29">Jul 29, 2025</time><div>
<h2 id="post-2025-07-29-audit-logs-v2-ui-beta"><a href="/changelog/post/2025-07-29-audit-logs-v2-ui-beta/">Audit logs (version 2) - UI Beta Release</a></h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>The Audit Logs v2 UI is now available to all Cloudflare customers in Beta. This release builds on the public <a href="/changelog/product/audit-logs/">Beta of the Audit Logs v2 API</a> and introduces a redesigned user interface with powerful new capabilities to make it easier to investigate account activity.</p>
<p><strong>Enabling the new UI</strong></p>
<p>To try the new user interface, go to <strong>Manage Account &gt; Audit Logs</strong>. The previous version of Audit Logs remains available and can be re-enabled at any time using the <strong>Switch back to old Audit Logs</strong> link in the banner at the top of the page.</p>
<p><strong>New Features:</strong></p>
<ul>
<li><strong>Advanced Filtering</strong>: Filter logs by actor, resource, method, and more for faster insights.</li>
<li><strong>On-hover filter controls</strong>: Easily include or exclude values in queries by hovering over fields within a log entry.</li>
<li><strong>Detailed Log Sidebar</strong>: View rich context for each log entry without leaving the main view.</li>
<li><strong>JSON Log View</strong>: Inspect the raw log data in a structured JSON format.</li>
<li><strong>Custom Time Ranges</strong>: Define your own time windows to view historical activity.</li>
<li><strong>Infinite Scroll</strong>: Seamlessly browse logs without clicking through pages.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_filters.png" alt="Audit Logs v2 new UI" /></p>
<p>For more details on Audit Logs v2, see the <a href="https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>
<p><strong>Known issues</strong></p>
<ul>
<li>A small number of audit logs may currently be unavailable in Audit Logs v2. In some cases, certain fields such as actor information may be missing in certain audit logs. We are actively working to improve coverage and completeness for General Availability.</li>
<li>Export to CSV is not supported in the new UI.</li>
</ul>
<p>We are actively refining the Audit Logs v2 experience and welcome your feedback. You can share overall feedback by clicking the thumbs up or thumbs down icons at the top of the page, or provide feedback on specific audit log entries using the thumbs icons next to each audit log line or by filling out our <a href="https://docs.google.com/forms/d/e/1FAIpQLSfXGkJpOG1jUPEh-flJy9B13icmcdBhveFwe-X0EzQjJQnQfQ/viewform?usp=sharing">feedback form</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-28">Jul 28, 2025</time><div>
<h2 id="post-2025-07-28-br-pricing"><a href="/changelog/post/2025-07-28-br-pricing/">Introducing pricing for the Browser Rendering API — $0.09 per browser hour</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We’ve launched pricing for <a href="/browser-run/">Browser Rendering</a>, including a free tier and a pay-as-you-go model that scales with your needs. Starting <strong>August 20, 2025</strong>, Cloudflare will begin billing for Browser Rendering.</p>
<p>There are two ways to use Browser Rendering. Depending on the method you use, here’s how billing will work:</p>
<ul>
<li><a href="/browser-run/quick-actions/"><strong>REST API</strong></a>: Charged for <strong>Duration</strong> only ($/browser hour)</li>
<li><a href="/browser-run/#integration-methods"><strong>Browser Sessions</strong></a>: Charged for both <strong>Duration</strong> and <strong>Concurrency</strong> ($/browser hour and # of concurrent browsers)</li>
</ul>
<p>Included usage and pricing by plan</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Included duration</th>
<th>Included concurrency</th>
<th>Price (beyond included)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Free</strong></td>
<td>10 minutes per day</td>
<td>3 concurrent browsers</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>10 hours per month</td>
<td>10 concurrent browsers (averaged monthly)</td>
<td><strong>1. REST API</strong>: $0.09 per additional browser hour <br /><strong>2. Workers Bindings</strong>: $0.09 per additional browser hour <br /> $2.00 per additional concurrent browser</td>
</tr>
</tbody>
</table>
<p>What you need to know:</p>
<ul>
<li><strong>Workers Free Plan:</strong> 10 minutes of browser usage per day with 3 concurrent browsers at no charge.</li>
<li><strong>Workers Paid Plan:</strong> 10 hours of browser usage per month with 10 concurrent browsers (averaged monthly) at no charge. Additional usage is charged as shown above.</li>
</ul>
<p>You can monitor usage via the <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">Cloudflare dashboard</a>. Go to <strong>Compute</strong> &gt; <strong>Browser Run</strong>.</p>
<p><img src="/assets/upstream/images/browser-run/dashboard.png" alt="Browser Rendering dashboard" /></p>
<p>If you've been using Browser Rendering and do not wish to incur charges, ensure your usage stays within your plan's <a href="/browser-run/pricing/">included usage</a>. To estimate costs, take a look at these <a href="/browser-run/pricing/#examples-of-workers-paid-pricing">example pricing scenarios</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-28">Jul 28, 2025</time><div>
<h2 id="post-2025-07-28-Spam-domain-category-introduced"><a href="/changelog/post/2025-07-28-Spam-domain-category-introduced/">Scam domain category introduced under Security Threats</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>We have introduced a new Security Threat category called <strong>Scam</strong>. Relevant domains are marked with the Scam category. Scam typically refers to fraudulent websites and schemes designed to trick victims into giving away money or personal information.</p>
<p><strong>New category added</strong></p>
<table>
<thead>
<tr>
<th>Parent ID</th>
<th>Parent Name</th>
<th>Category ID</th>
<th>Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>191</td>
<td>Scam</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/37/">Previous</a><span>Page 38 of 50</span><a class="pagination-next" rel="next" href="/changelog/39/">Next</a></nav>
</div>
