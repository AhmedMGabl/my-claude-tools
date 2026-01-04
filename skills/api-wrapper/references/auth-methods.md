# API Authentication Methods

## API Key Authentication

Simple authentication using an API key in headers.

```python
headers = {
    'Authorization': f'Bearer {api_key}',
    # or
    'X-API-Key': api_key
}
```

**Best for**: Simple APIs, server-to-server communication

## OAuth 2.0

Token-based authentication with refresh capability.

```python
# Initial authentication
POST /oauth/token
{
    "grant_type": "client_credentials",
    "client_id": "your_client_id",
    "client_secret": "your_client_secret"
}

# Use access token
headers = {'Authorization': f'Bearer {access_token}'}

# Refresh when expired
POST /oauth/token
{
    "grant_type": "refresh_token",
    "refresh_token": "your_refresh_token"
}
```

**Best for**: User-facing applications, mobile apps

## JWT (JSON Web Tokens)

Self-contained tokens with encoded claims.

```python
import jwt

# Create JWT
token = jwt.encode(
    {'user_id': 123, 'exp': datetime.utcnow() + timedelta(hours=1)},
    secret_key,
    algorithm='HS256'
)

# Verify JWT
payload = jwt.decode(token, secret_key, algorithms=['HS256'])
```

**Best for**: Stateless authentication, microservices

## Basic Authentication

Username and password encoded in headers.

```python
import base64

credentials = f"{username}:{password}".encode()
encoded = base64.b64encode(credentials).decode()

headers = {'Authorization': f'Basic {encoded}'}
```

**Best for**: Development, internal tools (⚠️ Use HTTPS)

## Security Best Practices

1. **Never commit credentials** - Use environment variables
2. **Use HTTPS** - Always encrypt API communication
3. **Rotate keys** - Regularly update API keys and tokens
4. **Limit scope** - Use minimum required permissions
5. **Monitor usage** - Track API key usage for security
