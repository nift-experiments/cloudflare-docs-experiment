<p>Generate a public/private key pair using the Cloudflare <a href="https://github.com/cloudflare/matched-data-cli"><code>matched-data-cli</code></a> command-line tool. After generating a key pair, enter the generated public key in the payload logging configuration.</p>
<p>Do the following:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15660.md")
</div>
<p>After generating the key pair, copy the public key value and enter it in the payload logging configuration.</p>
<h2 id="troubleshooting-macos-errors">Troubleshooting macOS errors</h2>
<p>If you are using macOS, the operating system may block the <code>matched-data-cli</code> tool, depending on your security settings.</p>
<p>For instructions on how to execute unsigned binaries like the <code>matched-data-cli</code> tool in macOS, refer to the <a href="https://support.apple.com/en-us/102445#openanyway">Safely open apps on your Mac</a> page in Apple Support.</p>
