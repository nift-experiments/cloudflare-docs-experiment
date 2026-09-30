<p>In addition to private keys stored on disk, Keyless SSL supports keys stored in a Hardware Security Module (HSM) via the PKCS#11 standard. Keyless uses PKCS#11 for signing and decrypting payloads without having direct access to the private keys.</p>
<hr />
<h2 id="why-use-keyless-ssl-with-an-hsm">Why use Keyless SSL with an HSM?</h2>
<p>Hardware Security Modules (HSMs) facilitate a higher level of protection for your private keys over storing them directly on your key server. The primary responsibility of an HSM is safeguarding private keys and performing operations such as signing or encryption internally. In addition to access control, that means the physical device must offer some degree of tamper-resistance in order to be compliant with government or <a href="https://csrc.nist.gov/pubs/fips/140-3/final">industry regulations such as FIPS 140</a>.</p>
<p>Moreover, many HSMs are also capable of generating keys and producing cryptographically secure randomness. Some are purpose-built to perform cryptographic computations more efficiently.</p>
<hr />
<h2 id="communicating-using-pkcs-11">Communicating using PKCS#11</h2>
<p>The key server communicates with HSMs via PKCS#11, so any HSM supporting the standard can be used with Keyless SSL.</p>
<h3 id="initial-configuration">Initial configuration</h3>
<p>For more details on initializing your PKCS#11 token, refer to <a href="/ssl/keyless-ssl/hardware-security-modules/configuration/">Configuration</a>.</p>
<h3 id="compatibility">Compatibility</h3>
<p>Keyless SSL has interoperability with the following modules:</p>
<ul>
<li><a href="https://www.entrust.com/digital-security/hsm">Entrust nShield Connect</a></li>
<li><a href="https://cpl.thalesgroup.com/compliance/fips-common-criteria-validations">Gemalto SafeNet Luna</a></li>
<li><a href="https://github.com/opendnssec/SoftHSMv2">SoftHSMv2</a></li>
<li><a href="https://www.yubico.com/product/yubikey-neo/">YubiKey Neo</a></li>
</ul>
<p>Also, the following cloud HSM offerings have been tested with Keyless SSL:</p>
<ul>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/">AWS CloudHSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/azure-dedicated-hsm/">Azure Dedicated HSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/azure-managed-hsm/">Azure Managed HSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/fortanix-dsm/">Fortanix DSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/">IBM Cloud HSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/">Google Cloud HSM</a></li>
</ul>
