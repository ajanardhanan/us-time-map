# Comprehensive Breakdown of All 9 APEX-Configured Claude Skills

This document provides detailed coverage of each skill's capabilities, areas covered, and use cases.

---

## Overview of APEX Skills

APEX has configured **9 specialized skills** to enhance Claude Code productivity:

| # | Skill | Primary Focus | Speed | Automation | Team Value |
|---|-------|---------------|-------|------------|------------|
| 1 | **update-config** | Workflow setup | One-time | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 2 | **keybindings-help** | Productivity | One-time | ⭐⭐ | ⭐⭐⭐ |
| 3 | **simplify** | Code quality | Fast | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 4 | **fewer-permission-prompts** | Speed | Fast | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 5 | **loop** | Monitoring | Continuous | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 6 | **claude-api** | AI apps | Project | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 7 | **init** | Documentation | Fast | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 8 | **review** | Code quality | Fast | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 9 | **security-review** | Security | Fast | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 1️⃣ update-config

**Purpose**: Configure Claude Code settings, hooks, permissions, and automation

**Invocation**: `/update-config` or ask "Configure Claude settings for..."

### **Areas Covered**:

#### **A. Automated Behaviors (Hooks)** 🔄
Configure when-X-then-Y automation:
- `pre-commit` hooks - Run before commits
- `post-commit` hooks - Run after commits
- `pre-deploy` hooks - Run before deployments
- `post-deploy` hooks - Run after deployments
- `on-error` hooks - Run when errors occur
- `user-prompt-submit` hooks - Run on user input

**Examples**:
```json
{
  "hooks": {
    "pre-commit": "npm test && npm run lint",
    "post-deploy": "slack-notify 'Deployment complete'",
    "on-error": "logger 'Error in Claude Code'"
  }
}
```

#### **B. Permission Management** 🔐
Control what runs automatically:
- Global permissions (all projects)
- User permissions (your account)
- Project permissions (specific repos)
- Allow/deny lists
- Auto-approve rules

**Examples**:
```json
{
  "permissions": {
    "auto_approve": ["npm install", "git status", "aws s3 ls"],
    "always_deny": ["rm -rf /", "sudo"],
    "prompt": ["git push", "aws s3 delete"]
  }
}
```

#### **C. Environment Variables** 🌍
Set project-wide variables:
- API keys (reference to secure storage)
- Configuration values
- Feature flags
- Runtime settings

**Examples**:
```json
{
  "environment": {
    "NODE_ENV": "development",
    "DEBUG": "true",
    "AWS_REGION": "us-east-1"
  }
}
```

#### **D. Hook Troubleshooting** 🔧
Fix hook issues:
- Debug failed hooks
- View hook execution logs
- Disable problematic hooks
- Test hook configurations

#### **E. Settings File Management** 📄
Manages these files:
- `~/.claude/settings.json` (global)
- `~/.claude/settings.local.json` (local overrides)
- `.claude/settings.json` (project-specific)

### **Complete Configuration Example**:

```json
{
  "permissions": {
    "auto_approve": ["npm install", "git status"],
    "always_deny": ["rm -rf /", "sudo"],
    "prompt": ["git push", "aws s3 delete"]
  },
  "hooks": {
    "pre-commit": "npm test && npm run lint",
    "post-deploy": "echo 'Deployment complete'",
    "on-error": "logger 'Error occurred in Claude Code'"
  },
  "environment": {
    "NODE_ENV": "development",
    "DEBUG": "true"
  },
  "notifications": {
    "slack_webhook": "https://hooks.slack.com/...",
    "email": "team@apex.com"
  }
}
```

### **Use Cases**:
- ✅ "Run linter before every commit"
- ✅ "Auto-approve read-only git commands"
- ✅ "Notify team on deployment"
- ✅ "Set environment variables for project"
- ✅ "Automate testing workflow"

---

## 2️⃣ keybindings-help

**Purpose**: Customize keyboard shortcuts and key bindings

**Invocation**: `/keybindings-help` or ask "Help me customize keyboard shortcuts"

### **Areas Covered**:

#### **A. Key Rebinding** ⌨️
Remap existing shortcuts:
- Submit message (default: Enter)
- Cancel operation (default: Ctrl+C)
- Clear screen
- Navigate history
- Copy/paste
- Undo/redo

**Examples**:
- Change submit from Enter to Ctrl+Enter
- Rebind cancel from Ctrl+C to Escape
- Custom copy/paste shortcuts

#### **B. Chord Bindings** 🎹
Multi-key shortcuts (like VS Code):
- Ctrl+K then S (save)
- Ctrl+K then D (deploy)
- Ctrl+K then T (test)

**Examples**:
```json
{
  "key": "ctrl+k ctrl+s",
  "command": "saveAndCommit"
}
```

#### **C. Function Key Mapping** 🔢
F-key shortcuts:
- F1-F12 mappings
- Custom commands
- Quick actions

**Examples**:
- F5 → Refresh/reload
- F9 → Build
- F10 → Deploy

#### **D. Modifier Keys** 🔧
Configure modifiers:
- Ctrl combinations
- Alt combinations
- Shift combinations
- Cmd (Mac) combinations

#### **E. Keybindings File** 📝
Manages: `~/.claude/keybindings.json`

### **Configuration Example**:

```json
{
  "bindings": [
    {
      "key": "ctrl+enter",
      "command": "submit",
      "when": "inputFocus"
    },
    {
      "key": "ctrl+k ctrl+s",
      "command": "saveAndCommit"
    },
    {
      "key": "ctrl+k ctrl+d",
      "command": "deploy"
    },
    {
      "key": "f5",
      "command": "refresh"
    }
  ]
}
```

