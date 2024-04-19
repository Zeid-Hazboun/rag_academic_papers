# Langchain RAG program for academic papers QA system

Most of the code is originally from the following youtube tutorial: https://www.youtube.com/watch?v=tcqEUSNCn8I&t=254s&ab_channel=pixegami

This projects started off as a tutorial on how to implement RAG using langchain. Once implemented, I wanted a way to make this useful for myself and other students. The steps for running the scripts can be seen below. There are still currently some problems with the file. It works for one paper ("attention is all you need"), however not for the other papers in the data/papers_pdf folder/

Install dependencies.

```python
pip install -r requirements.txt
```

You'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work. You can do that by running the following in the terminal:

```python
export OPENAI_API_KEY=‘your_openAI_key’
```

Change any pdf files to markdown
```python
python pdf_to_markdown.py <folder_path>
```

Create the Chroma DB.

```python
python create_database.py <folder_path>
```

Query the Chroma DB.

```python
python query_data.py 'What is the attention mechanism?'
```
