# AI Dataset Generator: MCP-Based Synthetic SMS Dataset Creation Pipeline

A Model Context Protocol (MCP) server for generating synthetic SMS datasets in multiple linguistic varieties using Claude (Anthropic). Developed to support multilingual SMS phishing (smishing) detection research across Bengali, English, Banglish, and Code-Mixed formats.

## Overview

This tool automates the generation of synthetic SMS datasets across four linguistic formats, each containing three distinct message categories. The generated datasets are designed for training and evaluating multilingual smishing detection models.

| Target Language | Description | Generator Tool | Save Tool |
|----------------|-------------|----------------|-----------|
| **Bengali** | Native Bengali script | `generate_bangla_dataset()` | `save_bangla_dataset()` |
| **English** | Full English translation | `generate_english_dataset()` | `save_english_dataset()` |
| **Banglish** | Romanized Bengali (Latin script) | `generate_banglish_dataset()` | `save_banglish_sms()` |
| **Code-Mixed** | Bengali-English code-switched text | `generate_code_mixed_dataset()` | `save_code_mixed_dataset()` |

## Message Categories

Each dataset contains three balanced classes:

| Label | Description | Examples |
|-------|-------------|----------|
| **smish** | Fraudulent, phishing, or scam messages | Fake bank alerts, lottery scams, suspicious links, crypto fraud |
| **promo** | Promotional or marketing messages | Telecom offers, product discounts, cashback deals, sales announcements |
| **normal** | Everyday personal or casual messages | Greetings, daily conversations, friendly chats, personal updates |

## Architecture

The generation pipeline is built on the **Model Context Protocol (MCP)** framework, which enables structured, reproducible prompt engineering for each linguistic variety. Each dataset type is handled by a dedicated MCP tool with domain-specific instructions and context-aware generation rules.

```
User Request → MCP Server (main.py) → Claude (Anthropic)
                                           ↓
                                   Synthetic CSV Data
                                           ↓
                              bangla_sms.csv
                              english_sms.csv
                              banglish_sms.csv
                              code_mixed_sms.csv
```

## Files

| File | Description |
|------|-------------|
| `main.py` | MCP server with dataset generation tool definitions and prompt templates |
| `bangla_sms.csv` | Generated Bengali SMS dataset |
| `english_sms.csv` | Generated English SMS dataset |
| `banglish_sms.csv` | Generated Banglish SMS dataset |
| `code_mixed_sms.csv` | Generated Code-Mixed SMS dataset |

## Requirements

- Python 3.10+
- `mcp` library (`pip install mcp`)
- Claude Desktop or Claude Code with MCP support
- FastMCP framework

## Installation

```bash
# Install dependencies
pip install mcp fastmcp

# Clone or download the project
git clone <repository-url>
cd ai-dataset-generator

# Run the MCP server
python main.py
```

## Usage

### 1. Configure MCP Server
Add the server configuration to your Claude Desktop or Claude Code MCP settings:

```json
{
  "mcpServers": {
    "ai-dataset-generator": {
      "command": "python",
      "args": ["/path/to/main.py"]
    }
  }
}
```

### 2. Generate Datasets

Use the generation tools with your desired sample count:

```python
# Generate 100 Bengali SMS messages
generate_bangla_dataset(sample_count=100)

# Generate 50 English SMS messages  
generate_english_dataset(sample_count=50)

# Generate 75 Banglish SMS messages
generate_banglish_dataset(sample_count=75)

# Generate 100 Code-Mixed SMS messages
generate_code_mixed_dataset(sample_count=100)
```

### 3. Save Generated Data

After Claude generates the CSV data, save it using the corresponding save function:

```python
# Save Bengali messages
save_bangla_dataset(messages="<generated_csv_content>")

# Save English messages
save_english_dataset(messages="<generated_csv_content>")

# Save Banglish messages
save_banglish_sms(messages="<generated_csv_content>")

# Save Code-Mixed messages
save_code_mixed_dataset(messages="<generated_csv_content>")
```

## Prompt Design

Each generation tool constructs a structured prompt that instructs Claude to:

