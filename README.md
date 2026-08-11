# Project Gyaan

> *"Knowledge begins with curiosity."*

**Gyaan** (ज्ञान, pronounced **"gyaan"**) is an AI-native research assistant built from first principles.

This repository accompanies the **AI-Native System Design** series, where we build Gyaan in public, one architectural decision at a time. Rather than hiding complexity behind frameworks, we explore the fundamental building blocks of AI-native systems: memory, planning, tool calling, workflows, observability, evaluation, and production reliability.

Every article, every commit, every release, and every design decision lives here.


## Start Here

1. [Introducing Project Gyaan](articles/00-introducing-gyaan.md)
2. [What Makes a System AI-Native?](articles/article-01/01-What-makes-system-ai-native.md)

## Project Foundations

- [Philosophy](docs/philosophy.md)
- [Roadmap](docs/roadmap.md)
- [Architecture Decisions](docs/adr/)
- [Glossary](docs/glossary.md)

## Current Status

Project Gyaan is now in the implementation phase. The current system
provides a command-line application with a provider-independent
`ChatModel` abstraction and implementations for Echo, OpenAI, and Ollama.

See the roadmap for what comes next.

## Architecture

Gyaan's application layer depends on a `ChatModel` abstraction, not on any specific provider:

```
GyaanApplication
        |
        v
    ChatModel
    /   |    \
   /    |     \
Echo  OpenAI  Ollama
```

Changing the model provider is a composition/configuration change, not an application-layer change.

## Running Gyaan

Install Gyaan into a virtual environment:

```bash
pip install -e ".[dev]"
```

Gyaan reads configuration from environment variables (see [`.env.example`](.env.example)). It does not load `.env` files automatically, so export these variables in your shell before running `gyaan`.

### Echo — default

- Works immediately.
- No LLM, API key, or local service required.
- It's a deterministic implementation of `ChatModel` that echoes the prompt back, which lets the CLI and architecture run without any AI infrastructure.

```bash
gyaan "What makes a system AI-native?"
```

### OpenAI

- Requires an OpenAI API key and available credits.

```bash
export GYAAN_PROVIDER=openai
export GYAAN_MODEL=<openai-model-name>
export OPENAI_API_KEY=<your-openai-api-key>

gyaan "What makes a system AI-native?"
```

### Ollama — local LLM

Ollama lets you run Gyaan against a local LLM without an API key.

- Requires [Ollama](https://ollama.com/download) installed, with the service running. The desktop app manages this for you; if you're running Ollama headless, start it manually with `ollama serve`.
- Recommended quick-test model: `qwen3:0.6b`. It is a small model intended here to verify the Gyaan → Ollama integration, not as a recommendation for model quality.

Pull the model:

```bash
ollama pull qwen3:0.6b
```

Configure Gyaan:

```bash
export GYAAN_PROVIDER=ollama
export GYAAN_MODEL=qwen3:0.6b
```

Run:

```bash
gyaan "What makes a system AI-native?"
```

You can replace `qwen3:0.6b` with any Ollama model available on your system.