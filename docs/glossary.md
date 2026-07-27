# Glossary

This glossary defines terms as they are used throughout Project Gyaan. It is intentionally concise and grows alongside the series.

---

## AI-Native System

A software system where model-driven intelligence is a first-class architectural primitive rather than an isolated API call.

An AI-native system is designed around capabilities such as dynamic context, probabilistic reasoning, planning, memory, evaluation, and feedback.

---

## Context

The information supplied to a language model to help it complete a task.

Context can include:

- User instructions
- Conversation history
- Retrieved documents
- Tool outputs
- Structured data
- System prompts

The quality of the context often matters more than the size of the model.

---

## Embedding

A numerical representation of data that captures semantic meaning.

Embeddings allow software to compare pieces of text based on meaning rather than exact keywords and form the foundation of semantic search.

---

## Large Language Model (LLM)

A machine learning model trained to predict the next token in a sequence.

In Project Gyaan, the LLM is treated as one component within a larger system rather than the system itself.

---

## Memory

Information preserved across interactions to provide continuity.

Memory enables a system to remember previous conversations, user preferences, goals, or important facts instead of treating every request independently.

---

## Planner

**Introduced in:** [Article 01 – What Makes a System AI-Native](../articles/article-01/01-What-makes-system-ai-native.md)

A component responsible for deciding how to solve a task.

Rather than immediately calling an LLM, a planner may decide to:

- Retrieve additional knowledge
- Invoke external tools
- Break a task into smaller steps
- Retry or revise an answer

---

## Prompt

The complete input provided to a language model.

A prompt typically consists of much more than a user's question and may include instructions, retrieved context, conversation history, examples, and tool outputs.

---

## Prompt Engineering

The practice of designing prompts that guide a language model toward better outputs.

As systems become more capable, prompt engineering evolves into **context engineering**, where assembling the right information becomes more important than carefully wording individual instructions.

---

## Retrieval

The process of finding relevant information from external knowledge sources before invoking a language model.

Retrieval allows systems to answer questions using information that was not present during the model's training.

---

## Retrieval-Augmented Generation (RAG)

An architectural pattern that combines retrieval with language model generation.

Rather than relying solely on the model's internal knowledge, a RAG system retrieves relevant information and includes it as context before generating a response.

---

## Tool

An external capability that an AI system can invoke to perform actions or obtain information.

Examples include:

- Calling an API
- Querying a database
- Executing code
- Sending an email
- Reading a document

---

## Validator

A component that evaluates model outputs before they are accepted.

A validator may check:

- Factual accuracy
- Output format
- Safety
- Business rules
- Confidence

Rather than generating answers, validators determine whether an answer is acceptable or whether another attempt is needed.

---

## Vector Store

A specialized database for storing embeddings and performing similarity search.

Instead of matching exact keywords, a vector store retrieves information based on semantic similarity.
