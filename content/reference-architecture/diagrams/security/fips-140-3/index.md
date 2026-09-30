<h2 id="introduction">Introduction</h2>
<p>This document outlines a reference architecture for achieving Federal Information Processing Standard (FIPS) 140 Level 3 compliance using Cloudflare's Application Services. FIPS 140 is a U.S. government standard that specifies security requirements for cryptographic modules protecting sensitive information in computer and telecommunication systems.</p>
<p>FIPS 140 defines four security levels, with Level 3 being the most stringent for non-military applications. It mandates physical tamper-resistance to prevent unauthorized access to cryptographic keys and critical security parameters. This includes measures like robust enclosures, tamper-evident seals, and identity-based authentication.</p>
<p>Achieving FIPS 140 compliance, particularly Level 3, is crucial for organizations handling sensitive data, especially those in regulated industries like:</p>
<ul>
<li><strong>Government</strong>: Federal agencies and contractors processing sensitive government information.</li>
<li><strong>Healthcare</strong>: Organizations handling protected health information (PHI) under HIPAA.</li>
<li><strong>Financial</strong> Services: Institutions dealing with financial transactions and customer data.</li>
<li><strong>Defense</strong>: Contractors working on defense projects requiring stringent security measures.</li>
</ul>
<p>FIPS 140 compliance demonstrates a strong commitment to data security, builds trust with customers and partners, and ensures adherence to regulatory requirements. This reference architecture provides a comprehensive guide to leveraging Cloudflare's robust security features to meet these stringent standards.</p>
<h2 id="fips-140-3-levels">FIPS 140-3 levels</h2>
<p>Organizations use the FIPS 140-3 standard to ensure that the hardware they select meets specific security requirements. The FIPS certification standard defines four increasing, qualitative levels of security.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12719.md")
</div></div>
<h2 id="key-components">Key components</h2>
<ul>
<li><strong>Cloudflare Keyless SSL</strong>: A service that allows organizations to use Cloudflare's SSL/TLS protection while keeping their private keys securely stored in their own infrastructure, ensuring private keys remain under their control and never leave their premises, while still benefiting from Cloudflare's DDoS protection and performance optimization features.</li>
<li><strong>Cloudflare Tunnel</strong>: Provides a secure, encrypted connection between Cloudflare's global network and the private infrastructure hosting CloudHSM, protecting data in transit.</li>
<li><strong>Hardware Security module</strong>: A FIPS 140 Level 3 compliant HSM that securely manages cryptographic keys. Cloudflare supports a handful of HSMs, including AWS CloudHSM, Azure Key Vault, and Google Cloud KMS.</li>
</ul>
<h2 id="architecture-overview">Architecture overview</h2>
<p>The architecture diagram below illustrates the key components and data flow for achieving FIPS 140 Level 3 compliance with Cloudflare Application Services and all its required components.</p>
<div style={{ display: 'flex', justifyContent: 'center', width: '100%' }}>
<pre><code class="language-mermaid">flowchart TB&#10;  User((User/Client)) --&gt; |1.SNI = keyless.example.com| CF[Cloudflare Edge Network]&#10;&#10;  subgraph CF [Cloudflare Edge]&#10;      KeylessSSL[Keyless SSL Service]&#10;  end&#10;&#10;  subgraph Private[Private Infrastructure]&#10;      Tunnel[Cloudflare Tunnel]&#10;      HSM[Hardware Security Module]&#10;  		KeylessModule[Keyless Module]&#10;  end&#10;&#10;  Tunnel --&gt;|2.Establish tunnel| KeylessSSL&#10;  KeylessSSL --&gt;|3.Keyless operation required| Tunnel&#10;  Tunnel --&gt;|4.Forward to HSM| KeylessModule&#10;  KeylessModule --&gt;|5.Key Operations via PKCS11| HSM&#10;&#10;  classDef cloudflare fill:#F6821F,stroke:#fff,stroke-width:2px,color:#fff&#10;  classDef aws fill:#232F3E,stroke:#fff,stroke-width:2px,color:#fff&#10;  classDef default fill:#fff,stroke:#000,stroke-width:2px, color:#000&#10;&#10;  class CF,KeylessSSL,Tunnel,KeylessModule cloudflare&#10;  class HSM aws&#10;  class User default&#10;</code></pre>
</div>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12720.md")
</div>
<h2 id="further-reading">Further reading</h2>
- [Cloudflare Keyless SSL](/ssl/keyless-ssl)
- [Cloudflare Tunnel](/cloudflare-one/networks/connectors/cloudflare-tunnel/)
- [Keyless SSL with secured Tunnel](/ssl/keyless-ssl/configuration/cloudflare-tunnel/)
- Supported HSMs:
	<ul class="directory-listing"><li><a href="/ssl/keyless-ssl/hardware-security-modules/configuration/">Configuration</a><p>Configure the key server to work with hardware security modules.</p></li><li><a href="/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/">AWS cloud HSM</a><p>Learn how to use Keyless SSL with AWS CloudHSM.</p></li><li><a href="/ssl/keyless-ssl/hardware-security-modules/azure-dedicated-hsm/">Azure Dedicated HSM</a><p>Learn how to use Keyless SSL with Azure Dedicated HSM.</p></li><li><a href="/ssl/keyless-ssl/hardware-security-modules/azure-managed-hsm/">Azure Managed HSM</a><p>This tutorial uses Microsoft Azure&#x27;s Managed HSM to deploy a VM with the Keyless SSL daemon. Follow these instructions to deploy your keyless server.</p></li><li><a href="/ssl/keyless-ssl/hardware-security-modules/entrust-nshield-connect/">Entrust nShield Connect</a><p>Learn how to use Keyless SSL with Entrust nShield Connect.</p></li><li><a href="/ssl/keyless-ssl/hardware-security-modules/fortanix-dsm/">Fortanix Data Security Manager</a><p>Configure Keyless SSL with Fortanix Data Security Manager.</p></li><li><a href="/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/">Google Cloud HSM</a><p>Learn how to use Keyless SSL with Google Cloud HSM.</p></li><li><a href="/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/">IBM Cloud HSM</a><p>Learn how to use Keyless SSL with IBM Cloud HSM.</p></li><li><a href="/ssl/keyless-ssl/hardware-security-modules/softhsmv2/">SoftHSMv2</a><p>Learn how to use Keyless SSL with SoftHSMv2.</p></li></ul>
<pre><code>&#10;</code></pre>
