# Model Context Protocol (MCP): Schnittstellen für LLMs schaffen

## Wichtige Keytakeaways

- MCP ist ein Protokoll für die Kommunikation zwischen AI-Anwendungen und Tools/Services.
- Das Protokoll ermöglicht es LLMs, Funktionen aufzurufen und mit externen Systemen zu interagieren.
- MCP Server sind unabhängig vom eigentlichen LLM und laufen auf der Client-Seite.
- Es gibt bereits ein großes Ökosystem von MCP Servern für verschiedene Anwendungsfälle.
- Sicherheitsaspekte müssen auf mehreren Ebenen berücksichtigt werden (Prompt-Filtering, Berechtigungen etc.).

## Behandelte Kernfragen

- Was ist das Model Context Protocol und wie funktioniert es?
- Wie unterscheidet sich MCP von RAG (Retrieval Augmented Generation)?
- Welche Sicherheitsrisiken gibt es bei der Verwendung von MCP?
- Wie kann MCP in der Softwareentwicklung eingesetzt werden?
- Wie erfolgt die Kommunikation zwischen Client, MCP Server und LLM?

## Glossar wichtiger Begriffe

- MCP (Model Context Protocol): Protokoll für die Kommunikation zwischen AI-Anwendungen und externen Tools
- Function Calling: Fähigkeit eines LLMs, definierte Funktionen aufzurufen
- Prompt Stuffing: Technik, bei der zusätzliche Informationen in den Prompt eingefügt werden
- Prompt Injection: Sicherheitsrisiko durch manipulierte Prompts
- RAG (Retrieval Augmented Generation): Technik zur kontextbasierten Generierung von Antworten
- JSON-RPC: Protokoll für den Austausch von Nachrichten zwischen MCP Client und Server
- Language Server Protocol: Von Microsoft entwickeltes Protokoll für IDE-Erweiterungen
