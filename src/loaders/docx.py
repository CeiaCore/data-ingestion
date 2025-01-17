
import mammoth
import markdownify

class DOCXLoader:
    def __init__(self):
        print("DOCLoader initialized")

    def get_text(file_path):
        """
            Carrega um arquivo DOCX e retorna o texto do arquivo.
        """
        return DOCXLoader.get_text_mammoth(file_path)
    
    @staticmethod
    def get_text_mammoth(doc_path):
        """
        Retorna o texto de um arquivo DOCX utilizando a biblioteca Mammoth.
        """
        try:
            with open(doc_path, "rb") as doc_file:
                result = mammoth.extract_raw_text(doc_file)
                return result.value
        except Exception as e:
            print(f"Erro ao ler o arquivo {doc_path}: {e}")
            return ""
        
    @staticmethod
    def get_md_mammoth(doc_path):
        """
        Retorna o markdown de um arquivo DOCX utilizando a biblioteca Mammoth.
        """
        try:
            with open(doc_path, "rb") as doc_file:
                result = mammoth.convert_to_html(doc_file)
                html = result.html
                md = markdownify.markdownify(html, heading_style="ATX")

                return md
        except Exception as e:
            print(f"Erro ao ler o arquivo {doc_path}: {e}")
            return ""