---
name: api-wrapper
description: This skill should be used when working with REST APIs, including making requests, handling authentication, parsing responses, error handling, and rate limiting. It provides structured workflows for API integration and testing.
---

# API Wrapper

Simplifies REST API interactions with built-in authentication, error handling, rate limiting, and response parsing.

## Purpose

Provides reusable patterns and utilities for working with REST APIs. Handles common concerns like authentication, retries, rate limiting, and response validation, allowing focus on business logic rather than HTTP mechanics.

## When to Use

Use this skill when:
- Integrating with REST APIs
- Building API clients or wrappers
- Testing API endpoints
- Handling API authentication (OAuth, API keys, JWT)
- Implementing rate limiting and retries
- Parsing and validating API responses
- Debugging API interactions

## Usage Guide

### Making API Requests

To make authenticated API requests:

1. Configure authentication method (API key, OAuth, JWT)
2. Set up request headers and parameters
3. Handle response and errors

Use `scripts/api_client.py` as a base for API interactions.

Example: "Fetch all users from the GitHub API"

### Authentication

To handle API authentication:

1. Determine authentication method
2. Store credentials securely
3. Include auth in requests
4. Refresh tokens when needed

Reference `references/auth-methods.md` for different authentication patterns.

### Rate Limiting

To implement rate limiting:

1. Check API rate limits
2. Track request counts
3. Implement backoff strategy
4. Queue requests if needed

Use `scripts/rate_limiter.py` for rate limit management.

### Error Handling

To handle API errors:

1. Catch HTTP errors
2. Parse error responses
3. Implement retry logic
4. Log failures appropriately

Reference `references/error-codes.md` for common HTTP status codes and handling.

### Response Parsing

To parse API responses:

1. Validate response structure
2. Extract needed data
3. Transform to desired format
4. Handle pagination

Use `scripts/response_parser.py` for consistent response handling.

### Testing APIs

To test API endpoints:

1. Create test fixtures
2. Mock API responses
3. Test error scenarios
4. Validate response schemas

Reference `references/testing-apis.md` for API testing best practices.

## Bundled Resources

### Scripts

- `scripts/api_client.py` - Base API client with auth and error handling
- `scripts/rate_limiter.py` - Rate limiting implementation
- `scripts/response_parser.py` - Response parsing and validation
- `scripts/oauth_helper.py` - OAuth 2.0 flow implementation

### References

- `references/auth-methods.md` - API authentication patterns and examples
- `references/error-codes.md` - HTTP status codes and error handling
- `references/testing-apis.md` - API testing strategies
- `references/rate-limits.md` - Common API rate limits and strategies

### Assets

- `assets/postman/` - Postman collection templates
- `assets/schemas/` - JSON schema files for response validation

## Best Practices

1. **Security** - Never hardcode credentials, use environment variables
2. **Error Handling** - Always handle network errors and timeouts
3. **Rate Limits** - Respect API rate limits to avoid blocking
4. **Logging** - Log requests and responses for debugging
5. **Caching** - Cache responses when appropriate to reduce API calls
6. **Retries** - Implement exponential backoff for transient failures
