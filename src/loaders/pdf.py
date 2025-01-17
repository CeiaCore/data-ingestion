from PyPDF2 import PdfReader
import pdfplumber

# LlamaParse
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

# Env here??
from dotenv import load_dotenv
import os

load_dotenv()


class PDFLoader:
    def __init__(self):
        print("PDFLoader initialized")

    def get_text(file_path):
        """
            Carrega um arquivo PDF e retorna o texto do arquivo.
        """
        return PDFLoader.get_text_pdfplumber(file_path)
    
    def get_pages(file_path):
        """
            Carrega um arquivo PDF e retorna uma lista de objetos do seguinte formato { "text": str, "page": int }
        """
        return PDFLoader.get_pages_pdfplumber(file_path)

    @staticmethod
    def get_text_PyPDF2(file_path):
        """ 
        (PyPDF2) Retorna o texto de um arquivo PDF utilizando a biblioteca PyPDF2.
        Não consegue extrair tabelas com acurácia e não extrai imagens.
        """
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            print(f"Erro ao ler o arquivo {file_path}: {e}")
            return ""
        
    @staticmethod
    def get_pages_PyPDF2(file_path):
        """ 
            (PyPDF2) Retorna uma lista de objetos do seguinte formato { "text": str, "page": int, "source": str }
            Não consegue extrair tabelas com acurácia e não extrai imagens.
        """
        try:
            reader = PdfReader(file_path)
            pages = []
            for i, page in enumerate(reader.pages):
                pages.append({
                    "text": page.extract_text(),
                    "page": i + 1,
                    "source": file_path
                })
            return pages
        except Exception as e:
            print(f"Erro ao ler o arquivo {file_path}: {e}")
            return []
        

    def get_text_pdfplumber(pdf_path):
        whole_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    whole_text += f"{text}\n\n"
        return whole_text
    
    def get_pages_pdfplumber(pdf_path):
        pages = []
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    pages.append({
                        "text": text,
                        "page": i + 1,
                        "source": pdf_path
                    })
        return pages
        
    
    async def get_text_LlamaParse(file_path):
        """
            (LlamaParse) Retorna o texto de um arquivo PDF utilizando a biblioteca LlamaParse.
            Consegue extrair tabelas com acurácia e extrai imagens.
        """

        api_key = os.getenv("LLAMA_PARSE_API_KEY")

        parser = LlamaParse(api_key=api_key, num_wokers=4, result_type="markdown")
        
        pages = await parser.aload_data(file_path)

        return pages
