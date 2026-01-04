#!/bin/bash
# Development environment setup script
# Configures development environment with standard tools and settings

set -e

echo "🚀 Setting up development environment..."

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cat > .env << 'EOF'
# Development Environment Variables
NODE_ENV=development
DEBUG=true
LOG_LEVEL=debug
EOF
    echo "  ✅ .env created"
fi

# Install Git hooks if directory exists
if [ -d .git ]; then
    echo "🔗 Setting up Git hooks..."
    mkdir -p .git/hooks

    # Pre-commit hook
    cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Run linting before commit
echo "Running pre-commit checks..."
npm run lint 2>/dev/null || python -m flake8 . 2>/dev/null || true
EOF
    chmod +x .git/hooks/pre-commit
    echo "  ✅ Git hooks configured"
fi

# Check for package files and install dependencies
if [ -f package.json ]; then
    echo "📦 Installing npm dependencies..."
    npm install
fi

if [ -f requirements.txt ]; then
    echo "🐍 Installing Python dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "✅ Development environment setup complete!"
