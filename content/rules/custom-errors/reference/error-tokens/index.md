<h2 id="for-error-pages">For Error Pages</h2>
<p>Each custom error token provides diagnostic information or specific functionality that appears on the error page. Certain error pages require a page-specific custom error token.</p>
<p>To display a custom page for each error, create a separate page per error. For example, to create an error page for both <strong>IP/Country Block</strong> and <strong>Interactive Challenge</strong>, you must design and publish two separate pages.</p>
<p>The following custom error tokens are required by their respective error pages:</p>
<table>
<thead>
<tr>
<th>Token</th>
<th>Required for</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>::CAPTCHA_BOX::</code></td>
<td>Interactive Challenge <br/>Country Challenge (Managed Challenge)<br/>Managed Challenge / I'm Under Attack Mode (Interstitial Page)</td>
</tr>
<tr>
<td><code>::IM_UNDER_ATTACK_BOX::</code></td>
<td>Non-Interactive Challenge</td>
</tr>
<tr>
<td><code>::CLOUDFLARE_ERROR_500S_BOX::</code></td>
<td>5XX Errors</td>
</tr>
<tr>
<td><code>::CLOUDFLARE_ERROR_1000S_BOX::</code></td>
<td>1XXX Errors</td>
</tr>
</tbody>
</table>
<p>Each custom error token has a default look and feel. However, you can use CSS to stylize each custom error tag using each tag's class ID. All the external resources like images, CSS, and scripts will be inlined during the process. As such, all external resources need to be available (that is, they must return <code>200 OK</code>) otherwise an error will be thrown.</p>
<h2 id="for-custom-error-assets-inline-responses-and-error-pages">For Custom Error Assets, inline responses, and Error Pages</h2>
<p>A custom error asset, inline response, or error page may also include the following error tokens, which will be replaced with their real values before sending the response to the visitor:</p>
<table>
<thead>
<tr>
<th>Token</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>::CLIENT_IP::</code></td>
<td>The visitor's IP address.</td>
</tr>
<tr>
<td><code>::RAY_ID::</code></td>
<td>A unique identifier given to every request that goes through Cloudflare.</td>
</tr>
<tr>
<td><code>::GEO::</code></td>
<td>The country or region associated with the visitor's IP address.</td>
</tr>
</tbody>
</table>
