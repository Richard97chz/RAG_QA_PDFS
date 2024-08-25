@echo off
REM Activar el entorno virtual
call C:\Users\Fytli\LLM_Bootcamp2024\RAG_QA_PDFS_venv\Scripts\activate.bat

REM Ejecutar el script Python
python C:\Users\Fytli\LLM_Bootcamp2024\RAG_QA_PDFS_venv\RAG_QA_PDFS\rag-data-loader\rag_load_and_process.py

REM Desactivar el entorno virtual (opcional)
deactivate