### **Use Cases**:
- ✅ "Make submit Ctrl+Enter instead of Enter"
- ✅ "Add chord shortcut Ctrl+K, D for deploy"
- ✅ "Rebind navigation to arrow keys"
- ✅ "Custom F-key shortcuts for common tasks"
- ✅ "Match VS Code keybindings"

---

## 3️⃣ simplify

**Purpose**: Review code for reuse, quality, and efficiency, then automatically fix issues

**Invocation**: `/simplify` or ask "Simplify this code"

### **Areas Covered**:

#### **A. Code Reuse Detection** ♻️
Identifies:
- Duplicate code blocks
- Similar functions
- Repeated patterns
- Copy-paste code
- Extractable utilities

**Fixes Applied**:
- Extract common functions
- Create reusable components
- Apply DRY (Don't Repeat Yourself) principles
- Create shared utility modules

#### **B. Code Quality Issues** ✨
Detects:
- Overly complex functions (cyclomatic complexity)
- Long parameter lists (>4 parameters)
- Deep nesting (>3 levels)
- Magic numbers
- Unclear variable names
- Poor code organization

**Improvements**:
- Simplify logic
- Break down complex functions
- Use constants for magic numbers
- Rename variables for clarity
- Restructure code

#### **C. Performance Inefficiencies** ⚡
Finds:
- Unnecessary loops
- Redundant calculations
- Inefficient algorithms (O(n²) → O(n))
- Memory leaks
- Unused imports/variables
- Excessive re-renders (React)

**Optimizations**:
- Replace inefficient algorithms
- Cache expensive calculations
- Remove unused code
- Optimize data structures
- Add memoization

#### **D. Modern Best Practices** 🎯
Updates to:
- Latest ES6+ syntax
- Async/await over promises
- Destructuring
- Template literals
- Arrow functions
- Modern framework patterns

#### **E. Code Smell Detection** 👃
Identifies:
- Long methods (>50 lines)
- Large classes (>300 lines)
- God objects
- Feature envy
- Data clumps
- Primitive obsession

#### **F. Framework-Specific Optimization** ⚛️

**React Example**:
```javascript
// Before
class MyComponent extends React.Component {
  render() {
    return <div>{this.props.name}</div>;
  }
}

// After (simplified by skill)
const MyComponent = ({ name }) => <div>{name}</div>;
```

**Python Example**:
```python
# Before
result = []
for item in items:
    if item.active:
        result.append(item.name)

# After (simplified by skill)
result = [item.name for item in items if item.active]
```

### **Supported Languages**:
- ✅ JavaScript/TypeScript
- ✅ Python
- ✅ Java
- ✅ Go
- ✅ Rust
- ✅ C/C++
- ✅ Ruby
- ✅ PHP
- ✅ Swift/Kotlin

### **Output Example**:

```
Simplification Report
====================

🔴 CRITICAL ISSUES (3 fixed)
✓ Function calculateTotal() had O(n²) complexity → Optimized to O(n)
✓ Duplicate code found in 4 places → Extracted to utils.js
✓ Memory leak in useEffect → Added cleanup function

🟡 IMPROVEMENTS (7 applied)
✓ Variable 'x' renamed to 'userCount' for clarity
✓ Magic number 86400000 → constant MS_PER_DAY
✓ Deep nesting (4 levels) → Flattened with early returns
✓ Long function split into 3 smaller functions
✓ Converted 5 functions to arrow functions
✓ Added TypeScript types for better safety
✓ Replaced .then() with async/await

✅ ADDITIONAL FIXES (10 applied)
✓ Removed 3 unused imports
✓ Fixed 2 ESLint warnings
✓ Added memoization to expensive calculation
✓ Optimized React component re-renders
✓ Simplified conditional logic
✓ Extracted magic strings to constants

📊 Metrics
- Lines of code: 347 → 289 (17% reduction)
- Complexity score: 8.4 → 5.2 (38% improvement)
- Maintainability index: 62 → 78 (26% improvement)
```

### **Use Cases**:
- ✅ After implementing new features
- ✅ Before code review
- ✅ Refactoring sessions
- ✅ Performance optimization
- ✅ Code cleanup sprints
- ✅ Learning better patterns

---

## 4️⃣ fewer-permission-prompts

**Purpose**: Reduce interruptions by auto-approving safe, repetitive commands

**Invocation**: `/fewer-permission-prompts` or ask "Reduce permission prompts"

### **Areas Covered**:

#### **A. Command Analysis** 🔍
Scans your history for:
- Read-only operations
- Safe git commands
- Package manager reads
- Status checks
- List operations
- Non-destructive queries

**Examples of Safe Commands**:
```bash
git status
git log
git diff
npm list
aws s3 ls
kubectl get pods
docker ps
cat file.txt
ls -la
```

#### **B. Bash Tool Patterns** 🐚
Auto-approves:
- File reads: `cat`, `less`, `head`, `tail`
- Directory listings: `ls`, `find`, `tree`
- Status checks: `git status`, `systemctl status`
- Info queries: `which`, `whereis`, `man`
- Network reads: `curl GET`, `wget`

#### **C. MCP Tool Allowlists** 🔌
Auto-approves safe MCP operations:
- Read Jira issues
- View Confluence pages
- List resources
- Get status
- Search operations

#### **D. Project-Specific Rules** 📁
Creates `.claude/settings.json` with:
```json
{
  "permissions": {
    "auto_approve": [
      "npm install",
      "npm list",
      "git status",
      "git log --oneline -10",
      "aws cloudformation describe-stacks",
      "kubectl get pods"
    ]
  }
}
```

#### **E. Risk Assessment** ⚖️
Categorizes commands:

**✅ Safe (auto-approve)**:
- git status, git log, git diff
- npm list, npm outdated
- aws s3 ls, aws cloudformation describe-stacks
- kubectl get (read-only)

**⚠️ Moderate (still prompts)**:
- git push
- npm install
- aws s3 sync
- kubectl apply

**🔴 Dangerous (never auto-approve)**:
- rm -rf
- git reset --hard
- aws s3 delete
- sudo commands
- DROP TABLE

### **Analysis Process**:

```
1. Scans your Bash tool usage history
2. Identifies patterns of safe commands
3. Groups by type (git, npm, aws, docker, etc.)
4. Creates prioritized allowlist
5. Writes to .claude/settings.json
6. Applies immediately to your workflow
```

### **Output Example**:

```
Permission Prompt Analysis
=========================

📊 Scanned 127 Bash commands from your history

✅ SAFE COMMANDS (Auto-approve recommended: 45)

Git Operations (15 commands):
- git status (used 12 times)
- git log --oneline -10 (used 8 times)
- git diff (used 6 times)

NPM Operations (12 commands):
- npm list (used 7 times)
- npm outdated (used 5 times)

AWS Operations (18 commands):
- aws s3 ls (used 10 times)
- aws cloudformation describe-stacks (used 8 times)

Docker Operations (8 commands):
- docker ps (used 6 times)
- docker images (used 3 times)

⚙️ CONFIGURATION CREATED
Written to: .claude/settings.json

📈 Impact Estimate:
- Commands auto-approved: 45
- Prompts eliminated per session: 15-20
- Time saved per session: 2-3 minutes
- Workflow interruptions reduced: 60%
```

### **Use Cases**:
- ✅ Start of new project (reduce friction)
- ✅ After repetitive command sessions
- ✅ Team workflow standardization
- ✅ CI/CD pipeline development
- ✅ Improve development flow

---

## 5️⃣ loop

**Purpose**: Run commands or skills on recurring intervals

**Invocation**: `/loop <interval> <command>` or ask "Run this every 5 minutes"

### **Areas Covered**:

#### **A. Status Monitoring** 📊
Poll for:
- Deployment status
- Build progress
- CI/CD pipeline status
- Server health
- Application metrics

**Examples**:
```bash
/loop 5m "check deployment status"
/loop 2m "aws cloudformation describe-stacks --stack-name my-app"
/loop 10s "curl https://api.example.com/health"
```

#### **B. Task Automation** 🤖
Recurring tasks:
- Run tests periodically
- Sync data
- Backup operations
- Log collection
- Status reports

**Examples**:
```bash
/loop 1h "npm test"
/loop 30m "git pull && npm install"
/loop 15m /security-review
```

#### **C. Alert Generation** 🚨
Check and notify:
- Error conditions
- Threshold breaches
- Status changes
- Completion events

**Examples**:
```bash
/loop 5m "check if deployment complete, then notify"
/loop 1m "if error count > 10, alert team"
```

#### **D. Development Workflows** 💻
Automate:
- Watch for file changes
- Re-run builds
- Restart dev servers
- Sync environments

**Examples**:
```bash
/loop 30s "check for code changes, run linter"
/loop 1m "sync local with remote branch"
```

#### **E. Interval Specifications** ⏱️
Supports:
- Seconds: `10s`, `30s`, `45s`
- Minutes: `1m`, `5m`, `15m`, `30m`
- Hours: `1h`, `2h`, `6h`, `12h`
- Default: `10m` if not specified

### **Command Syntax**:

```bash
# Basic format
/loop <interval> <command>

# With shell command
/loop 5m "aws cloudformation describe-stacks"

# With skill
/loop 15m /security-review
/loop 10m /simplify

# With complex command
/loop 2m "git status && npm test"
```

### **Lifecycle Management**:

```bash
# Start a loop
/loop 5m "check deployment"

# Stop a loop (Ctrl+C or TaskStop)
TaskStop <task-id>

# List running loops
TaskList

# Get loop output
TaskOutput <task-id>
```

### **Use Cases**:
- ✅ "Check deployment every 5 minutes"
- ✅ "Keep running security scans"
- ✅ "Monitor for PR reviews needed"
- ✅ "Periodic health checks"
- ✅ "Auto-sync development environment"
- ✅ "Watch for build completion"

---

## 6️⃣ claude-api

**Purpose**: Build, debug, and optimize applications using Claude API/Anthropic SDK

**Invocation**: `/claude-api` or ask "Help me build a Claude API app"

**Triggers Automatically When**:
- Code imports `anthropic` or `@anthropic-ai/sdk`
- User mentions Claude API, Anthropic SDK, or Managed Agents
- Modifying Claude API code (caching, thinking, tool use, etc.)
- Questions about API features

### **Areas Covered**:

#### **A. API Integration Development** 🔌
Builds applications using:
- Anthropic SDK (Python, TypeScript, Java, Go)
- Claude API endpoints
- Message API
- Streaming responses
- Batch API

**Generates Code For**:
```python
from anthropic import Anthropic

client = Anthropic(api_key="...")
message = client.messages.create(
    model="claude-sonnet-4.5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
```

#### **B. Prompt Caching** 💾
Implements:
- Cache control headers
- Cache breakpoints
- Cache hit optimization
- Cost reduction strategies

**Example**:
```python
message = client.messages.create(
    model="claude-sonnet-4.5",
    system=[{
        "type": "text",
        "text": "Large system prompt...",
        "cache_control": {"type": "ephemeral"}
    }],
    messages=[...]
)
```

#### **C. Tool Use (Function Calling)** 🛠️
Implements:
- Tool definitions
- Tool execution
- Multi-tool workflows
- Error handling

**Example**:
```python
tools = [{
    "name": "get_weather",
    "description": "Get weather for a location",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        },
        "required": ["location"]
    }
}]

message = client.messages.create(
    model="claude-sonnet-4.5",
    tools=tools,
    messages=[...]
)
```

#### **D. Extended Thinking** 🧠
Implements:
- Extended thinking mode
- Budget allocation
- Reasoning visibility
- Thought process access

#### **E. Model Migration** 🔄
Handles upgrades:
- Claude 4.5 → 4.6
- Claude 4.6 → 4.7
- Deprecated model replacements
- Breaking change management
- API version updates

#### **F. Optimization Techniques** ⚡
Improves:
- Token efficiency
- Response speed
- Cost optimization
- Cache hit rates
- Prompt engineering
- Batch processing

#### **G. Features Supported** ✨
Implements:
- **Streaming**: Real-time response streaming
- **Batching**: Process multiple requests efficiently
- **File uploads**: PDFs, images, documents
- **Citations**: Source attribution
- **Memory**: Context management across conversations
- **Vision**: Image analysis
- **Document understanding**: PDF/text analysis

### **What It Builds**:

**Chatbots**:
- Customer service bots
- Internal Q&A systems
- Documentation assistants
- Support automation

**Automation**:
- Code review bots
- Content generation pipelines
- Data analysis workflows
- Report generation

**Integrations**:
- Slack bots with Claude
- GitHub PR reviewers
- Email assistants
- CRM automation

### **Code Generation Example**:

**Request**: "Build a chatbot with streaming responses and tool use"

**Generated Output**:
```typescript
import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

// Define tools
const tools = [
  {
    name: 'get_user_info',
    description: 'Get user information from database',
    input_schema: {
      type: 'object',
      properties: {
        user_id: { type: 'string', description: 'User ID' }
      },
      required: ['user_id']
    }
  }
];

async function chatWithStreaming(message: string) {
  const stream = await anthropic.messages.stream({
    model: 'claude-sonnet-4.5',
    max_tokens: 1024,
    tools: tools,
    messages: [{
      role: 'user',
      content: message
    }]
  });

  // Handle streaming text
  stream.on('text', (text) => {
    process.stdout.write(text);
  });

  // Handle tool use
  stream.on('tool_use', async (tool) => {
    if (tool.name === 'get_user_info') {
      const result = await getUserFromDB(tool.input.user_id);
      // Send tool result back
    }
  });

  const finalMessage = await stream.finalMessage();
  return finalMessage;
}
```

### **Use Cases**:
- ✅ Building AI-powered applications
- ✅ Creating chatbots and assistants
- ✅ Automating workflows with AI
- ✅ Migrating between Claude versions
- ✅ Optimizing API usage and costs
- ✅ Implementing advanced features (caching, tools, streaming)

---

## 7️⃣ init

**Purpose**: Initialize CLAUDE.md documentation file for codebase

**Invocation**: `/init` or ask "Initialize project documentation"

### **Areas Covered**:

#### **A. Codebase Documentation** 📚
Documents:
- Project overview and purpose
- Architecture and design
- Key components and modules
- File structure and organization
- Dependencies and libraries
- Configuration files

**Creates**: `CLAUDE.md` or `.claude/CLAUDE.md`

#### **B. Development Guidelines** 📋
Includes:
- Coding standards and conventions
- Style guide
- Best practices
- Testing requirements
- Review process
- Git workflow

#### **C. Getting Started** 🚀
Documents:
- Setup instructions
- Prerequisites
- Installation steps
- First-time configuration
- Common commands
- Troubleshooting

#### **D. Architecture Documentation** 🏗️
Explains:
- System design patterns
- Component relationships
- Data flow and state management
- API structure
- Database schema
- External integrations

#### **E. Claude-Specific Context** 🤖
Helps Claude understand:
- Project conventions
- Custom terminology
- Business logic
- Important constraints
- Historical decisions
- Known issues

### **Generated CLAUDE.md Example**:

```markdown
# US Time Map

## Overview
Serverless application displaying real-time clocks for all 50 US states
on an interactive map using React, AWS Lambda, and CloudFront.

## Architecture

### Frontend
- **Framework**: React 19.2.8
- **Map Library**: react-simple-maps
- **Time Handling**: moment-timezone
- **Styling**: CSS-in-JS with gradient backgrounds

### Backend
- **Runtime**: AWS Lambda (Python 3.11)
- **API**: API Gateway REST API
- **Dependencies**: pytz for timezone calculations

### Infrastructure
- **IaC**: AWS SAM (CloudFormation)
- **Hosting**: S3 static website
- **CDN**: CloudFront distribution
- **Deployment**: Automated via deploy.sh

## Project Structure

```
us-time-map/
├── frontend/           # React application
│   ├── src/
│   │   ├── App.js     # Main app component
│   │   ├── USMap.js   # Map component with time display
│   │   └── stateData.js # State timezone mappings
│   └── package.json
├── backend/            # Lambda function
│   ├── lambda_function.py
│   └── requirements.txt
├── template.yaml       # SAM infrastructure
└── deploy.sh          # Deployment automation
```

## Development

### Prerequisites
- Node.js 14+
- Python 3.11
- AWS CLI configured
- SAM CLI installed

### Local Development
```bash
# Install dependencies
cd frontend && npm install

# Start dev server
npm start

# Runs on http://localhost:3000
```

### Testing Lambda Locally
```bash
sam local invoke TimeFunction -e backend/test_event.json
```

## Coding Standards

### JavaScript/React
- Use functional components with hooks
- Props destructuring in component signature
- No inline styles except for dynamic values
- ESLint configuration in .eslintrc

### Python
- PEP 8 style guide
- Type hints for function signatures
- Comprehensive error handling
- CORS headers on all responses

## Deployment

### Automated
```bash
./deploy.sh
```

### Manual
```bash
sam build
sam deploy --guided
cd frontend && npm run build
aws s3 sync build/ s3://bucket-name
```

## Important Context

### Timezone Handling
- All 50 states mapped to IANA timezones
- Client-side calculation (no backend needed for times)
- Updates every second via setInterval

### AWS Resources
- Stack name: us-time-map
- Region: us-east-1
- S3 bucket naming: us-time-map-{account-id}

### Security
- S3 bucket is publicly readable (required for website)
- API has CORS enabled for browser access
- No sensitive data stored or transmitted

## Known Issues
- react-simple-maps requires --legacy-peer-deps with React 19
- CloudFront distribution takes 15-20 minutes to deploy

## Dependencies

### Frontend
- react: ^19.2.8
- react-simple-maps: ^3.0.0
- moment-timezone: ^0.5.43
- d3-geo: ^3.1.0

### Backend
- pytz: 2024.1

## Contributing
1. Create feature branch
2. Make changes
3. Run tests
4. Submit PR
5. Requires 1 approval

## Contact
- Author: Anil Janardhanan
- Email: anilkjanardhan@gmail.com
- Repository: https://github.com/ajanardhanan/us-time-map
```

### **What It Analyzes**:

```
Scans:
✅ package.json / requirements.txt
✅ README.md (if exists)
✅ Directory structure
✅ Configuration files (.eslintrc, tsconfig.json, etc.)
✅ Code patterns and conventions
✅ Git history and commits
✅ Dependencies and versions
✅ Import/export patterns

Generates:
✅ Comprehensive CLAUDE.md
✅ Project overview
✅ Setup instructions
✅ Architecture details
✅ Coding standards
✅ Development workflow
✅ Deployment process
```

### **Use Cases**:
- ✅ Start of new project (establish conventions)
- ✅ Onboarding Claude to existing codebase
- ✅ Team documentation
- ✅ Maintain context across sessions
- ✅ Share project standards
- ✅ New team member onboarding

---

## 8️⃣ review

**Purpose**: Review pull requests for code quality and best practices

**Invocation**: `/review` or ask "Review this PR"

### **Areas Covered**:

#### **A. Code Quality Assessment** ✨
Reviews:
- Code clarity and readability
- Naming conventions (variables, functions, classes)
- Function complexity (cyclomatic complexity)
- Code organization and structure
- Maintainability index

#### **B. Best Practices Validation** ✅
Checks for:
- Design patterns (SOLID, DRY, KISS)
- Framework conventions (React, Angular, etc.)
- Language idioms and best practices
- Error handling patterns
- Async/Promise handling

#### **C. Bug Detection** 🐛
Identifies:
- Logic errors
- Edge case handling
- Null/undefined issues
- Race conditions
- Off-by-one errors
- Type mismatches

#### **D. Performance Issues** ⚡
Spots:
- Inefficient algorithms (O(n²) when O(n) possible)
- Memory leaks (unclosed connections, event listeners)
- Unnecessary re-renders (React)
- Database N+1 queries
- Blocking operations on main thread

#### **E. Testing Coverage** 🧪
Reviews:
- Test completeness
- Edge case coverage
- Mock usage appropriateness
- Test quality and clarity
- Missing test scenarios

#### **F. Documentation** 📝
Checks:
- Function/method documentation
- Complex logic comments
- API documentation updates
- README updates
- Changelog entries
- Migration guides

#### **G. Breaking Changes** ⚠️
Identifies:
- API signature changes
- Deprecated features
- Migration requirements
- Backwards compatibility issues
- Version bump recommendations

#### **H. Dependencies** 📦
Reviews:
- New dependencies (necessity check)
- Version updates (breaking changes)
- Security vulnerabilities (npm audit)
- License compatibility
- Bundle size impact

### **Review Process**:

```
1. Analyzes git diff (current branch vs base)
2. Examines all changed files
3. Checks context around changes
4. Compares against best practices
5. Generates inline review comments
6. Suggests specific improvements
7. Highlights concerns
8. Provides overall recommendation
```

### **Output Example**:

```
Pull Request Review
==================

📊 Summary
- Files changed: 8
- Lines added: 247
- Lines removed: 89
- Complexity: Medium
- Test coverage: 87% (+5%)

✅ APPROVED (12 items)
✓ Good error handling in api.ts
✓ Tests cover edge cases thoroughly
✓ Clear variable naming throughout
✓ Follows project conventions
✓ Documentation is comprehensive
✓ No security issues detected

💬 SUGGESTIONS (5 items)

📄 src/api/users.ts:42
⚠️ Potential N+1 query issue
The loop at line 42 makes a database query for each user.
Consider using .include() to fetch related data in one query.

Suggestion:
- const users = await User.findAll();
- for (const user of users) {
-   user.posts = await Post.findAll({ where: { userId: user.id } });
- }
+ const users = await User.findAll({
+   include: [{ model: Post }]
+ });

📄 src/components/UserList.tsx:15
💡 Optimization opportunity
Component re-renders on every parent update.
Wrap expensive calculation in useMemo.

Suggestion:
+ const sortedUsers = useMemo(() => {
    return users.sort((a, b) => a.name.localeCompare(b.name));
+ }, [users]);

📄 src/utils/validators.ts:88
📝 Documentation needed
Complex validation logic without explanation.
Add JSDoc comment explaining validation rules.

Suggestion:
+ /**
+  * Validates user email format and domain
+  * @param email - Email to validate
+  * @returns true if valid, false otherwise
+  */
  export function validateEmail(email: string): boolean {

🔴 BLOCKERS (2 items - Must fix before merge)

📄 src/api/auth.ts:67
❌ SECURITY ISSUE - Hardcoded API key
API key should not be committed to code.

Current:
const apiKey = "sk-1234567890abcdef"; // ❌ Security risk

Fix:
const apiKey = process.env.API_KEY; // ✅ Use environment variable

Also: Rotate the exposed API key immediately

📄 tests/auth.test.ts:120
❌ MISSING TEST CASE - Expired token
Authentication tests don't cover expired token scenario.

Add:
test('should reject expired token', async () => {
  const expiredToken = generateToken({ exp: Date.now() - 3600 });
  const response = await request(app)
    .get('/api/protected')
    .set('Authorization', `Bearer ${expiredToken}`);
  expect(response.status).toBe(401);
});

📈 Metrics
- Complexity score: 6.2 (acceptable, <10 is good)
- Maintainability: 78/100 (+6 from previous)
- Test coverage: 87% (+5%)
- Security issues: 1 critical (must fix)
- Performance issues: 1 should-fix

🎯 Recommendation: REQUEST CHANGES
Fix critical security issue before merging.
Address N+1 query for better performance.
Add missing test case for completeness.

Once addressed, this PR will be ready to merge.
```

### **Review Categories**:

```
✅ APPROVED
- Good practices identified
- Well-implemented features
- Proper error handling
- Comprehensive tests

💬 SUGGESTIONS
- Nice-to-have improvements
- Optimization opportunities
- Better patterns available
- Documentation enhancements

⚠️ CONCERNS
- Should fix before merge
- Performance issues
- Missing edge cases
- Unclear code

🔴 BLOCKERS
- Must fix before merge
- Security vulnerabilities
- Breaking changes
- Critical bugs
```

### **Use Cases**:
- ✅ Before merging PRs
- ✅ Code review automation
- ✅ Learning from feedback
- ✅ Maintaining code quality standards
- ✅ Team collaboration
- ✅ Onboarding new developers

---

## 9️⃣ security-review

**Purpose**: Comprehensive security analysis of code changes

**Invocation**: `/security-review` or ask "Run a security review"

### **Areas Covered**:

#### **A. Credential & Secret Exposure** 🔑
Detects:
- Hardcoded passwords
- API keys in code
- AWS access keys and secret keys
- Database credentials
- Private keys (SSH, PEM)
- OAuth tokens and secrets
- JWT secrets
- Encryption keys

**Examples Caught**:
```javascript
// ❌ CRITICAL
const apiKey = "sk-1234567890abcdef";
const dbPassword = "MyP@ssw0rd123";

// ✅ CORRECT
const apiKey = process.env.API_KEY;
const dbPassword = process.env.DB_PASSWORD;
```

#### **B. Injection Vulnerabilities** 💉
Detects:
- SQL injection
- Command injection
- Cross-Site Scripting (XSS)
- Code injection
- Path traversal
- LDAP injection
- XML injection

**Examples Caught**:
```python
# ❌ SQL Injection Risk
query = f"SELECT * FROM users WHERE id = {user_id}"

# ✅ SAFE - Parameterized query
query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_id,))
```

```javascript
// ❌ Command Injection Risk
exec(`git clone ${userInput}`);

// ✅ SAFE - Validate and sanitize
if (!/^[a-zA-Z0-9-_.]+$/.test(userInput)) {
  throw new Error('Invalid input');
}
```

#### **C. Authentication & Authorization** 👤
Detects:
- Missing authentication checks
- Weak password policies
- Insecure session management
- Authorization bypass opportunities
- Improper access controls
- Missing RBAC checks

**Examples Caught**:
```javascript
// ❌ Missing auth check
app.get('/admin/users', (req, res) => {
  return User.findAll(); // Anyone can access!
});

// ✅ SAFE - Auth required
app.get('/admin/users', requireAuth, requireAdmin, (req, res) => {
  return User.findAll();
});
```

#### **D. Data Exposure** 📊
Detects:
- Sensitive data in logs
- Unencrypted data transmission
- Insecure data storage
- PII (Personal Identifiable Information) handling
- Excessive data exposure in APIs
- Debug info in production

**Examples Caught**:
```javascript
// ❌ PII in logs
console.log('User login:', user.email, user.password);

// ✅ SAFE - No sensitive data
console.log('User login successful:', user.id);
```

#### **E. Configuration Issues** ⚙️
Detects:
- Debug mode enabled in production
- Insecure default configurations
- Overly permissive CORS settings
- Missing security headers
- Insecure dependencies
- Exposed error stack traces

**Examples Caught**:
```javascript
// ❌ Insecure CORS
app.use(cors({ origin: '*' }));

// ✅ SAFE - Restricted CORS
app.use(cors({ 
  origin: ['https://app.example.com'],
  credentials: true 
}));
```

#### **F. Cloud Security (AWS/Azure/GCP)** ☁️
Detects:
- Overly permissive IAM roles/policies
- Public S3 buckets (when not intended)
- Open security groups (0.0.0.0/0)
- Missing encryption at rest
- Missing encryption in transit
- Insecure CloudFormation/Terraform templates

**Examples Caught**:
```yaml
# ❌ Overly permissive IAM
Effect: Allow
Action: "*"
Resource: "*"

# ✅ SAFE - Least privilege
Effect: Allow
Action:
  - s3:GetObject
  - s3:PutObject
Resource: arn:aws:s3:::my-bucket/*
```

#### **G. Code Quality & Best Practices** ✅
Detects:
- Use of unsafe functions (`eval`, `exec`)
- Missing input validation
- Improper error handling
- Security anti-patterns
- OWASP Top 10 vulnerabilities
- CWE (Common Weakness Enumeration)

**Examples Caught**:
```javascript
// ❌ Unsafe eval
const result = eval(userInput);

// ✅ SAFE - Use JSON.parse or safe alternatives
const result = JSON.parse(userInput);
```

### **Security Standards Checked**:
- ✅ **OWASP Top 10** (2021)
- ✅ **CWE Top 25** (Common Weakness Enumeration)
- ✅ **AWS Security Best Practices**
- ✅ **SANS Top 25** Software Errors
- ✅ **PCI DSS** (Payment Card Industry)
- ✅ **GDPR** (Data Protection)
- ✅ **HIPAA** (Healthcare data)

### **Output Example**:

```
Security Review Report
=====================

📊 Scan Summary
- Files analyzed: 15
- Lines scanned: 2,847
- Issues found: 7
- Critical: 2
- High: 2
- Medium: 2
- Low: 1

🔴 CRITICAL (Fix immediately - 2 issues)

📄 src/config/aws.ts:12
❌ Hardcoded AWS credentials
Severity: CRITICAL
CWE-798: Use of Hard-coded Credentials

Issue:
const credentials = {
  accessKeyId: 'AKIA...[REDACTED]',
  secretAccessKey: '[REDACTED]'
};

Fix:
1. Remove credentials from code immediately
2. Use AWS IAM roles or environment variables
3. Rotate exposed credentials in AWS Console
4. Add .env to .gitignore
5. Use AWS Secrets Manager for production

Recommended:
import { fromEnv } from '@aws-sdk/credential-providers';
const credentials = fromEnv();

📄 src/api/users.ts:45
❌ SQL Injection vulnerability
Severity: CRITICAL
CWE-89: SQL Injection

Issue:
const query = `SELECT * FROM users WHERE email = '${email}'`;
db.execute(query);

Fix:
Use parameterized queries:
const query = 'SELECT * FROM users WHERE email = ?';
db.execute(query, [email]);

Or use ORM:
const user = await User.findOne({ where: { email } });

🟠 HIGH (Fix before deployment - 2 issues)

📄 src/middleware/auth.ts:23
⚠️ Missing authentication check
Severity: HIGH
CWE-306: Missing Authentication

Issue:
app.get('/api/admin/users', (req, res) => {
  // No authentication check!
});

Fix:
app.get('/api/admin/users', 
  requireAuth,
  requireRole('admin'),
  (req, res) => { ... }
);

📄 template.yaml:67
⚠️ Overly permissive IAM policy
Severity: HIGH
CWE-732: Incorrect Permission Assignment

Issue:
Action: "*"
Resource: "*"

Fix:
Action:
  - s3:GetObject
  - s3:PutObject
Resource: !Sub "arn:aws:s3:::${BucketName}/*"

🟡 MEDIUM (Should fix - 2 issues)

📄 src/api/cors.ts:8
⚠️ Overly permissive CORS
Severity: MEDIUM

Issue:
origin: '*'

Recommendation:
origin: process.env.ALLOWED_ORIGINS?.split(',') || []

📄 src/utils/logger.ts:34
⚠️ Sensitive data in logs
Severity: MEDIUM

Issue:
logger.info('User data:', user);

Fix:
logger.info('User action:', { userId: user.id, action: 'login' });

🟢 LOW (Consider fixing - 1 issue)

📄 src/config/app.ts:15
ℹ️ Debug mode may be enabled
Severity: LOW

Issue:
const DEBUG = true;

Recommendation:
const DEBUG = process.env.NODE_ENV === 'development';

✅ PASSED CHECKS (18 items)
✓ No XSS vulnerabilities detected
✓ CSRF protection in place
✓ Password hashing uses bcrypt
✓ HTTPS enforced
✓ Security headers configured
✓ Input validation present
✓ Rate limiting implemented
✓ Session timeout configured
✓ Encryption at rest enabled
✓ Audit logging enabled

📈 Security Score: 72/100

Breakdown:
- Critical issues: -20 (2 issues)
- High issues: -10 (2 issues)
- Medium issues: -4 (2 issues)
- Low issues: -1 (1 issue)
- Good practices: +15

🎯 Recommendation: DO NOT MERGE
Fix 2 critical issues immediately:
1. Remove hardcoded AWS credentials
2. Fix SQL injection vulnerability

After fixes, re-run security review.

⚠️ IMPORTANT
The hardcoded AWS credentials are now exposed.
Rotate them immediately in AWS IAM console:
1. Go to IAM → Users → Security Credentials
2. Deactivate exposed access key
3. Create new access key
4. Use environment variables
```

### **When to Use**:

**Always Before**:
- ✅ Deploying to production
- ✅ Pushing to main/master branch
- ✅ Creating pull requests
- ✅ Merging feature branches
- ✅ Publishing packages

**Especially Important For**:
- ✅ AWS/Cloud infrastructure changes
- ✅ Authentication/authorization code
- ✅ API endpoints (especially public)
- ✅ Database queries
- ✅ File upload/download features
- ✅ Payment processing
- ✅ User data handling
- ✅ Third-party integrations

### **Use Cases**:
- ✅ Pre-deployment security checks
- ✅ Code review security validation
- ✅ Compliance audits (PCI, HIPAA, GDPR)
- ✅ Security training and awareness
- ✅ Vulnerability detection
- ✅ Best practices enforcement

---

## 🎯 Recommended Workflow Using All Skills

### **Project Initialization** (Day 1)

```bash
# Document the project
/init

# Set up automation and permissions
/update-config
# Configure: pre-commit hooks, auto-approve safe commands

# Customize shortcuts (optional)
/keybindings-help

# Reduce workflow friction
/fewer-permission-prompts
```

**Result**: Well-documented, automated, efficient workflow

---

### **During Development**

```bash
# After writing significant code
/simplify
# Optimizes code, removes duplication, improves quality

# Continuous security monitoring
/loop 15m /security-review
# Periodic security checks while developing
```

**Result**: Clean, optimized, secure code

---

### **Before Commit/PR**

```bash
# Security check
/security-review
# Catch vulnerabilities before they reach production

# Code quality review
/review
# Ensure best practices and quality standards

# Final cleanup
/simplify
# Last pass optimization
```

**Result**: Production-ready, secure, high-quality code

---

### **During Deployment**

```bash
# Monitor deployment progress
/loop 2m "aws cloudformation describe-stacks --stack-name my-app"
# Track deployment status

# Check health after deployment
/loop 30s "curl https://api.example.com/health"
# Verify service is up
```

**Result**: Monitored, verified deployment

---

### **Building AI Features**

```bash
# When building Claude API apps
/claude-api
# Generates SDK code, implements caching, tools, streaming
```

**Result**: Optimized AI integration

---

## 📊 Skill Effectiveness Matrix

| Skill | Time Saved | Quality Impact | Security Impact | Learning Curve |
|-------|-----------|----------------|-----------------|----------------|
| **update-config** | High | Medium | Medium | Medium |
| **keybindings-help** | Low | Low | None | Low |
| **simplify** | Medium | High | Low | Low |
| **fewer-permission-prompts** | High | Low | None | Low |
| **loop** | High | Low | None | Low |
| **claude-api** | High | High | Medium | Medium |
| **init** | Medium | High | None | Low |
| **review** | High | High | Medium | Low |
| **security-review** | Medium | Medium | High | Low |

---

## 🎓 Skill Learning Path

### **Beginner** (Start Here)
1. **fewer-permission-prompts** - Immediate productivity boost
2. **init** - Understand project documentation
3. **simplify** - Learn code quality practices

### **Intermediate** (Build on Basics)
4. **update-config** - Automate workflows
5. **review** - Improve code review skills
6. **security-review** - Security awareness

### **Advanced** (Power User)
7. **loop** - Continuous monitoring
8. **claude-api** - AI integration
9. **keybindings-help** - Ultimate customization

---

## 💡 Pro Tips

### **Combine Skills for Maximum Impact**

```bash
# Set up automation to run security review before every commit
/update-config
# Configure: "pre-commit": "/security-review && /simplify"

# Monitor deployment and notify on completion
/loop 2m "check deployment && notify team when done"

# Build AI app with best practices
/claude-api
# Then run /review to check generated code
```

### **Create Custom Workflows**

```json
{
  "workflows": {
    "pre-deploy": [
      "/security-review",
      "/review",
      "/simplify"
    ],
    "daily": [
      "/loop 1h /security-review"
    ]
  }
}
```

---

## ✅ Quick Reference

| Need | Use Skill | Command |
|------|-----------|---------|
| Set up hooks | update-config | `/update-config` |
| Custom shortcuts | keybindings-help | `/keybindings-help` |
| Clean up code | simplify | `/simplify` |
| Reduce prompts | fewer-permission-prompts | `/fewer-permission-prompts` |
| Monitor status | loop | `/loop 5m "check status"` |
| Build AI app | claude-api | `/claude-api` |
| Document project | init | `/init` |
| Review PR | review | `/review` |
| Security check | security-review | `/security-review` |

---

## 🔗 Related Documentation

- [CLAUDE_README.md](./CLAUDE_README.md) - Token usage and development metrics
- [CLAUDE_COMPARISON_README.md](./CLAUDE_COMPARISON_README.md) - Cost comparison across models
- [CLAUDE_SKILLS.md](./CLAUDE_SKILLS.md) - APEX configuration analysis
- [PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md) - Project architecture

---

**Project**: US Time Map  
**Organization**: APEX  
**Repository**: https://github.com/ajanardhanan/us-time-map  
**Claude Version**: Sonnet 4.5  
**Date**: August 2, 2026
