<p>When you enable <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#turn-on-tls-decryption">TLS decryption</a>, you can review the prompts and responses for supported AI applications. This allows you to understand three key things about AI application usage:</p>
<ul>
<li>The sanctioned and unsanctioned AI tools your users are engaging with.</li>
<li>How they are interacting with them.</li>
<li>What information they are sharing.</li>
</ul>
<p><img src="/assets/upstream/images/learning-paths/holistic-ai-security/gateway-prompt-log.png" alt="Log entry for a prompt detected using AI prompt protection." /></p>
<p>You can use this in conjunction with <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> to detect sensitive data potentially being used in prompts, with or without explicitly blocking the action. You can use DLP to log AI prompt topics by turning on <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#turn-on-ai-prompt-content-logging-for-a-dlp-policy">Capture generative AI prompt content in logs</a> for the policy.</p>
