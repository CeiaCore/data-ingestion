from langchain.text_splitter import RecursiveCharacterTextSplitter

class Splitter:
    def __init__(self):
        print("BasicSplitter initialized")

    def get_chunks(self, text, chunk_size=1024, chunk_overlap=200):
        return self.recursively_split(text, chunk_size, chunk_overlap)
    
    def recursively_split(self, text, chunk_size=1024, chunk_overlap=200):

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        texts = text_splitter.split_text(text)

        return texts