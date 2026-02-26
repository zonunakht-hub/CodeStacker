# 🔒 SECURITY RULES

## Credentials Handling
- NEVER write actual credentials in any file
- NEVER commit .env files to version control
- ALWAYS reference where credentials are stored, never the values
- Use environment variables for all secrets

## Code Security
- No hardcoded passwords, API keys, or tokens
- Use parameterized queries for all database interactions
- Validate all user input
- Follow OWASP guidelines for the framework being used

## Access Control
- Follow principle of least privilege
- Never expose internal APIs or ports
- Authentication required for all sensitive endpoints

## Dependency Security
- Keep dependencies updated
- Audit for known vulnerabilities
- Use lock files (package-lock.json, requirements.txt, etc.)

## Reporting
- Document any security concerns in reports/
- Flag potential security issues immediately
- Never proceed with code that has security implications without user approval
