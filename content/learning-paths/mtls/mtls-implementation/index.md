<p>There are different ways to implement mTLS authentication. The most common ones are:</p>
<h2 id="option-1-mtls-device-authentication">Option 1: mTLS Device Authentication</h2>
<p>This version of mTLS is for device certificates, primarily focused on the number of IoT devices, not user devices.</p>
<p>Here we recommend using <a href="/learning-paths/mtls/mtls-app-security/">mTLS with Application Security</a>.</p>
<h2 id="option-2-mtls-user-authentication">Option 2: mTLS User Authentication</h2>
<p>When a user wants to establish a secure connection with a server, they present their certificate to the server, which verifies its authenticity. Once the certificate is authenticated, an encrypted connection is established between the user and the server, and all data transmitted between them is encrypted to protect against interception by third parties.</p>
<p>mTLS user authentication is included with Cloudflare Access and depends on the number of users.</p>
<h2 id="option-3-mtls-service-authentication">Option 3: mTLS Service Authentication</h2>
<p>The hostnames are used to look up the certificates and verify their authenticity. Once the connection is established, all data transmitted between the hosts is encrypted, ensuring that it cannot be intercepted and read by third parties. Here the main driver is the number of hostnames.</p>
