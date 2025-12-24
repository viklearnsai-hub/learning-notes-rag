# Learning Notes RAG Assistant

A simple Retrieval-Augmented Generation (RAG) system that allows users to upload learning notes and ask questions grounded strictly in the uploaded content.

# Creating Virtual Env

- python -m <venv_name>

# Activating it

in the venv_name folder looks for "scripts folder" and then ".bat" file and execute it in terminal

# Start the server

    uvicorn app.main:app --reload

# Debuggin

Create a Debug Configuration (One Time)

This is the Python equivalent of a Run/Debug configuration in IntelliJ.

Go to Run & Debug tab (left sidebar)

Click “create a launch.json file”

Choose Python

Choose “Module”

# Review command

git diff <old_commit> <new_commit> > code_review_git_diff.txt
