"""Shared validation for digest-bound CP8 evidence."""
import json


def validate_deployment(parser, provenance_path, attestation_path, candidate_url, upstream_sha):
    if bool(provenance_path) != bool(attestation_path):
        parser.error('--candidate-provenance and --deployment-attestation must be used together')
    if not provenance_path:
        return None, None
    provenance = json.loads(provenance_path.read_text())
    attestation = json.loads(attestation_path.read_text())
    if provenance.get('upstreamSha') != upstream_sha:
        parser.error('candidate provenance upstream SHA mismatch')
    if not attestation.get('verified'):
        parser.error('deployment attestation is not verified')
    if attestation.get('candidateProvenance') != provenance:
        parser.error('deployment attestation candidate provenance mismatch')
    if attestation.get('url', '').rstrip('/') != candidate_url.rstrip('/'):
        parser.error('deployment attestation URL mismatch')
    return provenance, attestation
