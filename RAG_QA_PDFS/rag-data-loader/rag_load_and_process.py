import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader
from langchain_community.vectorstores.pgvector import PGVector
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document  # Importar el esquema de Document

# Cargar las variables de entorno
load_dotenv()

# Recuperar las credenciales desde el archivo .env
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Crear la cadena de conexión usando las variables de entorno
connection_string = f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Configurar el cargador de directorios
loader = DirectoryLoader(
    os.path.abspath("../pdf-documents"),
    glob="**/*.pdf",
    use_multithreading=True,
    show_progress=True,
    max_concurrency=50,
    loader_cls=UnstructuredPDFLoader,
)

# Cargar los documentos
docs = loader.load()

# Inicializar las embeddings
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')

# Inicializar el separador de texto semántico
text_splitter = SemanticChunker(embeddings=embeddings)

# Extraer el contenido de cada documento
flattened_docs = [doc.page_content for doc in docs if doc.page_content]

# Dividir los textos en fragmentos usando split_text para cada documento
chunks = [text_splitter.split_text(doc) for doc in flattened_docs]

# Convertir cada fragmento en un objeto Document
chunk_documents = [Document(page_content=chunk) for sublist in chunks for chunk in sublist]

# Guardar los fragmentos en la base de datos PostgreSQL usando PGVector
PGVector.from_documents(
    documents=chunk_documents,
    embedding=embeddings,
    collection_name="collection164",
    connection_string=connection_string,
    pre_delete_collection=True,
)
