# OpenAI GPT-3

This project uses Artificial Intelligence of GPT-3 to generate texts using questions or descriptions as inputs.

# Quickstart

```bash
pip install -r requirements.txt
```

You must create an account in [OpenAI website](https://openai.com/api/)

Following, open a terminal inside this project folder and type following command to create a ```.env``` file:

```bash
echo <YOUR_OPENAI_SECRET_KEY> > .env
```

> Note: replace ```<YOUR_OPENAI_SECRET_KEY>``` with given in your own [OpenAI profile webpage](https://beta.openai.com/account/api-keys)

## Usage

```python
python main.py
```

Then, input a text and see the response.

App going to still question. If you wish to finish, just let in blank pressing <kbd>Enter</kbd>.
