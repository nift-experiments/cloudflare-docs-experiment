<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9833.md")
</aside>
<p>Setting up <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">mTLS</a> with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> can help in cases where the customer:</p>
<ul>
<li>Already has existing Client Certificates on devices.</li>
<li>Needs to protect Access applications with <a href="/ssl/client-certificates/byo-ca/">Bring Your Own CA (BYOCA)</a>.</li>
<li>Needs to integrate with a Zero Trust solution.</li>
</ul>
<h2 id="1-create-a-ca"><ol>
<li>Create a CA</li>
</ol></h2>
<p>The CA certificate can be from a publicly trusted CA or self-signed.</p>
<p>In case you want to <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#test-mtls-using-cloudflare-pki">create your own CA</a> from scratch, you can follow these example steps and adapt the information to your own needs:</p>
<ol>
<li>Create a JSON file called <code>ca-csr.json</code>:</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;CN&quot;: &quot;Cloudflare Access Testing CA&quot;,&#10;	&quot;key&quot;: {&#10;		&quot;algo&quot;: &quot;rsa&quot;,&#10;		&quot;size&quot;: 4096&#10;	},&#10;	&quot;names&quot;: [&#10;		{&#10;			&quot;C&quot;: &quot;US&quot;,&#10;			&quot;L&quot;: &quot;LA&quot;,&#10;			&quot;O&quot;: &quot;Access Testing&quot;,&#10;			&quot;OU&quot;: &quot;CA&quot;,&#10;			&quot;ST&quot;: &quot;California&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<ol start="2">
<li>Create a JSON file called <code>ca-config.json</code>:</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;signing&quot;: {&#10;		&quot;default&quot;: {&#10;			&quot;expiry&quot;: &quot;8760h&quot;&#10;		},&#10;		&quot;profiles&quot;: {&#10;			&quot;server&quot;: {&#10;				&quot;usages&quot;: [&quot;signing&quot;, &quot;key encipherment&quot;, &quot;server auth&quot;],&#10;				&quot;expiry&quot;: &quot;8760h&quot;&#10;			},&#10;			&quot;client&quot;: {&#10;				&quot;usages&quot;: [&quot;signing&quot;, &quot;key encipherment&quot;, &quot;client auth&quot;],&#10;				&quot;expiry&quot;: &quot;8760h&quot;&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<ol start="3">
<li>Run the following <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#test-mtls-using-cloudflare-pki">cfssl</a> command to generate the CA certificate <code>ca.pem</code>:</li>
</ol>
<pre><code class="language-txt">cfssl gencert -initca ca-csr.json | cfssljson -bare ca&#10;</code></pre>
<h2 id="2-create-client-certificates"><ol start="2">
<li>Create Client Certificates</li>
</ol></h2>
<ol>
<li>In order to create the Client Certificates, you need to prepare the following JSON file called <code>client-csr.json</code>:</li>
</ol>
<pre><code class="language-json">{&#10;    &quot;CN&quot;: &quot;mtls-access.example.com&quot;,        # replace with your own hostname&#10;    &quot;hosts&quot;: [&quot;mtls-access.example.com&quot;],   # replace with your own hostname&#10;    &quot;key&quot;: {&#10;      &quot;algo&quot;: &quot;rsa&quot;,&#10;      &quot;size&quot;: 4096&#10;    },&#10;    &quot;names&quot;: [&#10;      {&#10;        &quot;C&quot;: &quot;US&quot;,&#10;        &quot;L&quot;: &quot;Austin&quot;,&#10;        &quot;O&quot;: &quot;Access&quot;,&#10;        &quot;OU&quot;: &quot;Access Admins&quot;,&#10;        &quot;ST&quot;: &quot;Texas&quot;&#10;      }&#10;    ]&#10;  }&#10;</code></pre>
<ol start="2">
<li>Now you can run the following command to generate the Client Certificates, which will output the files <code>client.pem</code>, <code>client-key.pem</code> and <code>client.csr</code>:</li>
</ol>
<pre><code class="language-sh">cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=client client-csr.json | cfssljson -bare client&#10;</code></pre>
<h2 id="3-add-mtls-ca-certificate-to-cloudflare-access"><ol start="3">
<li>Add mTLS CA certificate to Cloudflare Access</li>
</ol></h2>
<p>Follow the steps outlined in the <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#add-mtls-authentication-to-your-access-configuration">developer documentation</a>.</p>
<p>Using the example from Step 2: upload the <code>ca.pem</code> to your Cloudflare Access account via the <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#add-mtls-authentication-to-your-access-configuration">dashboard</a> or <a href="/api/resources/zero_trust/subresources/access/subresources/certificates/methods/create/">Cloudflare API</a>.</p>
<p>Do not forget to enter the fully-qualified domain names (FQDN / associated hostnames) that will use this CA certificate.</p>
<p>Customers can identify which client sends the Client Certificates by <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#forward-a-client-certificate">forwarding client certificate headers</a> to the origin server. Customers can then store and use the certificate information such as Common Name (CN), Serial number, and other fields along with the device number to perform additional checks or logics.</p>
<p>Additionally, authenticated requests also send the <code>Cf-Access-Jwt-Assertion\</code> JWT header to the origin server. To decode the header value, you can use <a href="https://jwt.io/">jwt.io</a>.</p>
<h2 id="4-create-the-self-hosted-applications"><ol start="4">
<li>Create the self-hosted applications</li>
</ol></h2>
<p>Finally, the hostname you want to protect with mTLS needs to be added as a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted app</a> in Cloudflare Access, defining an <a href="/cloudflare-one/access-controls/policies/">Access Policy</a> which uses the action <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth</a> and the Selector <em>&quot;Valid Certificate&quot;</em>, or simply requiring an <a href="/cloudflare-one/integrations/identity-providers/">IdP</a> authentication. You can also take advantage of extra requirements, such as the &quot;Common Name&quot; (CN), which expects the indicated hostname, and more <a href="/cloudflare-one/access-controls/policies/#selectors">Selectors</a>. Alternatively, one can also <a href="/reference-architecture/diagrams/sase/augment-access-with-serverless/">extend ZTNA with external authorization and serverless computing</a>.</p>
<h2 id="demo">Demo</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9832.md")
</aside>
<p>With the Public and Private Client Certificates in the same directory, with this cURL command, we will gain access:</p>
<pre><code class="language-sh">curl -IXGET --cert client.pem --key client-key.pem https://mtls-access.example.com/&#10;</code></pre>
<pre><code class="language-txt">HTTP/2 200&#10;server: cloudflare&#10;</code></pre>
<p>Without the certificates, we would see the following:</p>
<pre><code class="language-sh">curl -I https://mtls-access.example.com/mtls-test&#10;</code></pre>
<pre><code class="language-txt">HTTP/2 401&#10;server: cloudflare&#10;</code></pre>