- **Output Format:** Strict CSV format with `label` and `text` columns
- **Bangladeshi Context:** Local banks (Sonali Bank, Dutch-Bangla Bank), telecom operators (Grameenphone, Robi, Banglalink), currency (TK/টাকা), common names, and places
- **Diversity Requirements:** Varied vocabulary, sentence structures, tones, and message lengths (20-70 words)
- **Realistic Details:** Phone numbers, amounts, URLs, OTP codes, verification links
- **Class-Specific Characteristics:**
  - **Smish:** Urgent tone, malicious intent, fake authority, pressure tactics
  - **Promo:** Persuasive language, attractive offers, call-to-action, limited-time deals
  - **Normal:** Conversational tone, natural language, everyday topics, friendly interaction
- **Uniqueness:** Avoids repetition, ensures each message is distinct

### Code-Mixed Specifics

The code-mixed dataset maintains approximately **50% Bengali (Bangla script) and 50% English** in each message, reflecting authentic bilingual communication patterns common in Bangladesh.

## Dataset Format

All generated datasets follow this CSV structure:

```csv
label,text
smish,"আপনার ডাচ্-বাংলা ব্যাংক অ্যাকাউন্ট ব্লক হয়েছে। এখনই কল করুন: +8801818788890"
promo,"Special deal last day, 30GB @300TK, 30 days! Get it today- cutt.ly/jwkuSC76"
normal,"কাল ক্লাসে যাচ্ছো তো? আমি সকাল ৯টায় চলে যাবো।"
```

## Features

- ✅ **Automatic Deduplication:** Prevents duplicate messages from being saved
- ✅ **Incremental Saving:** Appends new messages to existing datasets
- ✅ **Multi-Linguistic Support:** Four distinct linguistic varieties
- ✅ **Balanced Classes:** Even distribution across smish, promo, and normal categories
- ✅ **Contextual Generation:** Bangladesh-specific names, institutions, and conventions
- ✅ **CSV Validation:** Proper quoting for special characters and commas

## Research Applications

This tool is designed for:

- **Smishing Detection Research:** Training multilingual SMS phishing classifiers
- **NLP Model Development:** Testing cross-lingual transfer learning
- **Code-Switching Studies:** Analyzing Bengali-English code-mixed communication
- **Low-Resource Language Research:** Generating synthetic training data
- **Cybersecurity Education:** Creating realistic phishing awareness datasets

## Limitations

- Generated data is synthetic and may not capture all real-world variations
- Requires human validation for quality assurance
- Distribution balance depends on Claude's generation consistency
- May require multiple generation runs for large datasets (500+ samples)

## Best Practices

1. **Generate in Batches:** Create 50-100 samples per request for optimal quality
2. **Review Outputs:** Manually inspect generated messages for authenticity
3. **Iterative Refinement:** Regenerate specific categories if distribution is unbalanced
4. **Combine with Real Data:** Use synthetic data to augment, not replace, real datasets
5. **Version Control:** Track different generation runs for reproducibility

## Citation

If you use this tool in your research, please cite:

```bibtex
@software{ai_dataset_generator_2025,
  title={AI Dataset Generator: MCP-Based Synthetic SMS Dataset Creation Pipeline},
  author={[Your Name]},
  year={2025},
  url={[Repository URL]}
}
```

## Related Projects

- **SmishDetect-LLM Framework:** Multilingual SMS security detection
- **Bengali NLP Resources:** [HuggingFace Collections](https://huggingface.co/collections)
- **MCP Documentation:** [Model Context Protocol](https://modelcontextprotocol.io/)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-language`)
3. Commit your changes (`git commit -m 'Add Hindi dataset generator'`)
4. Push to the branch (`git push origin feature/new-language`)
5. Open a Pull Request

## License

This project is part of academic research. Please contact the author for usage permissions.

## Contact

For questions, issues, or collaboration opportunities:

- **Email:** shariul.islam.au@gmail.com
- **Institute:** Murdoch University

---

**Note:** This tool generates synthetic data using AI. Always validate generated datasets for quality and appropriateness before use in production systems or published research.
