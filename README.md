<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" height="128px" srcset="icon.png">
    <img alt="logo" height="128px" src="icon.png">
  </picture>
  <h1 align="center">Alfred Ollama</h1>
</div>

Use [Ollama](https://ollama.ai) for local llama inference on Alfred.

## Requirements

[Ollama](https://ollama.ai) installed and running on your mac. At least one model need to be installed throw Ollama cli tools.

required install model: `llama2`
```bash
ollama run llama2
```

## How to Use

### Command: Chat With Ollama

Command is `olla` and you can use it to chat with Ollama.
![screenshot](screenshot.png)

### WIP
- [ ] Add support for multiple models (currently only one model(`llama2`) is supported)
