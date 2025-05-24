from langchain.text_splitter import CharacterTextSplitter

class ChunkFixedSize:
    '''
        O CharacterTextSplitter funciona da seguinte forma:

        Divide o texto em partes de tamanho fixo (chunk_size=100), medido em número de caracteres.
        Mantém uma sobreposição (chunk_overlap=20) entre os chunks para garantir que o contexto não seja perdido entre as partes.
        Usa espaços em branco (separator=" ") para definir onde o texto pode ser dividido.
        No exemplo, o texto tem 376 caracteres. Com chunk_size=100 e chunk_overlap=20, o texto será dividido em 4 chunks:

        Chunk 1: 100 caracteres.
        Chunk 2: 100 caracteres (com 20 caracteres sobrepostos do Chunk 1).
        Chunk 3: 100 caracteres (com 20 caracteres sobrepostos do Chunk 2).
        Chunk 4: 56 caracteres (o restante do texto).
    '''
    
    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str) -> list[str]:
        text_splitter = CharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        return text_splitter.split_text(text)
    
# Exemplo 
texto_exemplo = """
A inteligência artificial está revolucionando diversos setores.
No setor de saúde, algoritmos de machine learning auxiliam no diagnóstico precoce de doenças.
Na educação, sistemas adaptativos personalizam o aprendizado.
No varejo, a IA otimiza a experiência do cliente através de recomendações personalizadas.
"""

# Configuração do splitter 
splitter_fixo = CharacterTextSplitter(chunk_size=100, chunk_overlap=20, separator=" ")

# Aplicando chunking 
chunks = splitter_fixo.split_text(texto_exemplo)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
    print(f"Tamanho do chunk: {len(chunk)} caracteres \n")