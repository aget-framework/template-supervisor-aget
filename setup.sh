#!/bin/bash

# my-AGET-template Setup Wizard
# Customizes the template for your governance layer

set -e

echo "════════════════════════════════════════════════════════"
echo "   Welcome to my-AGET-template Setup Wizard"
echo "   Creating your personalized AGET governance layer"
echo "════════════════════════════════════════════════════════"
echo

# Function to replace placeholders
replace_placeholder() {
    local placeholder=$1
    local value=$2
    local file=$3

    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s|{{${placeholder}}}|${value}|g" "$file" 2>/dev/null || true
    else
        # Linux
        sed -i "s|{{${placeholder}}}|${value}|g" "$file" 2>/dev/null || true
    fi
}

# Collect user information
echo "Let's customize your AGET governance layer..."
echo

read -p "Your name: " USER_NAME
read -p "Project name (e.g., 'my-AGET' or 'alex-AGET'): " PROJECT_NAME
read -p "Brief project description: " PROJECT_DESC
read -p "Project tagline (5-10 words): " PROJECT_TAGLINE
read -p "Repository visibility (Private/Public): " VISIBILITY
read -p "Your main purpose for this governance layer: " PURPOSE

echo
echo "Setting up your customized template..."

# Copy templates if they don't exist as main files
if [ -f "templates/AGENTS.md.template" ] && [ ! -f "AGENTS.md" ]; then
    cp templates/AGENTS.md.template AGENTS.md
fi

if [ -f "templates/README.md.template" ]; then
    cp templates/README.md.template README.md
fi

# Replace placeholders in AGENTS.md
replace_placeholder "YOUR_PROJECT_NAME" "$PROJECT_NAME" "AGENTS.md"
replace_placeholder "YOUR_PROJECT_DESCRIPTION" "$PROJECT_DESC" "AGENTS.md"
replace_placeholder "ADD_YOUR_CUSTOM_RULES_HERE" "# Add your custom rules as you discover them" "AGENTS.md"
replace_placeholder "DATE" "$(date +%Y-%m-%d)" "AGENTS.md"

# Replace placeholders in README.md
replace_placeholder "YOUR_PROJECT_NAME" "$PROJECT_NAME" "README.md"
replace_placeholder "YOUR_TAGLINE" "$PROJECT_TAGLINE" "README.md"
replace_placeholder "VISIBILITY" "$VISIBILITY" "README.md"
replace_placeholder "YOUR_PURPOSE" "$PURPOSE" "README.md"
replace_placeholder "YOUR_DESCRIPTION" "$PROJECT_DESC" "README.md"
replace_placeholder "YOUR_MISSION_STATEMENT" "To manage and govern my AGET agent ecosystem effectively" "README.md"
replace_placeholder "YOUR_CURRENT_PRIORITY_1" "Pattern extraction and validation" "README.md"
replace_placeholder "YOUR_CURRENT_PRIORITY_2" "Evolution tracking and documentation" "README.md"
replace_placeholder "YOUR_CURRENT_PRIORITY_3" "Governance framework development" "README.md"
replace_placeholder "YOUR_PHILOSOPHY_POINTS" "1. **Learn by doing**\n2. **Document everything**\n3. **Share what works**" "README.md"
replace_placeholder "CREATION_DATE" "$(date +%Y-%m-%d)" "README.md"
replace_placeholder "PROJECT_NATURE" "AGET Governance Layer" "README.md"
replace_placeholder "YOUR_NAME" "$USER_NAME" "README.md"
replace_placeholder "YOUR_CLOSING_STATEMENT" "Where patterns evolve through practice" "README.md"

# Create CLAUDE.md as symlink if it doesn't exist
if [ ! -e "CLAUDE.md" ]; then
    ln -s AGENTS.md CLAUDE.md
    echo "✓ Created CLAUDE.md symlink"
fi

# Create initial evolution entry
mkdir -p .aget/evolution
cat > .aget/evolution/INIT-$(date +%Y-%m-%d)-setup.md << EOF
# Initial Setup
*Date: $(date +%Y-%m-%d)*
*Type: Initialization*
*Owner: $USER_NAME*

## Configuration
- Project: $PROJECT_NAME
- Purpose: $PURPOSE
- Template Version: 0.1.0

## Starting Point
Initialized from my-AGET-template to create personalized governance layer.

## Next Steps
1. Review generated configuration
2. Start documenting patterns
3. Track evolution decisions
EOF

echo
echo "════════════════════════════════════════════════════════"
echo "✅ Setup Complete!"
echo "════════════════════════════════════════════════════════"
echo
echo "Your governance layer is ready. Next steps:"
echo "1. Review AGENTS.md and README.md"
echo "2. Start documenting your patterns in patterns/"
echo "3. Track decisions in .aget/evolution/"
echo "4. Run ./validate.sh to verify setup"
echo
echo "To start using: echo 'wake up'"
echo